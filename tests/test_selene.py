from selene import browser, have, be, by


def test_github():
    browser.open('/')

    browser.element('[data-target="qbsearch-input.inputButtonText"]').click()
    browser.element('#query-builder-test').type("eroshenkoam/allure-example").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()
    browser.element("#issues-tab").click()
    browser.element(by.partial_text("#81")).should(be.visible)

    browser.element('#repo-content-turbo-frame').should(have.text('issue_to_test_allure_report'))
