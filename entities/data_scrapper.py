from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeServices
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options


class DataScrapper:
    def __init__(self) -> None:
        self.__download_path = r'./data/replays/'
        # Selenium Options
        self.__options = Options()
        self.__options.headless = True
        self.__options.use_chromium = True
        self.__options.add_experimental_option('prefs', {
            "download.default_directory": self.__download_path
        })
        self.__options.add_argument('--log-level=3')
        self.driver = webdriver.Edge(service=EdgeServices(
            EdgeChromiumDriverManager().install()), options=self.__options)

    def quit(self):
        self.driver.quit()
