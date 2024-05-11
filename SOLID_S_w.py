class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # Getter for the age attribute.
    @property
    def age(self):
        return self._age

    # Setter for the age attribute, also validates the age is in a valid range.
    @age.setter
    def age(self, age):
        if age < 0 or age >= 130:
            raise ValueError("Age must be between 0 and 130 ")
        self._age = age

    # Displays user information to the console.
    def display(self):
        print(f"{self.name}{self.last_name}{self.age}")

    # Reads user input from the console to create or update a User object.
    def input(self):
        self.name = input("Input name:")
        self.last_name = input("Input last name:")
        self.age = int(input("Input age:"))

# Create a User object, display its information,
# update it with user input, then display it again.
obj = User("Bill", "Windows", 34)
obj.display()
obj.input()
obj.display()