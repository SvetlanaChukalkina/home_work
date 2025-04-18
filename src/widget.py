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
    elif number_for_mask == "":   #elif name_for_mask == "" or number_for_mask == "":
        return "Данные не введены"
    else:
        if len(number_for_mask) >= 16:
            return f"{name_for_mask} {get_mask_card_number(number_for_mask)}"
        return "Данные введены неверно"


def get_date(date: str) -> str:
    """Функция для форматирования даты"""
    all_month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    short_month_list = ["01", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    long_month_list = ["01", "03", "05", "07", "08", "10", "12"]

    if date[8:10].isdigit() and date[5:7].isdigit() and date[0:4].isdigit():
        if date[8] == "0" and date[9] != "0" and date[5:7] in all_month_list:
            return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
        elif date[8] in ["1", "2"] and date[5:7] in all_month_list:
            return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
        elif date[8:10] == "30" and date[5:7] in short_month_list:
            return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
        elif date[8:10] == "31" and date[5:7] in long_month_list:
            return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
        else:
            return "Данные введены неверно"
    elif date[8:10] == "" and date[5:7] == "" and date[0:4] == "":
        return "Данные не введены"
    else:
        return "Данные введены неверно"


print(get_date("2024-13-21T02:26:18.671407"))
print(get_date("2024-13-11T02:26:18.671407"))

print(get_date("2023-10-20T21:00:39Z"))
