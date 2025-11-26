from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date

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

list_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


filtered = filter_by_state(list_dict, state="EXECUTED")
print(filtered)

list_of_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


sorted_list = sort_by_date(list_of_dict, reverse = True)
print(sorted_list)
