import argparse
import os
import requests
 
from dotenv import load_dotenv
from urllib.parse import urlparse

BASE_URL = 'https://api-ssl.bitly.com/v4/'

def shorten_link(bitly_token, url):
    headers = {'Authorization': f'Bearer {bitly_token}'}

    payload = {
        'long_url': url,
    }

    short_url = f'{BASE_URL}shorten'

    response = requests.post(short_url, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()['link']


def parse_the_link(link):
    parsed_link = urlparse(link)
    return f'{parsed_link.netloc}{parsed_link.path}'


def count_clicks(bitly_token, link):
    headers = {'Authorization': f'Bearer {bitly_token}'}

    payload = {
        'unit': 'day',
        'units': -1,
    }

    count_clicks_url = f'{BASE_URL}bitlinks/{link}/clicks/summary'

    response = requests.get(count_clicks_url, headers=headers, params=payload)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(bitly_token, url):
    headers = {'Authorization': f'Bearer {bitly_token}'}

    parsed_url = parse_the_link(url)
    response = requests.get(f'{BASE_URL}bitlinks/{parsed_url}', headers=headers)
    return response.ok


def main():
    load_dotenv()

    bitly_token = os.getenv('BITLY_API_TOKEN')

    parser = argparse.ArgumentParser(description='Link shortener and clicks counter')
    parser.add_argument('url', help='Paste your link. It should start with HTTP or HTTPS')
    url = parser.parse_args().url

    if is_bitlink(bitly_token, url):
        try:
            parsed_url = parse_the_link(url)
            print(
                f'\u001b[32mClicks on link:\u001b[0m {count_clicks(bitly_token, parsed_url)}'
            )
        except requests.exceptions.HTTPError as error:
            print(
                f'\u001b[33mSomething went wrong. Please, check your link. \n\u001b[31m{error}'
            )
    else:
        try:
            bitlink = shorten_link(bitly_token, url)
            print(f'\u001b[32mShort link:\u001b[0m {bitlink}')
        except requests.exceptions.HTTPError as error:
            print(
                f'\u001b[33mSomething went wrong. Please, check your link. \n\u001b[31m{error}'
            )


if __name__ == '__main__':
    main()