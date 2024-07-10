import csv

with open("./prova.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lettore = csv.reader(filecsv,delimiter=";")

    f_key: bool = False
    dict_key: list[str] = []
    key = []
    list_dict: list[dict] = []

    for header in lettore:
        header = header.__str__().split(",")
        print(header)
        if not f_key:
            f_key = True
            key = [h.strip() for h in header]
            continue

        current_dict: dict = {}
        for key, value in dict_key, header:
            current_dict[key] = value
        list_dict += current_dict
        print(current_dict)

    print("\n\nLISTA:", list_dict)


# return lista dict {title: str, author: str, book_id: str, url: str} 