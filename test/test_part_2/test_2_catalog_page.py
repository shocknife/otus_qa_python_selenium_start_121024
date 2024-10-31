from page_objects.catalog_page import CatalogPage


def test_page_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open()
    catalog_page.select_tablets()
    catalog_page.verify_title(catalog_page.TITLE)
    catalog_page.verify_catalog_url()
    catalog_page.check_elements()
