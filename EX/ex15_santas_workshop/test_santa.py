from santa import *


def test_nice_list_empty():
    world = World()
    result = world.read_nice_list("empty.csv")
    assert result == []


def test_nice_list_children():
    world = World()
    result = world.read_nice_list("ex15_nice_list.csv")
    assert result[0] == "Libby"
    assert result[-1] == "Stacy"


def test_naughty_list_empty():
    world = World()
    result = world.read_naugty_list("empty.csv")
    assert result == []


def test_naughty_list_children():
    world = World()
    result = world.read_naugty_list("ex15_naughty_list.csv")
    assert result[0] == "Tanya"
    assert result[-1] == "Bailey"


def test_wishlist_empty():
    world = World()
    result = world.read_wishlist("empty.csv")
    assert result == {}


def test_wishlist_random_child():
    world = World()
    result = world.read_wishlist("ex15_wish_list.csv")
    assert result["Dylan"] == " Roller skates"


def test_product_not_in_factory():
    warehouse = Warehouse()
    result = warehouse.get_product_from_factory("helicopter")
    assert result == None


def test_product_from_factory():
    warehouse = Warehouse()
    result = warehouse.get_product_from_factory("New phone")
    assert result.name == "New phone"
    assert result.price == 100
    assert result.production_time == 9
    assert result.weight == 200


def test_give_gift_to_nice_child():
    world = World()
    world.read_nice_list("ex15_nice_list.csv")
    world.read_naugty_list("ex15_naughty_list.csv")
    world.read_wishlist("ex15_wish_list.csv")
    child = Child("Lexie", "Canada")
    result = world.gift_to_child(child)
    assert result == " Mermaid barbie"


def test_give_gift_to_naughty_child():
    world = World()
    world.read_nice_list("ex15_nice_list.csv")
    world.read_naugty_list("ex15_naughty_list.csv")
    world.read_wishlist("ex15_wish_list.csv")
    child = Child("Jamie", "Canada")
    result = world.gift_to_child(child)
    assert result == "coal"
