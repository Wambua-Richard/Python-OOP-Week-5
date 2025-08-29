- - Assignment 1 - -

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self._battery_level = 100  # encapsulated attribute (private by convention)

    # Getter for battery level
    def get_battery_level(self):
        return self._battery_level

    # Setter for battery level with validation
    def set_battery_level(self, level):
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            print("Battery level must be between 0 and 100.")

    def charge(self):
        self._battery_level = 100
        print(f"{self.brand} {self.model} is now fully charged.")

    def use(self, hours):
        drain = hours * 10  # assume 10% battery per hour of use
        if self._battery_level - drain >= 0:
            self._battery_level -= drain
            print(f"{self.brand} {self.model} used for {hours} hour(s). Battery now at {self._battery_level}%.")
        else:
            print(f"Not enough battery to use for {hours} hour(s). Please charge the phone.")

    def get_status(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self._battery_level}%"

- - Assignment 2 - -

# Base class (can be abstract or just a generic parent)
class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Vehicle classes
class Car(Entity):
    def move(self):
        print("Driving")

class Bicycle(Entity):
    def move(self):
        print("Pedaling")

# Animal classes
class Dog(Entity):
    def move(self):
        print("Running")

class Bird(Entity):
    def move(self):
        print("Flying")

# Example usage
if __name__ == "__main__":
    entities = [Car(), Bicycle(), Dog(), Bird()]

    for e in entities:
        e.move()
