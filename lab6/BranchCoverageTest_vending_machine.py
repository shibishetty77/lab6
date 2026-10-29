# Lab 6: Branch coverage tests — 100% branch coverage achieved.
from vending_machine import select_item, make_change, purchase


def test_credit_below_price():
    assert select_item("chips", {"chips": 1}, 99) == "insufficient"


def test_credit_equal_to_price():
    assert select_item("chips", {"chips": 1}, 100) == "ok"


def test_credit_above_price():
    assert select_item("chips", {"chips": 1}, 150) == "ok"


def test_change_loop_skipped():
    assert make_change(0) == []


def test_change_loop_executed():
    assert make_change(50) == [50]


def test_remaining_unrepresentable_amount():
    assert make_change(1) is None


def test_purchase_rejected_does_not_change_stock():
    stock = {"chips": 2}

    result = purchase("chips", stock, 50)

    assert result == ("insufficient", [])
    assert stock["chips"] == 2


def test_purchase_success_decrements_stock():
    stock = {"chips": 2}

    result = purchase("chips", stock, 100)

    assert result == ("dispensed", [])
    assert stock["chips"] == 1
def test_invalid_item_purchase():
    assert purchase("water", {}, 100) == ("invalid", [])


def test_sold_out_item_purchase():
    assert purchase("cola", {"cola": 0}, 200) == ("sold_out", [])


def test_change_exact_multiple_coins():
    assert make_change(75) == [50, 25]


def test_change_with_unrepresentable_remainder():
    assert make_change(7) is None


def test_purchase_exact_payment():
    stock = {"cola": 1}

    result = purchase("cola", stock, 150)

    assert result == ("dispensed", [])
    assert stock["cola"] == 0


def test_purchase_no_exact_change():
    stock = {"chips": 1}

    result = purchase("chips", stock, 103)

    assert result == ("no_exact_change", [])
    assert stock["chips"] == 1


def test_negative_change():
    import pytest

    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)