import pytest
import datetime
from covid19tracker import convertdate

@pytest.mark.convertdate
def test_convertdate():
  date = 1589635082564
  result = convertdate(date)
  expected = datetime.datetime.utcfromtimestamp(date/1000).strftime('%Y-%m-%d %H:%M:%S')
  assert expected == result
