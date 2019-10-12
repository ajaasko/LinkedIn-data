from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
import time as t
import getpass


def getData():
    ''' Function to log in to your page and counts total views, comments and likes of your posts'''
    try:
        # element locators for likes, views and comments.
        likes_element = "//span[@class='v-align-middle social-details-social-counts__reactions-count']"
        views_element = "//*[contains(text(), ' of your post in the feed')]"
        comments_element = "//*[contains(text(), ' Comments')]"

        # for counting views, comments and likes.
        count = 0
        total_views = []
        total_comments = []
        total_likes = []

        options = Options()

        # filter out some unnecessary log writngs
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument('--log-level=3')

        # chrome in headless mode
        options.headless = True

        driver = webdriver.Chrome(options=options)	
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.implicitly_wait(10) 

        # opens linkedin page and clicks Sign in button
        driver.get("http://www.linkedin.com")
        t.sleep(2)
        driver.find_element_by_link_text("Sign in").click()
        
        # Verify username and password, if not OK then asks again.
        while True:
            # clear username/password fields
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("password").clear()

            # send username/password and click login button
            userName = input("Username: ")
            passWord = getpass.getpass("Password: ")
            elem = driver.find_element_by_id("username").send_keys(userName)
            elem = driver.find_element_by_id("password").send_keys(passWord)
            elem = driver.find_element_by_class_name("login__form_action_container").click()
            print("Title of the page is: ", driver.title) 
            t.sleep(1)

            # checks if login succeeded or not.
            if (driver.title != "LinkedIn Login, LinkedIn Sign in | LinkedIn" and
                driver.title != "LinkedIn Login, Sign in | LinkedIn"):
                print("Logged in successfully.")
                break
            else:
                print("\nWrong username/password, pls try again.")

        # click Views of your post button on LinkedIn main page   
        element = driver.find_element_by_xpath("//span[contains(.,'Views of your post')]").click()
        t.sleep(5)

        # Scroll down your page.
        last_height = driver.execute_script("return document.body.scrollHeight")
        print("\nScrolling down your page, this might take a while, pls wait...")           
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            t.sleep(2)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
       
        # search views, likes and comments element locators
        for a in driver.find_elements_by_xpath(views_element):
            temp1 = a.text[0:50]
            data1 = temp1.split(" ")
            views_temp = data1[0]
            views = views_temp.replace(',', '')
            total_views.append(int(views))
            count += 1

        for b in driver.find_elements_by_xpath(likes_element):
            temp2 = b.text[0:50]
            data2 = temp2.split(" ")
            likes_temp = data2[0]
            likes = likes_temp.replace(',', '')
            total_likes.append(int(likes))

        for c in driver.find_elements_by_xpath(comments_element):
            temp3 = c.text[0:50]
            data3 = temp3.split(" ")
            comments_temp = data3[0]
            comments = comments_temp.replace(',', '')
            total_comments.append(int(comments))
 
        # prints the results
        print("Posts:", count)
        print("Views:", (sum(total_views)))
        print("Comments:", sum(total_comments))
        print("Likes:", sum(total_likes))
        #driver.close()

    # expection handling
    except NoSuchElementException:
        print("NoSuchElementException, check your code.")
    except WebDriverException:
        print(" ")
    except KeyboardInterrupt:
        print("You cancelled the operation.")


if __name__ == "__main__":
    getData()

