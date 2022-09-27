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
    res = []
    for car in car_list:
        for i in car:
            if car[0] not in res:
                res.append(car[0])
                for x in car[1]:
                    if x not in res:
                        res.append(x)

    print(res)
    aa = res[0]
    bb = res[1]
    cc = res[2]
    dd = res[3]
    a1 = " ".join([aa, bb])
    a2 = " ".join([cc, dd])
    print(a1)
    print(a2)
    list1 = [a1, a2]
    print(list1)
    string1 = ",".join(list1)
    print(string1)
    end = string1 + "," + all_cars
    final = car_make_and_models(end)
    return final


print(car_make_and_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon,Skoda Superb,Skoda Superb,BMW x5"))
# [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon']]]
print(car_make_and_models("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [['Mazda', ['6']]]
print(car_make_and_models(""))  # []

print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]],
               "Audi A6,BMW A B C,Audi A4"))
# [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
