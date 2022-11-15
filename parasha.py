import json

f = open('timetable.json', 'r', encoding='utf-8')
f = ' '.join(f.readlines())

data = json.loads(f)
xml_file = open('dfdf.xml', 'w', encoding='utf-8')
xml_file.write('<?xml version="1.0" encoding="UTF-8" ?>' + '\n')

tab_count = 0


def find_item(dictionary):
    global tab_count
    keys = dictionary.keys()
    for key in keys:
        if isinstance(dictionary[key], dict):
            xml_file.write(tab_count * '   ' + f"<{key}>\n")
            tab_count += 1
            find_item(dictionary[key])
            xml_file.write(tab_count * '   ' + f"</{key}>\n")
        else:
            xml_file.write(tab_count * '   ' + '<' + key + '>' + dictionary[key] + '</' + key + '>' + '\n')
    tab_count -= 1


find_item(data)
