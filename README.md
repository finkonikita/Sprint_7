Финальный проект 7 спринта

Описание тестов:

test_create_courier.py - проверка создания курьера
test_login_courier.py - проверка авторизации курьера
test_create_order.py - проверка создания заказа
test_order_list.py - проверка полного списка заказов

Перед работой с репозиторием

Установить зависимости
pip3 install -r requirements.txt

Запустить все тесты из директории tests
pytest tests --alluredir=allure_results

Посмотреть отчет в веб версии пройденного прогона
allure serve allure_results# Sprint_7
