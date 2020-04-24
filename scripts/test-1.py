from selenium import webdriver

from bazel_tools.tools.python.runfiles import runfiles

r = runfiles.Create()

driver = webdriver.Chrome(executable_path=r.Rlocation("test_suite/drivers/chromedriver.exe"))

driver.get("https://codoid.com")

driver.quit()

#print(r.Rlocation("foo_ws/drivers/chromedriver.exe"))

