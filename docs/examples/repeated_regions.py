from pypom import Page, Region
from selenium.webdriver.common.by import By


class Results(Page):
    _result_locator = (By.CLASS_NAME, 'result')

    @property
    def results(self):
        results = self.find_elements(*self.Result._name_locator)
        return [self.Result(self, el) for el in results]

    class Result(Region):
        _name_locator = (By.CLASS_NAME, 'name')

        @property
        def name(self):
            return self.root.text
