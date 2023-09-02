from selene import browser, have, be, by
import allure


def test_decarator():
    open_page()
    serch_repositoty("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    opet_tab()
    should_number('#81')
    should_text('issue_to_test_allure_report')






@allure.step('Открываем главную страницу')
def open_page():
    browser.open('/')

@allure.step('Поиск репозитория {repo}')
def serch_repositoty(repo):
    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('#query-builder-test').type(repo).press_enter()

@allure.step('Переходим по ссылке репозитория')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step('Открываем Таб Issues')
def opet_tab():
    browser.element("#issues-tab").click()

@allure.step('Проверяем наличие Issues #81')
def should_number(number):
    browser.element(by.partial_text(number)).should(be.visible)

@allure.step('Проверяем название Issue в репозитории')
def should_text(Issue):
    browser.element('#repo-content-turbo-frame').should(have.text(Issue))