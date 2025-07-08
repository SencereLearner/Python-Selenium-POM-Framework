import pytest


@pytest.mark.extended
def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title_is('Sale')