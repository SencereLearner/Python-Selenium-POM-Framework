from selenium.webdriver.common.by import By


email_field_loc = (By.ID, 'email')
password_field_loc = (By.ID, 'pass')
button_loc = (By.ID, 'send2')
error_locator = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')