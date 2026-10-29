
import pytest

from vending_machine import select_item, make_change, purchase


def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_missing_stock_item():
    assert select_item("chips", {}, 200) == "sold_out"


def test_insufficient_credit():
    assert select_item("cola", {"cola": 2}, 100) == "insufficient"


def test_valid_selection():
    assert select_item("cola", {"cola": 2}, 150) == "ok"


def test_exact_change_zero():
    assert make_change(0) == []


def test_change_using_one_coin():
    assert make_change(100) == [100]


def test_change_using_multiple_coins():
    assert make_change(185) == [100, 50, 25, 10]


def test_negative_change_raises_error():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)


def test_unrepresentable_change():
    assert make_change(3) is None


def test_purchase_invalid_item():
    assert purchase("water", {}, 100) == ("invalid", [])


def test_purchase_sold_out():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])


def test_purchase_insufficient_credit():
    assert purchase("cola", {"cola": 2}, 100) == ("insufficient", [])


def test_successful_purchase_and_stock_update():
    stock = {"cola": 2}
    status, change = purchase("cola", stock, 200)

    assert status == "dispensed"
    assert change == [50]
    assert stock["cola"] == 1


def test_purchase_without_exact_change():
    stock = {"chips": 1}
    assert purchase("chips", stock, 103) == ("no_exact_change", [])
    assert stock["chips"] == 1
