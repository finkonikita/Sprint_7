import allure
import requests
from const import MessageText, Const

class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    def test_login_courier(self, create_courier):
        login, password, _ = create_courier
        with allure.step('Отправка запроса на авторизацию курьера с валидными данными'):
            response = requests.post(Const.LOGIN_COURIER, json={
                "login": login,
                "password": password
            })
        with allure.step('Проверка, что статус ответа 200 и присутствует сообщение об успешной авторизации'):
            assert response.status_code == 200
            assert MessageText.LOGING_COURIER in response.text

    @allure.title('Проверка авторизации курьера без логина')
    def test_login_courier_without_login(self, create_courier):
        _, password, _ = create_courier
        with allure.step('Отправка запроса на авторизацию без логина'):
            response = requests.post(Const.LOGIN_COURIER, json={
                "login": '',
                "password": password
            })
        with allure.step('Проверка, что статус ответа 400 и сообщение об ошибке отсутствия данных'):
            assert response.status_code == 400
            assert MessageText.LOGING_COURIER_WITHOUT_DATA in response.text

    @allure.title('Проверка авторизации курьера без пароля')
    def test_login_courier_without_password(self, create_courier):
        login, _, _ = create_courier
        with allure.step('Отправка запроса на авторизацию без пароля'):
            response = requests.post(Const.LOGIN_COURIER, json={
                "login": login,
                "password": ''
            })
        with allure.step('Проверка, что статус ответа 400 и сообщение об ошибке отсутствия данных'):
            assert response.status_code == 400
            assert MessageText.LOGING_COURIER_WITHOUT_DATA in response.text

    @allure.title('Проверка авторизации курьера без логина и пароля')
    def test_login_courier_without_data(self):
        with allure.step('Отправка запроса на авторизацию без логина и пароля'):
            response = requests.post(Const.LOGIN_COURIER, json={
                "login": '',
                "password": '',
            })
        with allure.step('Проверка, что статус ответа 400 и сообщение об ошибке отсутствия данных'):
            assert response.status_code == 400
            assert MessageText.LOGING_COURIER_WITHOUT_DATA in response.text

    @allure.title('Проверка авторизации с несуществующими данными')
    def test_login_courier_fake_data(self):
        with allure.step('Отправка запроса на авторизацию с несуществующими данными'):
            response = requests.post(Const.LOGIN_COURIER, json={
                "login": 'victor',
                "password": 'qwertyuiopasd',
            })
        with allure.step('Проверка, что статус ответа 404 и сообщение об ошибке отсутствия курьера'):
            assert response.status_code == 404
            assert MessageText.LOGING_COURIER_FAKE_DATA in response.text