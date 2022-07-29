from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.ID, 'userName')
    EMAIL = (By.ID, 'userEmail')
    CURRENT_ADDRESS = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS = (By.ID, 'permanentAddress')
    SUBMIT = (By.ID, 'submit')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, '.rct-option.rct-option-expand-all')
    ITEM_LIST = (By.CSS_SELECTOR, '.rct-title')
    CHECKED_ITEMS = (By.CSS_SELECTOR, '.rct-icon.rct-icon-check')
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span.text-success")

    # CHECKBOX_HOME = (By.ID, 'tree-node-home')
    # CHECKBOX_DESKTOP = (By.ID, 'ttree-node-desktop')
    # CHECKBOX_DOCUMENTS = (By.ID, 'tree-node-documents')
    # CHECKBOX_DOWNLOADS = (By.ID, 'tree-node-downloads')
    # CHECKBOX_NOTES = (By.ID, 'tree-node-notes')
    # CHECKBOX_COMMANDS = (By.ID, 'tree-node-commands')
    # CHECKBOX_WORKSPACE = (By.ID, 'tree-node-workspace')
    # CHECKBOX_OFFICE = (By.ID, 'tree-node-office')
    # CHECKBOX_WORD_FILE = (By.ID, 'tree-node-wordFile')
    # CHECKBOX_EXCEL_FILE = (By.ID, 'tree-node-excelFile')
    # CHECKBOX_REACT = (By.ID, 'tree-node-react')
    # CHECKBOX_ANGULAR = (By.ID, 'tree-node-angular')
    # CHECKBOX_VEU = (By.ID, 'tree-node-veu')
    # CHECKBOX_PUBLIC = (By.ID, 'tree-node-public')
    # CHECKBOX_PRIVATE = (By.ID, 'tree-node-private')
    # CHECKBOX_CLASSIFIED = (By.ID, 'tree-node-classified')
    # CHECKBOX_GENERAL = (By.ID, 'tree-node-general')
    #
    # ARROW_HOME = (By.XPATH, "//button/following-sibling::*[./*[@id='tree-node-home']]")
    # ARROW_DESKTOP = (By.XPATH, "//button/following-sibling::*[./*[@id='tree-node-desktop']]")
    # ARROW_DOCUMENTS = (By.XPATH, "//button/following-sibling::*[./*[@id='tree-node-documents']]")
    # ARROW_DOWNLOADS = (By.XPATH, "//button/following-sibling::*[./*[@id='tree-node-downloads']]")
    # ARROW_WORKSPACE = (By.XPATH, "//button/following-sibling::*[./*[@id='tree-node-workspace']]")
    # ARROW_OFFICE = (By.XPATH, "//button/following-sibling::*[./*[@id='tree-node-office']]")


class RadioButtonPageLocators:
    ITEM_LIST = (By.CSS_SELECTOR, ".custom-control-label")
    OUTPUT_RESULT = (By.CSS_SELECTOR, ".text-success")

    YES_RADIOBUTTON = (By.CSS_SELECTOR, "#yesRadio + label")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "#impressiveRadio + label")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "#noRadio + label")


class WebTablePageLocators:
    # add person info
    ADD_BUTTON = (By.ID, "addNewRecordButton")
    SUBMIT_BUTTON = (By.ID, "submit")

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#userForm #firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#userForm #lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#userForm #userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "#userForm #age")
    SALARY_INPUT = (By.CSS_SELECTOR, "#userForm #salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "#userForm #department")

    # search
    SEARCH_INPUT = (By.ID, "searchBox")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#searchBox + div")

    # person table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, ".rt-tr-group")
    DELETE_BUTTON = (By.CSS_SELECTOR, "[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_BUTTON = (By.CSS_SELECTOR, "[title='Edit']")
    NO_DATA = (By.CSS_SELECTOR, ".rt-noData")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "[aria-label='rows per page']")

