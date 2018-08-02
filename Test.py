import time;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


def Customer_TC():

    names = []
    browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
    menu = browser.find_element_by_name('userSelect')
    time.sleep(2)
    options = [x for x in menu.find_elements_by_tag_name("option")]

    for element in options:
        names.append(element.text)

    names.remove(names[0])
    print(names)

    for name in names:
        time.sleep(2)

        t = '''//*[contains(text(), '{}')]'''.format(name)
        browser.find_element_by_xpath(t).click()

        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/form/button').click()

        deposit_click = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/button[2]')
        deposit_click.click()
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/div/form/div/input').send_keys(1000)
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/div/form/button').click()

        time.sleep(2)

        withdrawl_click = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/button[3]')
        withdrawl_click.click()
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/div/form/div/input').send_keys(500)
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/div/form/button').click()

        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div/div/div[1]/button[2]').click()  # logout


def Manager_TC():

    sample_First_name = ['Firstname1','Firstname2','Firstname3']
    sample_Last_name = ['Lastname1','Lastname2','Lastname3']
    sample_Pincode = ['Pincode1','Pincode2','Pincode3']
    sample = ['1','2','3']

    home = browser.find_element_by_xpath('/html/body/div/div/div[1]/button[1]')
    home.click()

    time.sleep(2)
    manager_login = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/button')
    manager_login.click()

    add_customer = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/button[1]')
    add_customer.click()
    i = 0
    for item in sample:
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/form/div[1]/input').send_keys(sample_First_name[i])
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/form/div[2]/input').send_keys(sample_Last_name[i])
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/form/div[3]/input').send_keys(sample_Pincode[i])
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/form/button').click()
        time.sleep(1)
        WebDriverWait(browser,3)
        alert = browser.switch_to.alert
        alert.accept()
        i+=1

    customers_click = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/button[3]')
    customers_click.click()

    j=0
    for item in sample:
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input').clear()
        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/form/div/div/input').send_keys(sample_First_name[j])
        time.sleep(1)

        browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[5]/button').click()
        j+=1

    home.click()


browser = webdriver.Chrome(r"C:\Python27\chromedriver.exe")
browser.get("http://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
browser.implicitly_wait(3)


Manager_TC()
Customer_TC()