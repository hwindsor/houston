# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
import pytest


@pytest.mark.parametrize(
    'http_method,http_path',
    (
        ('GET', '/api/v1/users/'),
        ('GET', '/api/v1/users/11111111-1111-1111-1111-111111111111'),
        ('PATCH', '/api/v1/users/11111111-1111-1111-1111-111111111111'),
        ('GET', '/api/v1/users/me'),
    ),
)
def test_unauthorized_access(http_method, http_path, flask_app_client):
    response = flask_app_client.open(method=http_method, path=http_path)
    assert response.status_code == 401
