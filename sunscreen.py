import os

import arrow
from colorama import Fore, Back, Style
import click
import requests


SUN_FACE = "\U0001f31e"
BAR_CHART = "\U0001f4ca"


class UVForecast:
    def __init__(self, epa_resp):
        self.today = arrow.utcnow()
        self.readings = self._interpret(epa_resp)

    def _interpret(self, epa_data):
        today = []
        for hour in epa_data:
            # TODO: map zipcode to timezone for storage later
            normalized_datetime = arrow.get(hour["DATE_TIME"], "MMM/DD/YYYY HH A")
            order = hour["ORDER"]
            uv = hour["UV_VALUE"]
            today.append(
                {"order": order, "datetime": normalized_datetime, "uv_value": uv}
            )
        return today

    def max(self):
        return max(a["uv_value"] for a in self.readings)


def get_local_zip():
    zipcode = click.prompt("Enter US zipcode", default=78701, type=int)
    # TODO: ensure zipcode is legit
    return zipcode


def get_todays_uv_data(zipcode):
    click.echo("Retrieving today's UV data...")
    epa_url = (
        "https://iaspub.epa.gov/enviro/efservice/"
        f"getEnvirofactsUVHOURLY/ZIP/{zipcode}/json"
    )
    # TODO: handle network problems
    req = requests.get(epa_url)
    uv = UVForecast(req.json())
    return uv


def graph_uv_data(uv_forecast):
    # print the date
    click.echo(uv_forecast.today.format("MMM DD, YYYY HH:MM"))

    # print legend
    print("Time ", end="")
    max_uv = uv_forecast.max()
    LEVEL = " "
    for val in range(1, max_uv + 1):
        if val < 3:
            print(Back.GREEN + LEVEL, end="")
        elif val < 6:
            print(Back.YELLOW + LEVEL, end="")
        elif val < 8:
            print(Back.CYAN + LEVEL, end="")
        elif val < 10:
            print(Back.RED + LEVEL, end="")
        else:
            print(Back.MAGENTA + LEVEL, end="")

    print(Style.RESET_ALL)

    # TODO: use the colors above as background for the chart below

    # print data
    for hour in uv_forecast.readings:
        uv = hour["uv_value"]
        print(hour["datetime"].format("HHmm"), end=" ")
        print("*" * uv)


@click.command()
def main():
    """example"""
    click.echo(f"Welcome to sunscreen! {SUN_FACE} {BAR_CHART}")
    # TODO: first run dialog, ask to save zip code for future use
    # TODO: add option to specify a new zip code as arg
    zipcode = get_local_zip()
    uv_data = get_todays_uv_data(zipcode)
    graph_uv_data(uv_data)
