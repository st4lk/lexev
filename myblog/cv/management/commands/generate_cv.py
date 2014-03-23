# -*- coding: utf-8 -*-
import logging
import os
import pickle
import markdown
from django.core.management.base import BaseCommand
from django.conf import settings
from linkedin import linkedin
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa
from pages.models import Page

l = logging.getLogger('linkedin')


path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ROOT = path(ROOT, 'templates')
if settings.OPENSHIFT_GEAR_NAME is None:
    CACHE_FILE = '.linkedin_cache'
else:
    CACHE_FILE = os.path.join(os.environ['OPENSHIFT_TMP_DIR'], '.linkedin_cache')


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
            settings.LINKEDIN_CONSUMER_KEY, settings.LINKEDIN_CONSUMER_SECRET,
            settings.LINKEDIN_USER_TOKEN, settings.LINKEDIN_USER_SECRET,
            settings.LINKEDIN_RETURN_URL, linkedin.PERMISSIONS.enums.values())

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
        l.debug("Got profile from linkedin: '{0}'".format(profile))
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
    l.info("### Start generating linkedin CV...")
    profile = get_linkedin_profile(settings.LINKEDIN_STORE_CACHE)
    profile = add_info_to_profile(profile)

    context = {"linkedin": profile, }
    md_en = jinja_env.get_template('cv.md').render(context).encode('utf8')
    l.info("Generated mardown english successfully")
    html_en = generate_html(md_en)
    l.info("Generated html english successfully")
    save_md(md_en, html_en, md_en, html_en)
    l.info("Saved english content successfully")
    pdf_en = os.path.join(settings.MEDIA_ROOT, 'cv/en/cv.pdf')
    generate_pdf(html_en, pdf_en)
    l.info("English cv.pdf genrated successfully")
    pdf_ru = os.path.join(settings.MEDIA_ROOT, 'cv/ru/cv.pdf')
    generate_pdf(html_en, pdf_ru)
    l.info("Russian cv.pdf genrated successfully")


class Command(BaseCommand):
    args = '<None>'
    help = 'generage cv'

    def handle(self, **options):
        try:
            generate_cv()
        except:
            l.exception("Something goes wrong in generate_cv")
