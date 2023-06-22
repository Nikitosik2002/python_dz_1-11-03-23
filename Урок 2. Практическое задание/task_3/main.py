import yaml

dict_in_yaml = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price':
        {'computer': '100 \u20AC',
         'printer': '5 \u20AC',
         'keyboard': '4 \u20AC',
         'mouse': '1 \u20AC',
         }
}

with open('File.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(dict_in_yaml, f_n, default_flow_style=False, allow_unicode=True)