from webdriver_manager.chrome import ChromeDriverManager

def get_chromedriver_path():
    try:
        # Use webdriver_manager to get the path to the ChromeDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # Add any options you need
        driver = webdriver.Chrome(ChromeDriverManager(version="92.0.4515.107").install(), options=chrome_options)
        driver_path = driver.capabilities['chrome']['chromedriverVersion']
        driver.quit()
        return driver_path
    except Exception as e:
        print(f"Error while getting ChromeDriver path: {str(e)}")
        return None

