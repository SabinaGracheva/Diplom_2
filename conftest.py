import pytest
import requests
from create_new_user import register_new_user_and_return_login_password
from data import Url, Endpoints


@pytest.fixture
def create_user():
    new_user = register_new_user_and_return_login_password()
    yield new_user[0]
    new_user[1]
    # new_user_log_pass = {
    #     "email": new_user[0][0],
    #     "password": new_user[0][1],
    #     "name": new_user[0][2]
    # }
    # response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', new_user_log_pass)
    # token = response.json()['accessToken']
    token = new_user[1].json()['accessToken']
    requests.delete(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}', headers={'Authorization': f'{token}'})


@pytest.fixture
def create_user_response():
    new_user = register_new_user_and_return_login_password()
    yield new_user[1]
    token = new_user[1].json()['accessToken']
    requests.delete(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}', headers={'Authorization': f'{token}'})


@pytest.fixture
def create_user_response_and_data():
    new_user = register_new_user_and_return_login_password()
    yield new_user[0], new_user[1]
    token = new_user[1].json()['accessToken']
    requests.delete(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}', headers={'Authorization': f'{token}'})