def get_nr_items(name1):
    items = name1.split(",")
    total_items = len(items)
    return total_items


print(get_nr_items("john,lisa,teresa"))

