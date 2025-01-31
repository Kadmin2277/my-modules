class WebViewUrlNotFounded(Exception):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = None


