from urllib.parse import urljoin

import requests

BASE_URL = 'http://localhost:8080'


def test_has_form():
    response = requests.get(urljoin(BASE_URL, '/courses/new'), timeout=10)
    assert 'title' in response.text
    assert 'paid' in response.text


def test_validate_empty_form():
    data = {'title': '', 'paid': ''}
    response = requests.post(
        urljoin(BASE_URL, '/courses'),
        data=data,
        timeout=10
    )
    assert response.status_code == 422
    print(response.text)
    assert "Can&#39;t be blank" in response.text


def test_validate_empty_paid():
    data = {'title': 'How to Foobar', 'paid': ''}
    response = requests.post(
        urljoin(BASE_URL, '/courses'),
        data=data,
        timeout=10
    )
    assert "Can&#39;t be blank" in response.text
    assert 'How to Foobar' in response.text


def test_validate_empty_title():
    data = {'title': '', 'paid': '1'}
    response = requests.post(
        urljoin(BASE_URL, '/courses'),
        data=data,
        timeout=10
    )
    assert "Can&#39;t be blank" in response.text


def test_escaping():
    data = {'title': '<script></script>', 'paid': ''}
    response = requests.post(
        urljoin(BASE_URL, '/courses'),
        data=data,
        timeout=10
    )
    assert '&lt;script&gt;&lt;/script&gt;' in response.text


def test_post():
    data = {'title': '<script></script>', 'paid': '1'}
    response = requests.post(
        urljoin(BASE_URL, '/courses'),
        data=data,
        allow_redirects=False, timeout=10
    )
    assert response.status_code == 302
    response = requests.post(
        urljoin(BASE_URL, '/courses'),
        data=data,
        timeout=10
    )
    assert '&lt;script&gt;&lt;/script&gt;' in response.text
