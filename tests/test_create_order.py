import allure
import requests
from conftest import create_user
from data import Url, Endpoints


class TestCreateOrder:
    @allure.title('Успешное создание заказа авторизованным пользователем')
    def test_successful_create_order_user_with_authorization(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]}
        response = requests.post(f'{Url.URL}{Endpoints.ORDER_CREATE}', data=ingredients)
        assert response.status_code == 200

    @allure.title('Создание заказа неавторизованным пользователем')
    def test_successful_create_order_user_without_authorization(self, create_user):
        ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa70"]}
        response = requests.post(f'{Url.URL}{Endpoints.ORDER_CREATE}', data=ingredients)
        assert response.status_code == 200

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        response = requests.post(f'{Url.URL}{Endpoints.ORDER_CREATE}')
        assert (response.status_code == 400 and
                response.text == '{"success":false,"message":"Ingredient ids must be provided"}')

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_without_hash_ingredients(self, create_user):
        new_user = create_user
        new_user_log_pass = {
            "email": new_user[0],
            "password": new_user[1]
        }
        requests.post(f'{Url.URL}{Endpoints.USER_LOGIN}', data=new_user_log_pass)
        ingredients = {"ingredients": ["61c0c5a71d1f82001bd11161"]}
        response = requests.post(f'{Url.URL}{Endpoints.ORDER_CREATE}', data=ingredients)
        assert response.status_code == 500
