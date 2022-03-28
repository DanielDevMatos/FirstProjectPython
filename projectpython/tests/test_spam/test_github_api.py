from unittest.mock import Mock

import pytest

from projectpython import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/635?v=4'
    resp_mock.json.return_value ={
            'login': 'daniel',
            'id': 635,
            'avatar_url': url
        }
    get_mocker = mocker.patch('projectpython.github_api.requests.get')
    get_mocker.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('daniel')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('danieldevmatos')
    assert 'https://avatars.githubusercontent.com/u/99550469?v=4' == url
