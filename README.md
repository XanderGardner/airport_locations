# airport_locations


# setup

## requirements
- python3: you can download and install python 3 from the official python website

## dependencies

this project relies on the following python libraries:

- requests: used for making http requests.
```bash
pip install requests
```
- beautifulsoup4: used for parsing html and xml documents.
```bash
pip install beautifulsoup4
```
- geopandas: used for working with geospatial data and shapes (shapely is included)
```bash
pip install geopandas
```
- matplotlib: used for data visualization and plotting for understanding/debugging (optional)
```bash
pip install matplotlib
```

# testing

- run all tests
```
python3 -m unittest discover tests
```

- test by module
```
python3 -m unittest tests/test_airport_scraper.py
python3 -m unittest tests/test_main.py
```

# execution

## input

there are two lines of standard input 
- the first line represents a list of strings for airport codes. the list must represent the structure of a python list. for example: `['I58', 'ANQ', 'OEB']`. the airport identifier codes must be present on https://www.airnav.com/airports or a `ValueError` will be thrown for invalid input
- the second line represents a list of list of floats representing points making up the polygon. the points must be in decimal degree format with latitude being in index 0 and longitude being in index 1. the list of lists must represent the stucture of a python list of lists and all items must be float (*not ints*). for example `[[50.0, -150.0],[50.0,-80.0],[10.0,-80.0],[10.0,-150.0]]`

## execution

execute `python3 main.py` in terminal and enter input

## output

returns a parallel list of bools identifying if each airport is in the polygon formed by the convex hull of polygon points. for example: `[True, True, False]`
