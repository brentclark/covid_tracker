import pytest
import datetime
from covid19tracker import change_case


@pytest.mark.test_change_case
def test_change_case():
    """
    Below is the rawdata when you query the global status of
    the pandemic

    rawdata = {
        "updated":1589644684727,
        "cases":4670224,
        "todayCases":48810,
        "deaths":310003,
        "todayDeaths":1849,
        "recovered":1780118,
        "active":2580103,
        "critical":44984,
        "casesPerOneMillion":599,
        "deathsPerOneMillion":39.8,
        "tests":57501547,
        "testsPerOneMillion":7421.34,
        "population":7748138803,
        "activePerOneMillion":333,
        "recoveredPerOneMillion":229.75,
        "criticalPerOneMillion":5.81,
        "affectedCountries":215
    }
    """

    # just randomly chose a few keys
    assert 'Cases' == change_case('cases')
    assert 'Deaths_Per_One_Million' == change_case('deathsPerOneMillion')
    assert 'Tests' == change_case('tests')
    assert 'Tests_Per_One_Million' == change_case('testsPerOneMillion')
    assert 'Population' == change_case('population')

    assert 'recovered' != change_case('recovered')
    assert 'activePerOneMillion' != change_case('activePerOneMillion')
