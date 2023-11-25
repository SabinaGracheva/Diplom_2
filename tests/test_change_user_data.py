import allure
import requests
from conftest import create_user
from data import Url, Endpoints
from faker import Faker


fake = Faker("ru_RU")


class TestUserDataUpdate:
    @allure.title('Успешное изменение email пользователя с авторизацией')
    def test_successful_update_user_email_with_authorization(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        token = response.json()['accessToken']
        update_user_data = {
            "email": fake.ascii_free_email(),
            "password": new_user[1]
        }
        response_update = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}',
                                         headers={'Authorization': f'{token}'}, data=update_user_data)
        email = response_update.json()['user']['email']
        name = response_update.json()['user']['name']
        assert response_update.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'
        # для ревьюера - не выполнила проверку по статус коду, потому что он отсутствует в документации

    @allure.title('Успешное изменение пароля пользователя с авторизацией')
    def test_successful_update_user_password_with_authorization(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        response = requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        token = response.json()['accessToken']
        update_user_data = {
            "email": new_user[0],
            "password": fake.password()
        }
        response_update = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}',
                                         headers={'Authorization': f'{token}'}, data=update_user_data)
        email = response_update.json()['user']['email']
        name = response_update.json()['user']['name']
        assert response_update.text == f'{{"success":true,"user":{{"email":"{email}","name":"{name}"}}}}'
        # для ревьюера - не выполнила проверку по статус коду, потому что он отсутствует в документации

    @allure.title('Изменение email пользователя без авторизации')
    def test_update_user_email_without_authorization_t(self, create_user):
        new_user = create_user
        update_user_email = {
            "email": new_user[0],
            "password": fake.password()
        }
        response = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}', data=update_user_email)
        assert (response.status_code == 401 and
                response.text == '{"success":false,"message":"You should be authorised"}')

    @allure.title('Изменение пароля пользователя без авторизации')
    def test_update_user_password_without_authorization(self, create_user):
        new_user = create_user
        update_user_pass = {
            "email": fake.ascii_free_email(),
            "password": new_user[1]
        }
        response = requests.patch(f'{Url.URL}{Endpoints.USER_DATA_UPDATE}', data=update_user_pass)
        assert (response.status_code == 401 and
                    response.text == '{"success":false,"message":"You should be authorised"}')
