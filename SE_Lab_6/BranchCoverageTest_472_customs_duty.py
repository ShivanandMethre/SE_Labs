import pytest

from customs_duty import duty_rate, total_duty, clearance_channel


def test_duty_rate_prohibited():
    with pytest.raises(ValueError):
        duty_rate("weapons", "US")


def test_duty_rate_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10


def test_duty_rate_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20


def test_duty_rate_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05


def test_duty_rate_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12


def test_duty_rate_books():
    assert duty_rate("books", "US") == 0


def test_duty_rate_other():
    assert duty_rate("furniture", "US") == 0.15


def test_negative_value():
    with pytest.raises(ValueError):
        total_duty("books", -1, "US", False)


def test_gift_value_below_limit():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_value_above_limit():
    assert total_duty("electronics", 6000, "US", True) == 200


def test_non_gift_value_below_limit():
    assert total_duty("books", 1000, "US", False) == 0


def test_non_gift_value_above_limit():
    assert total_duty("electronics", 1001, "US", False) == pytest.approx(200.2)


def test_minimum_duty():
    assert total_duty("clothing", 5101, "FTA", True) == 50


def test_clearance_prohibited():
    assert clearance_channel(1000, "weapons", True) == "refuse"


def test_clearance_high_value():
    assert clearance_channel(100001, "books", True) == "inspect"


def test_clearance_medium_no_documents():
    assert clearance_channel(20001, "books", False) == "inspect"


def test_clearance_medium_with_documents():
    assert clearance_channel(20001, "books", True) == "green"


def test_clearance_low_value():
    assert clearance_channel(10000, "books", False) == "green"