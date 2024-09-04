import csv

def fromCSVtoLISTofDICT(csv_path: str) -> list[dict]:
    with open(csv_path, newline="", encoding="ISO-8859-1") as filecsv:
        lettore = csv.reader(filecsv,delimiter=",")

        flag_key = True
        dict_keys = []

        list_dict = []

        for header in lettore:
            current_dict = {}
            
            if flag_key:
                dict_keys = [h for h in header]
                flag_key = False
                continue

            for i in range(len(dict_keys)):
                current_dict[dict_keys[i]] = header[i]

            list_dict.append(current_dict)

    return list_dict

print(fromCSVtoLISTofDICT("./prova.csv"))

# return lista dict {title: str, author: str, book_id: str, url: str} 