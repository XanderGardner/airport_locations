import unittest
from unittest.mock import patch, Mock
from main import parse_input, contains

class TestMain(unittest.TestCase):

  ### test parse_input function ###

  # test valid input to parse_input function
  def test_parse_input_valid_input(self):
    input_str = "['JFK', 'LHR']\n[[42.0, -71.0], [51.5, -0.5]]\n"
    with unittest.mock.patch("builtins.input", side_effect=input_str.split("\n")):
      airport_codes, polygon = parse_input()
    self.assertEqual(airport_codes, ["JFK", "LHR"])
    self.assertEqual(polygon, [[42.0, -71.0], [51.5, -0.5]])

  # test that invalid input with ints insteads of floats to parse_input raises ValueError
  def test_parse_input_invalid_input_int(self):
    input_str = "['JFK', 'LHR']\n[[42, -71], [51.5, -0.5]]\n"
    with unittest.mock.patch("builtins.input", side_effect=input_str.split('\n')):
      with self.assertRaises(ValueError):
        parse_input()

  # test that invalid input with too few coordinates to parse_input raises ValueError
  def test_parse_input_invalid_input_int(self):
    input_str = "['JFK', 'LHR']\n[[42.0], [51.5, -0.5]]\n"
    with unittest.mock.patch("builtins.input", side_effect=input_str.split('\n')):
      with self.assertRaises(ValueError):
        parse_input()

  # test that invalid input with unstructured list to parse_input raises ValueError
  def test_parse_input_invalid_input_int(self):
    input_str = "'JFK' 'LHR'\n42.0, 5.0, 51.5, -0.5\n"
    with unittest.mock.patch("builtins.input", side_effect=input_str.split('\n')):
      with self.assertRaises(ValueError):
        parse_input()


  ### test contains function ###

  # test that locations are found to be within polygon
  def test_contains(self):
    locations = [[1.0, 1.0]]
    polygon = [[0.0,0.0],[0.0,2.0],[2.0,2.0],[2.0,0.0]]
    findings = contains(locations, polygon)
    self.assertEqual(findings, [True])

  # test that location on the edge of the polygon are included as within the polygon
  def test_contains_touches_edge(self):
    locations = [[2.0, 2.0]]
    polygon = [[0.0,0.0],[0.0,2.0],[2.0,2.0],[2.0,0.0]]
    findings = contains(locations, polygon)
    self.assertEqual(findings, [True])

  # test that location outside of the polygon is not included as within the polygon
  def test_contains_invalid(self):
    locations = [[3.0, 3.0]]
    polygon = [[0.0,0.0],[0.0,2.0],[2.0,2.0],[2.0,0.0]]
    findings = contains(locations, polygon)
    self.assertEqual(findings, [False])

if __name__ == '__main__':
  unittest.main()
