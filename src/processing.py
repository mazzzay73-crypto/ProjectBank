def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    filtred_list = []
    for item in list_dict:
        if item.get("state") == state:
            filtred_list.append(item)
    return filtred_list


list_dict = input("Please enter your list: ")
print(filter_by_state)
