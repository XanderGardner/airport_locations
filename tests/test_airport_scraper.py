import unittest
from unittest.mock import patch, Mock
from airport_scraper import airport_scraper

class TestAirportScraper(unittest.TestCase):
  def setUp(self):
    self.scraper = airport_scraper()

  # test that get_coordinates handles valid airport codes 
  @patch("requests.get")
  def test_get_coordinates_valid(self, mock_requests_get):
    # mock the requests.get function to return a valid html response
    mock_response = Mock()
    mock_response.text = """
    <html>
      <head>
        <title>EWR Title</title>
      </head>
      <body>
        <td>Lat/Long:&nbsp;</td>
        <td>
          42-42-31.5740N 110-56-31.8160W
          <br>
          42-42.526233N 110-56.530267W
          <br>
          42.3629444, -71.0063889
          <br>
          (estimated)
        </td>
      </body>
    </html>
    """
    mock_requests_get.return_value = mock_response

    coordinates = self.scraper.get_coordinates("EWR")
    self.assertEqual(coordinates, [42.3629444, -71.0063889])

  # test that get_coordinates handles invalid airport codes 
  @patch("requests.get")
  def test_get_coordinates_invalid(self, mock_requests_get):
    # mock the requests.get function to return an html response indicating an invalid airport code
    mock_response = Mock()
    mock_response.text = """
    <html>
      <head>
        <title>AirNav: Airport Information</title>
      </head>
    </html>
    """
    mock_requests_get.return_value = mock_response

    with self.assertRaises(ValueError):
      self.scraper.get_coordinates("invalid airport code")

if __name__ == "__main__":
  unittest.main()
