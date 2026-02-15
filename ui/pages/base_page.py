from selene import browser, have, be

class BasePage:

    def __init__(self):
        self.browser = browser

    def open(self, url):
        self.browser.open(url)
        return self

    def should_have_title(self, text):
        self.browser.should(have.title_containing(text))
        return self
