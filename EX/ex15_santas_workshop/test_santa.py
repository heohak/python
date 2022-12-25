"""Test for the Santa's Workshop exercise"""
from santa import World, Child, Warehouse


def test_nice_list_empty():
    """Test that the nice list is empty."""
    world = World()
    result = world.read_nice_list("empty.csv")
    assert result == []


def test_nice_list_random_children():
    """Test random children in the nice list."""
    world = World()
    result = world.read_nice_list("ex15_nice_list.csv")
    assert result[0] == "Libby"
    assert result[-1] == "Stacy"


def test_naughty_list_empty():
    """Test that the naughty list is empty."""
    world = World()
    result = world.read_naugty_list("empty.csv")
    assert result == []


def test_naughty_list_children():
    """Test random children in the naughty list."""
    world = World()
    result = world.read_naugty_list("ex15_naughty_list.csv")
    assert result[0] == "Tanya"
    assert result[-1] == "Bailey"


def test_wishlist_empty():
    """Test that the wishlist is empty."""
    world = World()
    result = world.read_wishlist("empty.csv")
    assert result == {}


def test_wishlist_random_child():
    """Test random child present in the wishlist."""
    world = World()
    result = world.read_wishlist("ex15_wish_list.csv")
    assert result["Dylan"] == " Roller skates"


def test_product_not_in_factory():
    """Test that the product is not in the factory."""
    warehouse = Warehouse()
    result = warehouse.get_product_from_factory("helicopter")
    assert result == None


def test_product_from_factory():
    """Test that the product is in the factory."""
    warehouse = Warehouse()
    result = warehouse.get_product_from_factory("New phone")
    assert result.name == "New phone"
    assert result.price == 100
    assert result.production_time == 9
    assert result.weight == 200


def test_give_gift_to_nice_child():
    """Test that the gift is given to the nice child."""
    world = World()
    world.read_nice_list("ex15_nice_list.csv")
    world.read_naugty_list("ex15_naughty_list.csv")
    world.read_wishlist("ex15_wish_list.csv")
    child = Child("Lexie", "Canada")
    result = world.gift_to_child(child)
    assert result == " Mermaid barbie"


def test_give_gift_to_naughty_child():
    """Test that the gift is given to the naughty child."""
    world = World()
    world.read_nice_list("ex15_nice_list.csv")
    world.read_naugty_list("ex15_naughty_list.csv")
    world.read_wishlist("ex15_wish_list.csv")
    child = Child("Jamie", "Canada")
    result = world.gift_to_child(child)
    assert result == "coal"
