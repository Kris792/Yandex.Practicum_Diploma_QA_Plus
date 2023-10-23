import order_request


# Кристина Еремеева, 9-й поток — Финальный проект. Инженер по тестированию плюс

def test_get_order_by_track():
    track_number = order_request.get_order_info_by_track()
    assert track_number.status_code == 200
