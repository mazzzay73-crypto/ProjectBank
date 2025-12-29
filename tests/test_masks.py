import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.mark.parametrize(
    "number, result",
    [("4545454545454545", "4545 45** **** 4545"), ("4545 45 45 4545 4545", "4545 45** **** 4545"), ("", "")],
)
def test_get_mask_card_number(number: str, result: str):
    assert get_mask_card_number(number) == result


@pytest.mark.parametrize("account, masked", [("123456789", "**6789"), ("123", "**123"), ("", "")])
def test_get_mask_account(account: str, masked: str):
    assert get_mask_account(account) == masked
