import requests
from data import Url, Endpoints
from faker import Faker


fake = Faker("ru_RU")


# метод регистрации нового пользователя возвращает список из email и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    email = fake.ascii_free_email()
    password = fake.password()
    user_name = fake.first_name()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": user_name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Url.URL}{Endpoints.USER_REGISTRATION}', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список email, пароль и имя пользователя
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(user_name)

    # возвращаем список
    return login_pass, response
