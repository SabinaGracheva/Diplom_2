import allure


url = 'https://stellarburgers.nomoreparties.site'


class TestCreatingUser:
    @allure.title('Проверка, что пользователя можно создать')
    def test_create_new_user(self, create_user_response):
        user = create_user_response
        assert "accessToken" in user.text

    @allure.title('Проверка, что нельзя создать пользователя, который уже существует')
    def test_creating_a_registered_user(self):
        pass
