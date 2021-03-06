from . import Controller
from .session import SessionStorage


class Authentication(object):
    def isAuthenticated(self, request):
        if "owrx-session" in request.cookies:
            session = SessionStorage.getSharedInstance().getSession(request.cookies["owrx-session"].value)
            return session is not None
        return False


class SettingsController(Controller):
    def __init__(self, handler, request, options):
        self.authentication = Authentication()
        super().__init__(handler, request, options)

    def handle_request(self):
        if self.authentication.isAuthenticated(self.request):
            super().handle_request()
        else:
            self.send_redirect("/login")

    def indexAction(self):
        self.send_response("actual content here")
