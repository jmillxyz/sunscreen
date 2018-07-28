import os

import requests
import click


GEO_API_KEY = os.environ["google_geolocation_api_key"]


def check_local_zip():
    geo_url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GEO_API_KEY}"
    req = requests.get(geo_url)
    # getting a 404 here...?
    print(f"your api key is {GEO_API_KEY}")
    print("grabbing lat lng")
    print("grabbing zip code")


def grab_todays_uv_data():
    print("grabbing today's UV data")


def graph_uv_data():
    print("graphing UV data")


@click.command()
def main():
    """example"""
    click.echo("welcome to sunscreen!")
    zipcode = check_local_zip()
    grab_todays_uv_data()
    graph_uv_data()
