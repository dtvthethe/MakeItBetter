import main

text = main.read('config.txt').split('\n')
my_dict = {}
for line in text:
    line = line.strip()
    if line:
        if line.startswith('[') and line.endswith(']'):
            key = line[1:-1]
            item_dict = {}
        elif '=' in line and '|' in line and key is not '':
            item_key, item_data = line.split('=')
            item_value, iten_type = item_data.split('|')
            exec('item_dict[item_key.strip()] = ' + iten_type.strip() + '("' + item_value.strip() + '")')
        else:
            continue
        my_dict[key] = item_dict
print(my_dict)
