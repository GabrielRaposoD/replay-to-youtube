from entities.match_data import MatchData
from entities.data_scrapper import DataScrapper
from utils.data import load_match_data
from utils.scrapper import Scrapper

scrapper = Scrapper()
scrapper.init_data_folder()
scrapper.start_scrap()
match_data: MatchData = load_match_data()
