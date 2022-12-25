"""EX15."""
import json
import urllib.request
import urllib.parse
import urllib.error
import csv


class Child:
    """Child class."""
    def __init__(self, name, country):
        """Child constructor."""
        self.name = name
        self.country = country


class World:
    """World class."""
    def __init__(self):
        """World constructor."""
        self.nice_list = []
        self.naughty_list = []
        self.wishlist = {}

    def read_nice_list(self, filename):
        """Read nice list and add to list."""
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            self.nice_list = [row[0] for row in reader]
        return self.nice_list

    def read_naugty_list(self, filename):
        """Read naughty list and add to list."""
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            self.naughty_list = [row[0] for row in reader]
        return self.naughty_list

    def read_wishlist(self, filename):
        """Read wishlist and add to dict."""
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.wishlist[row[0]] = row[1]
        return self.wishlist

    def gift_to_child(self, child):
        """Gift to child."""
        if child.name in self.nice_list:
            return self.wishlist[child.name]
        elif child.name in self.naughty_list:
            return "coal"
        else:
            return "nothing"


class Product:
    """Product class."""
    def __init__(self, name, price, production_time, weight):
        """Product constructor."""
        self.name = name
        self.price = price
        self.production_time = production_time
        self.weight = weight

    def __repr__(self):
        """Product representation."""
        return f"Product({self.name}, {self.price}, {self.production_time}, {self.weight})"


API_URL = """https://cs.ttu.ee/services/xmas/gift?"""


class Warehouse:
    """Warehouse class."""
    def __init__(self):
        """Warehouse constructor."""
        self.products = {}

    def get_product_from_factory(self, name: str):
        """Get product from factory."""
        qs = urllib.parse.quote_plus(name)
        try:
            with urllib.request.urlopen(API_URL + "name=" + qs) as f:
                # read all
                contents = f.read()

                # to convert into regular string
                print(contents.decode("utf-8"))

                # read json to python object
                data = json.loads(contents.decode('utf-8'))
                print(data)

                product = Product(data["gift"], data["material_cost"], data["production_time"], data["weight_in_grams"])
                if data["gift"] not in self.products:
                    self.products[data["gift"]] = []
                self.products[data["gift"]].append(product)
                return product
        except urllib.error.HTTPError:
            return None
