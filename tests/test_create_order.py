import allure
import pytest
import requests
from const import MessageText, Const
from data import person_data


class TestCreateOrder:

    @pytest.mark.parametrize(
        "firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color",
        person_data
    )
    @allure.title('Создание заказа с цветом')
    def test_create_order_with_color(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate,
                                     comment, color):
        data = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": [color] if color else [],
        }
        with allure.step('Отправка запроса на создание заказа'):
            response = requests.post(Const.CREATE_ORDER, json=data)

        with allure.step('Проверка, что заказ успешно создан'):
            assert response.status_code == 201
            assert MessageText.CREATE_ORDER in response.text