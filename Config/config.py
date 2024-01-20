import socket
import psutil


class TestData:

    SELENIUM_GRID_CHROME_URL = "http://172.20.0.21:4444/wd/hub"
    SELENIUM_GRID_FIREFOX_URL = "http://172.20.0.22:4444/wd/hub"
    BASE_URL = "http://172.20.0.20:5000/"
    USER_NAME = "oscp.prep2021@gmail.com"  # <<admin>> # for regular user: "test1@test.com"
    PASSWORD = "YNG>iarqC5wGE~>"  # same pass for admin and user unless you register a new one

    PAGE_TITLE = "Obaid's Blog"
    COUNT_OF_HAMBURGER_BUTTONS = [4, 5]
    CREATE_NEW_POST_HEADER = "New Post"



