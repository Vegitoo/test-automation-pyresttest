from selenium import webdriver
from selenium.webdriver.common.by import By

def test_create_article():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    
    title_input = driver.find_element(By.ID, "title")
    content_input = driver.find_element(By.ID, "content")
    submit_button = driver.find_element(By.ID, "submit")

    title_input.send_keys("New Article Title")
    content_input.send_keys("New Article Content")
    submit_button.click()

    assert "New Article Title" in driver.page_source

    driver.quit()
