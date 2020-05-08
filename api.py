"Test for Api"
import unittest
import requests

class TestMathFunction(unittest.TestCase):
    "Class for testing api"
    def test_for_api(self):
        "Testing for the api"
        url = "https://corona-virus-stats.herokuapp.com/api/v1/cases" \
              "/countries-search?search=albania"
        test = requests.get(url)
        status_code = test.status_code
        expected = 200
        data = test.json()

        status = data["status"]
        status_message = "success"

        self.assertEqual(status_code, expected)
        self.assertEqual(status, status_message)


if __name__ == '__main__':
    unittest.main()