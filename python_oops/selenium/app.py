from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the form page hosted locally
    driver.get("http://localhost:8000")  # or the server URL if hosted on a server

    # Wait until the form elements are present
    wait = WebDriverWait(driver, 10)
    name_field = wait.until(EC.presence_of_element_located((By.ID, "name")))
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    message_field = wait.until(EC.presence_of_element_located((By.ID, "message")))

    # Fill out the form fields
    name_field.send_keys("John Doe")
    email_field.send_keys("john.doe@example.com")
    message_field.send_keys("Hello, I would like to inquire about your services.")

    # Submit the form by clicking the submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    print("Form submitted successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
