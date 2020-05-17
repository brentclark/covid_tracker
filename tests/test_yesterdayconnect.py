import mock
import pytest
from pytest_mock import mocker
from covid19tracker import connect

yesterday_url = 'https://corona.lmao.ninja/v2/countries/za?yesterday=true'


@pytest.mark.yesterdayconnect
def test_yesterdayconnect():
    """ should return a dictionary with the following keys, based
        on yesterdays flagged as true
    """
    data = connect(yesterday_url)
    print(f"Testing {yesterday_url}")

    assert 'active' in data
    assert 'cases' in data
    assert 'country' in data
    assert 'critical' in data
    assert 'deaths' in data
    assert 'deathsPerOneMillion' in data
    assert 'recovered' in data
    assert 'tests' in data
    assert 'testsPerOneMillion' in data
    assert 'todayCases' in data
    assert 'todayDeaths' in data
