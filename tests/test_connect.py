import mock
import pytest
from pytest_mock import mocker
from covid19tracker import connect

url = 'https://corona.lmao.ninja/v2/countries/' + 'za'


@pytest.mark.connect
def test_connect():
    """ should return a dictionary with the following keys """
    data = connect(url)
    print(f"Testing {url}")

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


@pytest.mark.connect_should_throw_exception
def test_that_connect_should_throw_exception():
    with pytest.raises(Exception):
        connect()
