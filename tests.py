# Инна Калачева 11-я когорта - Финальный проект. Инженер по тестированию плюс

from sender_stand_request import get_order_status_code


def test_get_info_about_order():
    assert get_order_status_code() == 200
