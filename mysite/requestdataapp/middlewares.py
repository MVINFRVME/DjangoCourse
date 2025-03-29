import datetime

from django.http import HttpRequest, HttpResponseForbidden


def set_user_agent_on_request_middleware(get_response):

    print('initial call')

    def middleware(request: HttpRequest):
        request.user_agent = request.META['HTTP_USER_AGENT']
        response = get_response(request)
        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        response = self.get_response(request)
        self.responses_count += 1
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print('got', self.exceptions_count, 'exceptions so far')



def throttling_middleware(get_response):
    users_request_time = {}

    def middleware(request: HttpRequest):
        if request.META['REMOTE_ADDR'] in users_request_time:
            diff = datetime.datetime.today() - users_request_time[request.META['REMOTE_ADDR']]
            if diff.seconds < 0.1:
                users_request_time[request.META['REMOTE_ADDR']] = datetime.datetime.today()
                return HttpResponseForbidden("Request limit exceeded! Please try again later.")
        else:
            users_request_time[request.META['REMOTE_ADDR']] = datetime.datetime.today()
        response = get_response(request)

        return response

    return middleware






