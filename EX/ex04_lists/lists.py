"""Car inventory."""

def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    if all_cars == "":
        return []
    else:
        return all_cars.split(",")


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    list2 = []
    list1 = all_cars.split(",")
    for i in list1:
        make = i.split()
        list2.append(make[0])
        list2 = list(dict.fromkeys(list2))
    return list2


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    list2 = []
    list1 = all_cars.split(",")
    for i in list1:
        make = i.split()
        list2.append(make[-1])
        list2 = list(dict.fromkeys(list2))
    return list2
