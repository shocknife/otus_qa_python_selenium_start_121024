from page_objects.main_page import MainPage


def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.open()
    main_page.verify_title(main_page.TITLE)
    main_page.verify_quantity_cards(4)
    main_page.verify_quantity_banner(2)
    main_page.check_privacy_policy()
