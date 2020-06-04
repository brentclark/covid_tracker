#!/usr/bin/python3
"""
Author : Brent Clark <brentgclark@gmail.com>
Purpose: This is something I wrote to keep track of the global pandemic.
         The work is very much inspired by the project of Waren Gonzaga.
         Do be sure to check out his Github / project.
         i.e. https://github.com/trackercli/covid19-tracker-cli

MIT License
Copyright (c) <2020> <Brent Clark>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

API used: https://corona.lmao.ninja/docs/#/Countries%20/%20Continents
"""
import argparse
import datetime
import requests
from collections import OrderedDict

from rich.console import Console
from rich.table import Table

def main():
    """ main function to satisfy pylint """

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--country', action='store', help="Per Country stats")
    parser.add_argument('-cs', '--countrys', action='store_true',
                        help="Get All Countries Totals for Actual and Yesterday Data",
                        default=False)
    parser.add_argument('-sb', '--sortby', choices=['deaths','cases', 'recovered', 'active', 'critical', 'population' ], default='deaths', help='sort by for country sort')
    parser.add_argument('-y', '--yesterday', action='store_true',
                        default=False,
                        help="Yesterdays Country stats")
    parser.add_argument('-a', '--all', action='store_true',
                        help="Global stats: cases, deaths, recovered etc.")
    args = parser.parse_args()

    url = "https://corona.lmao.ninja/v2/"

    if args.all:
        url = url + 'all'
        allcountries(url)
    elif args.country:

        url = url + 'countries/' + args.country
        whatdays_data = 'Todays'

        if args.yesterday:
            url = url + '?yesterday=true'
            whatdays_data = 'Yesterdays'

        percountry(url, whatdays_data)
    elif args.countrys:
        url = url + 'countries/'
        countries(url, args.sortby)
    else:
        parser.print_help()

def connect(url):
    """ http request to corona API """

    try:
        with requests.get(url, timeout=3) as requestapi:
            if requestapi.status_code == 200:
                return requestapi.json()
        return False
    except requests.exceptions.RequestException as requestapiexception:
        raise SystemExit(requestapiexception)

def convertdate(date):
    """ divide timestamp by 1000 to convert from milliseconds to seconds """

    return datetime.datetime.utcfromtimestamp(date/1000).strftime('%Y-%m-%d %H:%M:%S')

def change_case(globalkey):
    """ convert camelString """

    return ''.join(['_'+i.lower() if i.isupper() else i for i in globalkey]).lstrip('_').title()

def allcountries(url):
    """ query global status """

    data = connect(url)
    table = Table(show_header=True)
    table.add_column("Global Stats", header_style="white")
    table.add_column("")

    for key, value in data.items():
        if key == 'updated':
            value = convertdate(data['updated'])
            table.add_row(key.title(), value)
            continue

        table.add_row(
            change_case(key),
            str("{:,}".format(value))
        )

    CONSOLE.print(table)

def percountry(url, whatdays_data):
    """ per country status """

    data = connect(url)
    updated = convertdate(data['updated'])

    status = f"Country: {data['country']} ([dim white]Last updated: {updated}[/dim white] (UTC))"
    CONSOLE.print(status, style="red")

    table = Table(show_header=True)
    table.add_column("Cases", header_style="magenta")
    table.add_column("Deaths", header_style="red")
    table.add_column("Recovered", header_style="green")
    table.add_column("Active", header_style="blue")
    table.add_column("Critical", header_style="cyan")

    table.add_row(
        str("{:,}".format(data['cases'])),
        str("{:,}".format(data['deaths'])),
        str("{:,}".format(data['recovered'])),
        str("{:,}".format(data['active'])),
        str("{:,}".format(data['critical']))
    )
    CONSOLE.print(table)

    CONSOLE.print(f'{whatdays_data} Cases:')
    table = Table(show_header=True)
    table.add_column(f"{whatdays_data} Cases", header_style="magenta")
    table.add_column(f"{whatdays_data} Deaths", header_style="red")
    table.add_column("Deaths Per Million", header_style="green")
    table.add_column("Total Tests", header_style="blue")
    table.add_column("Tests Per OneMillion", header_style="cyan")
    table.add_row(
        str("{:,}".format(data['todayCases'])),
        str("{:,}".format(data['todayDeaths'])),
        str("{:,}".format(data['deathsPerOneMillion'])),
        str("{:,}".format(data['tests'])),
        str("{:,}".format(data['testsPerOneMillion']))
    )
    CONSOLE.print(table)

def countries(url, sortby):
    """ country rankings """
    d = connect(url)

    a = {i['country']:i[sortby] for i in d}
    data = OrderedDict(sorted(a.items(), key=lambda t: t[1]))

    result = {}
    for k, v in data.items():
        for x in d:
            if x['country'] == k:
                result[k] = x

    table = Table(show_header=True)
    table.add_column("Country", header_style="yellow")
    table.add_column("Deaths", header_style="red")
    table.add_column("Cases", header_style="magenta")
    table.add_column("Recovered", header_style="green")
    table.add_column("Active", header_style="blue")
    table.add_column("Critical", header_style="cyan")
    table.add_column("Population", header_style="green")

    for country in data.keys():
        table.add_row(
            f"{country}",
            str("[red]{:,}[/red]".format(result[country]['deaths'])) if sortby == 'deaths' else str("{:,}".format(result[country]['deaths'])) ,
            str("[magenta]{:,}[/magenta]".format(result[country]['cases'])) if sortby == 'cases' else str("{:,}".format(result[country]['cases'])),
            str("[green]{:,}[/green]".format(result[country]['recovered'])) if sortby == 'recovered' else str("{:,}".format(result[country]['recovered'])),
            str("[blue]{:,}[/blue]".format(result[country]['active'])) if sortby == 'active' else str("{:,}".format(result[country]['active'])),
            str("[cyan]{:,}[/cyan]".format(result[country]['critical']))if sortby == 'critical' else str("{:,}".format(result[country]['critical'])),
            str("[green]{:,}[/green]".format(result[country]['population'])) if sortby == 'population' else str("{:,}".format(result[country]['population']))
        )

    CONSOLE.print(table)
    print(f"Highlighted column which is sorted by. i.e. {sortby}")

if __name__ == '__main__':

    CONSOLE = Console()
    main()
