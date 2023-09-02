
from selene import browser, have, be, by
import allure

def test_github():
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    with allure.step('Поиск репозитория'):
        browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
        browser.element('#query-builder-test').type("eroshenkoam/allure-example").press_enter()
    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step('Открываем Таб Issues'):
        browser.element("#issues-tab").click()
    with allure.step('Проверяем наличие Issues #81'):
        browser.element(by.partial_text("#81")).should(be.visible)

    with allure.step('Проверяем название Issue в репозитории'):
        browser.element('#repo-content-turbo-frame').should(have.text('issue_to_test_allure_report'))