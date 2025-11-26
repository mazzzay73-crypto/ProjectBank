from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date

card_number = input("Please enter card number: ")
masked_number = get_mask_card_number(card_number)
print(masked_number)

account_number = input("Please enter account number: ")
masked_account = get_mask_account(account_number)
print(masked_account)

date = input("Please enter date")
correct_day = get_date(date)
print(correct_day)

card_info = input("Please enter your number: ")
result = mask_account_card(card_info)
print(result)
