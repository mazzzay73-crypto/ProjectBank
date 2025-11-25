import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.fixture
def number():
    return "4545 4545 4545 4545"


@pytest.mark.parametrize("result", ["4545 45** **** 4545"])
def test_get_mask_card_number(number: str, result) -> str:
    assert get_mask_card_number(number) == result

@pytest.fixture
def account():
    return "123456789"


@pytest.mark.parametrize("masked", ["**6789"])
def test_get_mask_account(account: str, masked) -> str:
    assert get_mask_account(account) == masked
