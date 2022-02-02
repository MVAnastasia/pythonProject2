from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print('\nStart browser for test: ')
    browser = webdriver.Chrome(
        executable_path="C:\\Users\\Anastasy MTT\\PycharmProjects\\pythonProject2\\tests_chromedriver\\chromedriver.exe")
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
    print('\nQuit browser ')


links = [  # Список ссылок на тестируемые страницы
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.implicitly_wait(10)

    answer = math.log(int(time.time()))

    textarea = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
    )
        # Передаем ответ из фикстуры answer в поле ввода
    textarea.send_keys(answer)
        # Нажимаем кнопку

    browser.find_element_by_css_selector('button.submit-submission ').click()
# Получаем текст элемента, подтверждающего правильность ответа
    feedback = browser.find_element_by_css_selector('pre.smart-hints__hint').text
# Проверяем ответ
    assert feedback == 'Correct!'
