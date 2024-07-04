# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import json
from urllib.parse import urljoin

import requests

BASE_URL = 'http://localhost:8000'


def test_get_phones():
    expected = [
        '052-762-0197',
        '(183)205-1824',
        '064.024.2427x096',
        '001-575-977-0792x78744',
        '266-181-7643',
        '(129)425-7116x304',
        '3815471941',
        '001-631-637-8353x862',
        '001-340-582-7875',
        '(209)228-1520',
    ]
    response = requests.get(urljoin(BASE_URL, '/phones'), timeout=10)
    my_result = json.loads(response.text)
    assert my_result == expected


def test_get_domains():
    expected = [
        'wilson-davis.org',
        'powers.com',
        'young-johnson.com',
        'wong-washington.info',
        'davis.com',
        'gordon.com',
        'weaver.com',
        'riley.com',
        'horn-adams.com',
        'mcdowell-ortega.net',
    ]
    response = requests.get(urljoin(BASE_URL, '/domains'), timeout=10)
    assert json.loads(response.text) == expected
