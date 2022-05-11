import unittest

from rest_api_functions import single_date_temp_wind, multi_dates_temp_wind, interval_dates_temp_wind


# Now test each of the imported functions
class TestRestApi(unittest.TestCase):
    # Tests for a single date
    def test_single(self):
        self.assertAlmostEqual(single_date_temp_wind('weather_archive_valid.db', '2022-04-06'), 5.8)
        self.assertAlmostEqual(single_date_temp_wind('weather_archive_valid.db', '2022-04-07'), 14.2)
        self.assertAlmostEqual(single_date_temp_wind('weather_archive_valid.db', '2022-04-08'), 1.4)

    # Tests for multi dates
    def test_multi(self):
        self.assertAlmostEqual(
            multi_dates_temp_wind('weather_archive_valid.db', '2022-04-06,2022-04-07,2022-04-08'), 7.1333333333333)
        self.assertAlmostEqual(multi_dates_temp_wind('weather_archive_valid.db', '2022-04-06,2022-04-07'), 10)
        self.assertAlmostEqual(multi_dates_temp_wind('weather_archive_valid.db', '2022-04-08'), 1.4)

    # Tests for interval dates
    def test_interval(self):
        self.assertAlmostEqual(
            interval_dates_temp_wind('weather_archive_valid.db', '2022-04-06', '2022-04-08'), 7.1333333333333)
        self.assertAlmostEqual(interval_dates_temp_wind('weather_archive_valid.db', '2022-04-06', '2022-04-07'), 10)
        self.assertAlmostEqual(interval_dates_temp_wind('weather_archive_valid.db', '2022-04-08', '2022-04-08'), 1.4)
