
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
