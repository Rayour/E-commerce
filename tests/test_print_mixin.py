from typing import Any

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys: Any) -> None:
    Product("Ваза", "Описание вазы", 200.0, 9)
    message = capsys.readouterr().out.strip().split("\n")[-1]
    assert message == "Product('Ваза', 'Описание вазы', 200.0, 9)"

    Smartphone("Nokia", "Прочный", 20000.0, 9, 123, "3310", 32, "Синий")
    message = capsys.readouterr().out.strip().split("\n")[-1]
    assert message == "Smartphone('Nokia', 'Прочный', 20000.0, 9)"

    LawnGrass("Трава", "Красивая", 2000.0, 9, "Канада", "Неделя", "Зеленый")
    message = capsys.readouterr().out.strip().split("\n")[-1]
    assert message == "LawnGrass('Трава', 'Красивая', 2000.0, 9)"
