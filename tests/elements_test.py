import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, browser):
            text_box_page = TextBoxPage(browser, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            time.sleep(4)
            output_name, output_email, output_current_address, output_permanent_address =\
                text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_current_address)
            print(output_permanent_address)
