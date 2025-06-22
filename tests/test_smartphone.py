from src.smartphone import Smartphone


def test_smartphone_init(smartphone: Smartphone) -> None:
    assert smartphone.name == "Xiaomi Redmi Note 11"
    assert smartphone.description == "1024GB, Синий"
    assert smartphone.price == 31000.0
    assert smartphone.quantity == 14
    assert smartphone.efficiency == 90.3
    assert smartphone.model == "Note 11"
    assert smartphone.memory == 1024
    assert smartphone.color == "Синий"
