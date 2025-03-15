from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_information: str) -> str:
    """Функция для обработки и маскировки информации о картах и счетах"""
    card_or_account_num = []
    card_name = []
    shared_information = card_information.split(" ")
    for i in shared_information:
        if i.isdigit():
            card_or_account_num.append(i)
        if i.isalpha():
            card_name.append(i)
    number_for_mask = "".join(card_or_account_num)
    name_for_mask = " ".join(card_name)
    if name_for_mask == "Счет":
        if len(number_for_mask) < 6:
            return "Данные введены неверно"
        return f"{name_for_mask} {get_mask_account(number_for_mask)}"
    elif name_for_mask == "" or number_for_mask == "":
        return "Данные не введены"
    else:
        if len(number_for_mask) == 16:
            return f"{name_for_mask} {get_mask_card_number(number_for_mask)}"
        return "Данные введены неверно"


def get_date(date: str) -> str:
    """Функция для форматирования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
