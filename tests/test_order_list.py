import allure
import requests
from const import MessageText, Const


class TestGetOrderList:
    @allure.title('Проверка получения списка заказа')
    def test_get_order_list(self):
        with allure.step('Отправка GET запроса на получение списка заказов'):
            response = requests.get(Const.ORDER_LIST)
            allure.attach(response.text, name='Response body', attachment_type=allure.attachment_type.JSON)

        with allure.step('Проверка кода ответа и содержимого'):
            assert response.status_code == 200
            assert MessageText.LIST_ORDERS in response.text