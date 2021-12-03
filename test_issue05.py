import pytest
from what_is_year_now import what_is_year
from unittest.mock import patch


def test_error():
    with patch('what_is_year_now.json.load') as mock:
        mock.json.load = [{
            '$id': '1',
            'currentDateTime': '2021-12-02T20:05Z',
            'utcOffset': '00:00:00',
            'isDayLightSavingsTime': False,
            'dayOfTheWeek': 'Thursday',
            'timeZoneName': 'UTC',
            'currentFileTime': 132829491305006829,
            'ordinalDate': '2021-336',
            'serviceResponse': None
        }]
        with pytest.raises(ValueError):
            what_is_year()
# python -m pytest --cov . --cov-report html
