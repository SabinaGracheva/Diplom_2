import requests
import random
import string

# метод регистрации нового пользователя возвращает список из email и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_user_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем email, пароль и имя пользователя
    email = f'{generate_random_string(7)}@ya.ru'
    password = generate_random_string(10)
    user_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": user_name
    }

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    # если регистрация прошла успешно (код ответа 200), добавляем в список email и пароль пользователя
    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(user_name)

    # возвращаем список
    return login_pass, response
