from typing import List, Tuple

import ast
from airport_scraper import airport_scraper
from shapely.geometry import Point, Polygon
import geopandas as gpd
# import matplotlib.pyplot as plt

VALUE_ERROR_INPUT1 = "The first line of input must be a valid list of strings python structure"
VALUE_ERROR_INPUT2 = "The second line of input must be a valid list of list of floats structure, with two floats per list"

# read two lines of input from stdin and return the data structures they represent
# the first line represents a list of strings for airport codes
# the second line represents a list of list of floats for points in the polygon
def parse_input() -> Tuple[List[str],  List[List[float]]]:
  # read first line list of strings for airport codes
  try:
    airport_codes = ast.literal_eval(input())
  except Exception as e:
    raise ValueError(VALUE_ERROR_INPUT1)

  # validate type
  if not isinstance(airport_codes, list):
    raise ValueError(VALUE_ERROR_INPUT1)
  for airport_code in airport_codes:
    if not isinstance(airport_code, str):
      raise ValueError(VALUE_ERROR_INPUT1)

  # read second line of list of list of floats for points in the polygon
  try:
    polygon = ast.literal_eval(input())
  except Exception as e:
    raise ValueError(VALUE_ERROR_INPUT2)

  # validate type
  if not isinstance(polygon, list):
    raise ValueError(VALUE_ERROR_INPUT2)
  for point_pair in polygon:
    if not isinstance(point_pair, list) or len(point_pair) != 2:
      raise ValueError(VALUE_ERROR_INPUT2)
    for point in point_pair:
        if not isinstance(point, float):
          raise ValueError(VALUE_ERROR_INPUT2)

  return (airport_codes, polygon)

# given a list of coordinate locations and a list of coordinates for a polygon
# return a parallel list of bools representing if each coordinate location touches or is
# within polygon formed from the convex hull of the points
def contains(locations: List[List[float]], polygon: List[List[float]]) -> List[bool]:

  # create a geoseries with a single polygon
  # longitude should be the x coordinate of the point
  polygon_gs = gpd.GeoSeries([Polygon([Point(coordinate[1],coordinate[0]) for coordinate in polygon])])
  polygon_gs = polygon_gs.convex_hull
  
  ### plotting for debugging/understanding ###
  # polygon_gs.plot(ax=plt.gca(), color='red', markersize=10)
  # for location in locations:
  #   plt.scatter(location[1], location[0], color='blue', marker='o', s=50) 
  # plt.show()
  
  # check if each airport is within the polygon  
  findings = []
  for location in locations:
    point = Point(location[1], location[0]) # longitude should be the x coordinate of the point
    findings.append(bool(polygon_gs.contains(point)[0]) or bool(polygon_gs.touches(point)[0]))
  return findings

# given stdin input for airport identifiers and polygon points, returns a list
# identifying if each airport is in the convex hull of polygon points
if __name__ == "__main__":
  # parse input
  (airport_codes, polygon) = parse_input()

  # find locations of airport codes by scraping
  scraper = airport_scraper()
  locations = [scraper.get_coordinates(airport_code) for airport_code in airport_codes]

  # check if each airport is contained in the polygon
  findings = contains(locations, polygon)

  # print output
  print(findings)