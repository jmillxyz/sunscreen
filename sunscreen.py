import os

import requests
import click


SUNGLASSES_EMOJI = "\U0001f60e"
SUN_FACE = "\U0001f31e"
BAR_CHART = "\U0001f4ca"


def get_local_zip():
    zipcode = input("Enter US zipcode: ")
    # TODO: ensure zipcode is a 5-digit number
    return zipcode


def get_todays_uv_data(zipcode):
    print("grabbing today's UV data")
    epa_url = (
        "https://iaspub.epa.gov/enviro/efservice/"
        f"getEnvirofactsUVHOURLY/ZIP/{zipcode}/json"
    )
    # TODO: handle network problems
    req = requests.get(epa_url)
    return [hour.get("UV_VALUE") for hour in req.json()]


def graph_uv_data(uv_data):
    print("graphing UV data")
    print(uv_data)


@click.command()
def main():
    """example"""
    click.echo(f"Welcome to sunscreen! {SUN_FACE} {BAR_CHART} {SUNGLASSES_EMOJI}")
    # TODO: first run dialog, ask to save zip code for future use
    # TODO: add option to specify a new zip code as arg
    zipcode = get_local_zip()
    uv_data = get_todays_uv_data(zipcode)
    graph_uv_data(uv_data)
