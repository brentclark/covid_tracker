# covid tracker

covid19tracker.py is a simple tool help get the stats for COVID19.
Data shown, ranges from global data overviews to country specific mobility data.

```bash
git clone https://github.com/brentclark/covid_tracker
pip3 install -r requirements.txt
```

## Usage

```python
$ python3 covid19tracker.py -c za
Country: South Africa (Last updated: 2020-05-19 10:33:25 (UTC))
┏━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ Cases  ┃ Deaths ┃ Recovered ┃ Active ┃ Critical ┃
┡━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ 16,433 │ 286    │ 7,298     │ 8,849  │ 119      │
└────────┴────────┴───────────┴────────┴──────────┘
Todays Cases:
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Todays Cases ┃ Todays Deaths ┃ Deaths Per Million ┃ Total Tests ┃ Tests Per OneMillion ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ 0            │ 0             │ 5                  │ 475,071     │ 8,022                │
└──────────────┴───────────────┴────────────────────┴─────────────┴──────────────────────┘
```
## Contributing
Bug reports and pull requests are welcome on GitHub at https://github.com/brentclark/covid_tracker

## License
[MIT](https://choosealicense.com/licenses/mit/)

