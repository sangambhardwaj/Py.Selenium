from selenium import webdriver

# Create Session
# Send the Commands- navigate to a url
#  if you are useing selenium <4 , We use to set the driver path
# if you are using the selenium >4 , Driver path is note needed ,the will handle automatically

browser = webdriver.Chrome()
browser.get("https://app.vwo.com")
