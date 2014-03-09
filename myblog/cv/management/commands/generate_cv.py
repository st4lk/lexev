import os
import pickle
import markdown
from django.core.management.base import BaseCommand
from django.conf import settings
from linkedin import linkedin
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
import linkedin_settings
from pages.models import Page


path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ROOT = path(ROOT, 'templates')
CACHE_FILE = '.linkedin_cache'

# Jinja settings
# for all options see http://jinja.pocoo.org/docs/api/#jinja2.Environment
jinja_settings = {
    'autoescape': False,
}
jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_ROOT),
            **jinja_settings)


def get_linkedin_cache():
    profile = None
    try:
        with open(CACHE_FILE, 'rb') as pkl_file:
            profile = pickle.load(pkl_file)
    except IOError:
        pass
    return profile


def set_linkedin_cache(profile):
    with open(CACHE_FILE, 'wb') as output:
        pickle.dump(profile, output)


def get_linkedin_profile(use_cache=False):
    profile = None
    if use_cache:
        profile = get_linkedin_cache()
    if profile is None:

        authentication = linkedin.LinkedInDeveloperAuthentication(
            linkedin_settings.CONSUMER_KEY, linkedin_settings.CONSUMER_SECRET,
            linkedin_settings.USER_TOKEN, linkedin_settings.USER_SECRET,
            linkedin_settings.RETURN_URL, linkedin.PERMISSIONS.enums.values())

        # Pass it in to the app...

        application = linkedin.LinkedInApplication(authentication)

        # Use the app....

        # profile = application.get_profile()
        # http://developers.linkedin.com/documents/profile-fields
        profile = application.get_profile(selectors=[

            'associations',
            'certifications',
            'courses',
            'date-of-birth',
            # 'distance',
            'educations',
            'email-address',
            'first-name',
            # 'following',
            'formatted-name',
            'headline',
            'honors-awards',
            # 'id',
            'industry',
            'interests',
            # 'job-bookmarks',
            'languages',
            'last-name',
            'location',
            'maiden-name',
            'member-url-resources',
            # 'mfeed-rss-url',
            # 'num-connections',
            'num-recommenders',
            'patents',
            'picture-url',
            'positions',
            'proposal-comments',
            'publications',
            'public-profile-url',
            'recommendations-received',
            # 'related-profile-views',
            'skills',
            'specialties',
            # 'suggestions',
            'summary',
            'three-current-positions',
            'three-past-positions',
            'volunteer',

            "phone-numbers",
            "bound-account-types",
            "im-accounts",
            "main-address",
            "twitter-accounts",
            "primary-twitter-account",

            # "connections",
            # "group-memberships",

            # "network",

        ])
        set_linkedin_cache(profile)
    return profile


def add_info_to_profile(profile):
    for position in profile['positions']['values']:
        if position['company']['name'] == 'Freelance':
            position['additional'] = """Projects, i've been involved to:

- fursk.ru
- dropnroll.tv
- courses.by
- wirelayer.net
- 3dplitka.ru


Open-source contributing:

- django-oscar
"""
    return profile


def generate_html(md_content):
    html_content = jinja_env.get_template('includes/header.html').render({}).encode('utf8')
    html_content += markdown.markdown(md_content, extensions=['headerid'])
    return html_content


def generate_pdf(html_content, path_out):
    pisa.showLogging()
    with open(path_out, 'wb') as fw:
        pisaStatus = pisa.CreatePDF(html_content, dest=fw)
    return pisaStatus.err


def save_md(md_en, html_en, md_ru, html_ru):
    cv = Page.objects.get(title__name="cv")
    cv.markdown_content_en = md_en
    cv.content_en = html_en
    cv.markdown_content_ru = md_ru
    cv.content_ru = html_ru
    cv.save()


def generate_cv():
    profile = get_linkedin_profile(linkedin_settings.STORE_LINKEDIN_CACHE)
    profile = add_info_to_profile(profile)

    context = {"linkedin": profile, }
    md_en = jinja_env.get_template('cv.md').render(context).encode('utf8')
    html_en = generate_html(md_en)
    save_md(md_en, html_en, md_en, html_en)
    pdf_en = os.path.join(settings.MEDIA_ROOT, 'cv/en/cv.pdf')
    generate_pdf(html_en, pdf_en)
    pdf_ru = os.path.join(settings.MEDIA_ROOT, 'cv/ru/cv.pdf')
    generate_pdf(html_en, pdf_ru)


class Command(BaseCommand):
    args = '<None>'
    help = 'generage cv'

    def handle(self, **options):
        generate_cv()
