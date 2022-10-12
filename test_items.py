import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestLesson3():
  def test_find_button(self, browser):
    browser.get(link)
    time.sleep(30)
    btn = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    assert btn, 'basket button not found'

if __name__ == "__main__":
    pytest.main()  