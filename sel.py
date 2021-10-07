from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome('$PWD')
#driver = webdriver.Chrome(ChromeDriverManager().install())


#PATH = "$PWD/chromedriver"
#driver = webdriver.Chrome(executable_path = PATH)

#driver.get("https://techwithtim.net")
#driver.quit()
print("Done")