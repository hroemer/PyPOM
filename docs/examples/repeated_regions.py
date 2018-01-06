from pypom import Page, Region
from selenium.webdriver.common.by import By


class Results(Page):
    _result_locator = (By.CLASS_NAME, 'result')

    @property
    def results(self):
        results_element = self.find_element(*self._result_locator)
        items = results_element.find_elements(*self.Result._root_locator)
        return [self.Result(self, el) for el in items]

    class Result(Region):
        _root_locator = (By.CLASS_NAME, 'item')

        @property
        def name(self):
            return self.root.text
