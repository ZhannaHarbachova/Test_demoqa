import time

from pages.elements_page import TextBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, browser):
            text_box_page = TextBoxPage(browser, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            time.sleep(4)
            output_name, output_email, output_current_address, output_permanent_address =\
                text_box_page.check_filled_form()
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_current_address, "The current address does not match"
            assert permanent_address == output_permanent_address, "The permanent address does not match"

    class TestCheckbox:
        def test_check_box(self, browser):
            check_box_page = CheckBoxPage(browser, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'Checkboxes have not been selected'
