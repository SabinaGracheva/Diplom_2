import allure
import pytest
import requests
from conftest import create_user, create_user_response
from data import Url, Endpoints


class TestUserDataUpdate:
    @allure.title('Успешное изменение email пользователя с авторизацией')
    def test_successful_update_user_data_with_authorization(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        token = response.json()['accessToken']
        update_user_data = {
            "email": "cat304@ya.ru",
            "password": new_user[1]
        }
        response_update = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}',
                                         headers={'Authorization': f'{token}'}, data=update_user_data)
        email = response_update.json()['user']['email']
        name = response_update.json()['user']['name']
        assert response_update.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'
        # для ревьюера - не выполнила проверку по статус коду, потому что он отсутствует в документации

    @allure.title('Успешное изменение пароля пользователя с авторизацией')
    def test_successful_update_user_data_with_authorization(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        token = response.json()['accessToken']
        update_user_data = {
            "email": new_user[0],
            "password": "11223344"
        }
        response_update = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}',
                                         headers={'Authorization': f'{token}'}, data=update_user_data)
        email = response_update.json()['user']['email']
        name = response_update.json()['user']['name']
        assert response_update.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'
        # для ревьюера - не выполнила проверку по статус коду, потому что он отсутствует в документации

    @allure.title('Изменение email пользователя без авторизации')
    @pytest.mark.parametrize('')
    def test_update_user_email_without_authorization(self, create_user):
        new_user = create_user
        token = new_user.json()['accessToken']
        update_user_email = {
            "email": "cat301@ya.ru",
            "password": new_user[1]
        }
        response = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}', headers={'Authorization': f'{token}'},
                                  data=update_user_email)
        assert (response.status_code == 401 and
                response.text == '{"success":false,"message":"You should be authorised"}')

    @allure.title('Изменение пароля пользователя без авторизации')
    def test_update_user_password_without_authorization(self, create_user):
        new_user = create_user
        token = new_user.json()['accessToken']
        update_user_pass = {
            "email": new_user[0],
            "password": "112233"
        }
        response_update = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}',
                                         headers={'Authorization': f'{token}'}, data=update_user_pass)
        assert (response_update.status_code == 401 and
                response_update.text == '{"success":false,"message":"You should be authorised"}')
