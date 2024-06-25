from Products.Five.browser import BrowserView


class rssfeedView(BrowserView):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        req = self.request
        return self.index()
