import selenium.webdriver as d
from src.page_obj import GoogleSearchPage
from time import sleep


if __name__ == '__main__':
    # pass
    with GoogleSearchPage('s'):
        pass
    # driver = d.Chrome()
    #
    # driver.get('https://www.phptravels.net/login')
    # page = GoogleSearchPage(driver)
    #
    # # print(page.sign_in.text)
    # # print(page.sign_in.obj.text)
    #
    # print(page.name.value)
    # page.name.value = 'hello'
    # print(page.name.value)
    #
    # sleep(10)

    # with GoogleSearchPage(driver) as page:
    #     print('hi')


    # driver.close()
    # driver.quit()
