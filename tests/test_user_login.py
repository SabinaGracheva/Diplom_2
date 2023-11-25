import allure
import requests
from conftest import create_user
from data import Url, Endpoints


class TestUserLogin:
    @allure.title('Успешная авторизация пользователя в системе')
    def test_successful_user_authorization(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        access_token = response.json()['accessToken']
        refresh_token = response.json()['refreshToken']
        email = response.json()['user']['email']
        name = response.json()['user']['name']
        assert response.text == (f'{{"success":true,"accessToken":"{access_token}","refreshToken":"{refresh_token}",'
                                 f'"user":{{"email":"{email}","name":"{name}"}}}}')
        # для ревьюера - не выполнила проверку по статус коду, потому что он отсутствует в документации

    @allure.title('Авторизация пользователя в системе с неверным логином')
    def test_authorization_with_incorrect_login(self, create_user):
        new_user = create_user
        user_with_incorrect_log = {
            "email": "cat300@ya.ru",
            "password": new_user[1]
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=user_with_incorrect_log)
        assert (response.status_code == 401 and
                response.text == '{"success":false,"message":"email or password are incorrect"}')

    @allure.title('Авторизация пользователя в системе с неверным паролем')
    def test_authorization_with_incorrect_login(self, create_user):
        new_user = create_user
        user_with_incorrect_pass = {
            "email": new_user[0],
            "password": "112233"
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=user_with_incorrect_pass)
        assert (response.status_code == 401 and
                response.text == '{"success":false,"message":"email or password are incorrect"}')
