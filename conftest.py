import pytest
import requests
from create_new_user import register_new_user_and_return_login_password


url = 'https://stellarburgers.nomoreparties.site'


@pytest.fixture
def create_user():
    new_user = register_new_user_and_return_login_password()
    yield new_user[0]
    new_user_log_pass = {
        "email": new_user[0][0],
        "password": new_user[0][1],
        "name": new_user[0][2]
    }
    response = requests.delete(f'{url}/api/auth/user', data=new_user_log_pass)
    courier_id = response.json()['id']
    requests.delete(f'{url}/api/v1/courier/{courier_id}')


@pytest.fixture
def create_user_response():
    new_user = register_new_user_and_return_login_password()
    yield new_user[1]
    token = new_user[1].json()['accessToken']
    requests.delete(f'{url}/api/auth/user', headers={'Authorization': f'{token}'})
