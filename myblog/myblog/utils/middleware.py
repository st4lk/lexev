from django.http import HttpResponsePermanentRedirect


class RuRedirectMiddleware(object):
    """ Needs only for redirect from /ru/{path} to {path}, because some urls
    were indexed by search engines as /ru/{path}."""

    def process_request(self, request):
        if request.path_info.startswith("/ru/")\
          and not request.path_info.startswith("/ru/feeds"):
            return HttpResponsePermanentRedirect(request.path_info[3:])
