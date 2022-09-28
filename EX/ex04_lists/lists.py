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
    """Search by make."""
    result = []
    car_list = all_cars.split(",")
    for car in car_list:
        car_make = car.split(" ")[0]
        if car_make.upper() == make.upper():
            result.append(car)
    return result


def search_by_model(all_cars: str, model: str) -> list:
    """Search by model."""
    result = []
    car_list = all_cars.split(",")
    for car in car_list:
        car_model = car.upper().split(" ")[1:]
        if model.upper() in car_model:
            result.append(car)
    return result


def car_duplicate(all_cars: str) -> list:
    """
    Mu enda funktsioon.
    """
    car_list = list_of_cars(all_cars)
    if all_cars == "":
        return []
    make_list = car_makes(all_cars)
    result = []
    for make in make_list:
        a = [make, []]
        for car in car_list:
            car = car.split(" ", 1)
            if car[0] == make:
                a[1].append(car[1])
        result.append(a)
    return result


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    car_list = list(dict.fromkeys(list_of_cars(all_cars)))
    if all_cars == "":
        return []
    make_list = car_makes(all_cars)
    result = []
    for make in make_list:
        a = [make, []]
        for car in car_list:
            car = car.split(" ", 1)
            if car[0] == make:
                a[1].append(car[1])
        result.append(a)
    return result


def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    if car_list == []:
        return car_make_and_models(all_cars)
    result = []
    for car in car_list:
        if car[0] not in result:
            make = car[0]
            for x in car[1]:
                if x not in result:
                    model = "".join(x)
                    make_and_model = make + " " + model
                    result.append(make_and_model)

    list_as_string = ",".join(result)
    all_ever_cars = list_as_string + "," + all_cars
    final = car_make_and_models(all_ever_cars)
    return final


print(car_make_and_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
# [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon']]]
print(car_make_and_models("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [['Mazda', ['6']]]
print(car_make_and_models(""))  # []

print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]],
               "Audi A6,BMW A B C,Audi A4"))
# [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.
    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    list1 = car_duplicate(all_cars)
    if all_cars == "":
        return []
    result = []
    for car in list1:
        make = car[0]
        arv = len(car[1])
        a = (make, arv)
        result.append(a)
    return result


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    result = []
    for car in cars:
        if car[0] not in result:
            make = car[0]
            for x in car[1]:
                if x not in result:
                    model = "".join(x)
                    make_and_model = make + " " + model
                    result.append(make_and_model)

    list_as_string = ",".join(result)
    return list_as_string


print(number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6"))  # [('Audi', 2), ('Skoda', 1), ('Seat', 1)]
print(number_of_cars("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [('Mazda', 4)]

print(number_of_cars(""))  # []

print(car_list_as_string([['Audi', ['A4']], ['Skoda', ['Superb']]]))  # "Audi A4,Skoda Superb"
