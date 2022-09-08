class MyMixin:

    def get_upper(self, string):
        if isinstance(string, str):
            return string.upper()
        else:
            return string.title.upper()
