import pytest
import datetime
from covid19tracker import convertdate


@pytest.mark.convertdate
def test_convertdate():
    dateformat = '%Y-%m-%d %H:%M:%S'
    date = 1589635082564
    result = convertdate(date)
    expected = datetime.datetime.utcfromtimestamp(
                    date/1000).strftime(dateformat)
    assert expected == result
