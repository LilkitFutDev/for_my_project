import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_for_button(browser):
    browser.get(link)
    find_button = browser.find_element_by_xpath("//button[@value = 'Добавить в корзину']")
    find_button_text = find_button.text
    assert find_button_text == "Добавить в корзину"
