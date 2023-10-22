from typing import List

import requests
from bs4 import BeautifulSoup

MAIN_PAGE_TITLE = "AirNav: Airport Information"
DECIMAL_DEGREES_CORDINATE_INDEX = 4

class airport_scraper:

  # given an airport code string, scrapes https://www.airnav.com/airport/ to find 
  # and return a list of the latitude and longitude in decimal degrees format
  def get_coordinates(self, airport_code: str) -> List[float]:

    # get webpage for given airport code
    response = requests.get(f"https://www.airnav.com/airport/{airport_code}")
    response.raise_for_status() # while airnav.com always returns 200 status by rerouting, it may not in the future
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # invalid airport codes are rerouted to the main page
    title = soup.title.string
    if title == MAIN_PAGE_TITLE:
      raise ValueError("airport code must be a valid identifier on airnav.com")

    # traverse html content to decimal degrees formated latitude and longitude
    coordinate_td = soup.find("td", text="Lat/Long:\xa0").find_next_sibling("td")
    coordinate_strings = coordinate_td.contents[DECIMAL_DEGREES_CORDINATE_INDEX].strip().split(",")
    return [float(coordinate_strings[0]), float(coordinate_strings[1])]

if __name__ == "__main__":
  scraper = airport_scraper()
  print(scraper.get_coordinates("KBOS"))
  