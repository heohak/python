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
    if all_cars == "":
        return []
    for i in list1:
        i = i.partition(" ")[0]
        list2.append(i)
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
    if all_cars == "":
        return []
    for i in list1:
        i = i.partition(" ")[2]
        list2.append(i)
    list2 = list(dict.fromkeys(list2))
    return list2


def search_by_make(all_cars: str, make: str) -> list:

    result = []
    car_list = all_cars.split(",")
    for car in car_list:
        car_make = car.split(" ")[0]
        if car_make.upper() == make.upper():
            result.append(car)
    return result


def search_by_model(all_cars: str, model: str) -> list:
    result = []
    car_list = all_cars.split(",")
    for car in car_list:
        car_model = car.split(" ")[-1]
        car_model2 = car.split(" ")[-2]
        if car_model.upper() == model.upper():
            result.append(car)
        if car_model2.upper() == model.upper():
            result.append(car)
    return result


if __name__ == "__main__":

    print(list_of_cars("Audi A4,Skoda Superb,Audi A4"))  # ["Audi A4", "Skoda Superb", "Audi A4"]
    print(car_makes("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
                        # ['Audi', 'Skoda', 'BMW', 'Seat']

    print(car_makes("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # ['Mazda']

    print(car_makes(""))  # []

    print(car_models("Audi A4,Skoda Superb,Audi A4,Audi A6,Tesla Model S,Skoda Super Lux Sport"))  # ["A4", "Superb", "A6"]
    print(search_by_make("Audi A4,audi A5,AUDI a6 A7", "Audi"))
    print(search_by_model("Audi A4,Audi a4 2021,Audi A40", "a4"))
