## Дипломный проект. Задание 2: API

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы тесты с проверками для ручек по:
- созданию пользователя
- авторизации пользователя
- изменению данных прользователя
- созданию заказа
- получению заказов по конкретному пользователю

### Активация тестового окружения

> `$ source env/bin/activate`

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание Allure-отчета о прохождении тестов**

>  `$ pytest tests.py --alluredir=allure_results`

**Формирование Allure-отчета в формате веб-страницы**

>  `$ allure serve allure_results`

### Структура проекта

`tests` - пакет, содержащий тесты, разделенные по функционалу:

`test_change_user_data.py` - файл с тестами на проверку endpoints по изменению данных пользователя
- `test_successful_update_user_email_with_authorization` - Успешное изменение email пользователя с авторизацией
- `test_successful_update_user_password_with_authorization` - Успешное изменение пароля пользователя с авторизацией
- `test_update_user_email_without_authorization` - Изменение email пользователя без авторизации
- `test_update_user_password_without_authorization` - Изменение пароля пользователя без авторизации

`test_creare_order` - файл с тестами на проверку endpoints по созданию заказа
- `test_successful_create_order_user_with_authorization` - Успешное создание заказа авторизованным пользователем
- `test_successful_create_order_user_without_authorization` - Создание заказа неавторизованным пользователем
- `test_create_order_without_ingredients` - Создание заказа без ингредиентов
- `test_create_order_without_hash_ingredients` - Создание заказа с неверным хешем ингредиентов

`test_create_user` - файл с тестами на проверку endpoints по созданию пользователя
- `test_create_new_user` - Проверка, что пользователь успешно регистрируется
- `test_creating_a_registered_user` - Создание пользователя, который уже существует
- `test_create_user_without_log_or_pass_or_name` - Создание пользователя без заполнения обязательного поля email, пароля или имени

`test_receivind_oser_orders` - файл с тестами на проверку endpoints по получению списка заказов конкретного пользователя
- `test_successful_receiving_orders_from_a_specific_user_with_authorization` - Успешное получение списка заказов конкретного авторизованного пользователя
- `test_receiving_orders_from_a_specific_user_without_authorization` - Получение списка заказов конкретного неавторизованного пользователя

`test_user_login` - файл с тестами на проверку endpoints по авторизации пользователя
- `test_successful_user_authorization` - Успешная авторизация пользователя в системе
- `test_authorization_with_incorrect_login` - Авторизация пользователя в системе с неверным логином
- `test_authorization_with_incorrect_login` - Авторизация пользователя в системе с неверным паролем

