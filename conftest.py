import pytest
import requests
from const import Const


@pytest.fixture
def helpers():
    class Helpers:
        def generate_data(self):
            import random, string
            login = 'user_' + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            password = 'pass_' + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            first_name = 'Имя_' + ''.join(random.choices(string.ascii_letters, k=4))
            return login, password, first_name

        def delete_courier(self, login, password):
            login_resp = requests.post(Const.LOGIN_COURIER, data={"login": login, "password": password})
            if login_resp.status_code == 200:
                courier_id = login_resp.json().get("id")
                if courier_id:
                    requests.delete(f"{Const.DELETE_COURIER}/{courier_id}")

        def register_new_courier_and_return_login_password(self):
            login, password, first_name = self.generate_data()
            response = requests.post(Const.CREATE_COURIER, data={
                "login": login,
                "password": password,
                "firstName": first_name
            })
            assert response.status_code == 201
            return login, password, first_name

    return Helpers()


@pytest.fixture
def create_courier(helpers):
    login, password, first_name = helpers.generate_data()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response_create = requests.post(Const.CREATE_COURIER, data=payload)
    assert response_create.status_code == 201, "Не удалось создать курьера в фикстуре"

    yield login, password, first_name

    helpers.delete_courier(login, password)