class Restaurant:
    """A representation of a Restaurant"""

    def __init__(self, restaurant_name, restaurant_type):
        """Initialize attibutes to describe a Restaurant"""
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        """Return description of the restaurant"""
        print(f"Restaurant name {self.restaurant_name} and type {self.restaurant_type}.")

    def open_restaurant(self):
        """Indicating the restaurant is open"""
        print(f"Restaurant {self.restaurant_name} is open")

class IceCreamStand(Restaurant):
    """Specific kind of restaurant"""
    def __init__(self, restaurant_name, restaurant_type, flavors):
        """initialize parent class and child class"""
        self.flavors = flavors
        super().__init__(restaurant_name, restaurant_type)

    def list_flavors(self):
        result = ""
        if len(self.flavors) > 0:
            for flavor in self.flavors:
                result += flavor + " "
        else:
            result = "No hay sabores"
        return result

my_restaurant = Restaurant('Mama mia', 'Italiano')
print(my_restaurant.restaurant_name)
print(my_restaurant.restaurant_type)
my_restaurant.describe_restaurant()

ice_cream_stand = IceCreamStand('heladitos', 'heladeria', ['mora','fresa','durazno'])
print(ice_cream_stand.restaurant_name)
print(ice_cream_stand.restaurant_type)
ice_cream_stand.describe_restaurant()
print(ice_cream_stand.list_flavors())
