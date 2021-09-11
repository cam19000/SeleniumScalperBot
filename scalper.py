#MUST HAVE PYTHON, SELENIUM, AND CHROMEDRIVER
import time
import datetime
from selenium import webdriver
#Creates new browser object using chromedriver
browser = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

# Pulls 3080 ti webpage (Can use any best buy GPU that you want)
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
buyButton = False

#Login to Bestbuy before proceeding.
prompt = input("Continue?\n")



while not buyButton:

    try:
        #Button not open if this = true
        addToCartBtn = addButton = browser.find_element_by_class_name("c-button-disabled")

        #Button not ready yet, alert user and restart script
        print("Still no stock")

        #Refresh page after delay
        time.sleep(3)
        browser.refresh()

    except:
        #Finds the add to cart button ("button Primary is only used on the checkout button in this case)
        addToCartBtn = addButton = browser.find_element_by_class_name("c-button-primary")
        print("IN STOCK!")

        #Click the button
        addToCartBtn.click()
        print("button clicked")
        addToCartBtn.click()
        buyButton = True

#Go to cart
browser.get("https://www.bestbuy.com/cart")

time.sleep(6)

#Click the checkout button
checkoutBtn = browser.find_element_by_class_name("btn-primary")
checkoutBtn.click()

time.sleep(7)

#All other information is already filled out if you are logged into a valid account with payment info, only thing left is the cvv
cvvField = browser.find_element_by_id("cvv")

cvvField.send_keys("YOUR CVV")
print("ENTERED CVV")

time.sleep(3)

finalCheckout = browser.find_element_by_class_name("btn-primary")
finalCheckout.click()

#This script assumes you already have an account with a card setup, that way the bot won't need to enter anything other than the CVV. 
#This script also assumes that there is no captcha set in place after you complete the order