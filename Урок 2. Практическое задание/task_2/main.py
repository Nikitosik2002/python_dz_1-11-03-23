import json


def write_order_to_json(it, quan, pr, buy, dat):
    dict_in_json = {
        "item": it,
        "quantity": quan,
        "price": pr,
        "buyer": buy,
        "date": dat

    }

    with open('orders.json') as f_n:
        obj = json.load(f_n)
        obj['orders'].append(dict_in_json)

    with open('orders.json', 'w') as f_w:
        json.dump(obj, f_w, indent=4)


write_order_to_json("json", "3", "400", "vasiliy", "asdf")
