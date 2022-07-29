import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage


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
            assert input_checkbox == output_result, 'Checkboxes have not been selected'

    class TestRadioButton:

        def test_random_radio_button(self, browser):
            radio_button_page = RadioButtonPage(browser, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            input_radio_button = radio_button_page.click_random_radio_button()
            output_result = radio_button_page.get_output_result()
            assert input_radio_button == output_result

        def test_all_radio_button(self, browser):
            radio_button_page = RadioButtonPage(browser, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()

            assert output_yes == 'Yes', 'Yes have not been selected'
            assert output_impressive == 'Impressive', 'Impressive have not been selected'
            assert output_no == 'No', 'No have not been selected'

    class TestWebTable:

        def test_web_tabel_add_person(self, browser):
            web_table_page = WebTablePage(browser, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)

            assert new_person in table_result

        def test_web_table_search_person(self, browser):
            web_table_page = WebTablePage(browser, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()

            assert key_word in table_result, 'The person was not found in the table'

        def test_web_table_edit_person_info(self, browser):
            web_table_page = WebTablePage(browser, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            time.sleep(5)
            age = web_table_page.edit_person_info()
            row = web_table_page.check_search_person()
            assert age in row, 'The person card has not been changed'

        def test_web_table_delete_person(self, browser):
            web_table_page = WebTablePage(browser, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, browser):
            web_table_page = WebTablePage(browser, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()

            assert count == [5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or' \
                                                      ' has changed incorrectly'

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, browser):
            button_page = ButtonPage(browser, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_button('double')
            right = button_page.click_button('right')
            click = button_page.click_button('click')

            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"
