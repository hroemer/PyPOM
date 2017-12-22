from pypom import Page, Region
from selenium.webdriver.common.by import By


class MainPage(Page):

    @property
    def menu(self):
        return Menu(self)


class Menu(Region):
    _root_locator = (By.ID, 'menu')

    @property
    def entries(self):
        items = self.find_elements(*Entry._root_locator)
        return [Entry(self.page, item) for item in items]


class Entry(Region):
    _root_locator = (By.CLASS_NAME, 'entry')

    @property
    def name(self):
        return self.find_element(*self._root_locator).text
