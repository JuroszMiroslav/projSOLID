from abc import ABC, abstractmethod
import json
'''ABC (Abstract Base Class):

ABC je třída, kterou lze použít jako základní třídu pro definování abstraktních tříd. Třídy, které dědí z ABC, mohou obsahovat jednu nebo více abstraktních metod a nemohou být instanciovány přímo, což znamená, že slouží jako šablona pro další třídy.
Použití ABC jako základní třídy pomáhá definovat rozhraní pro ostatní třídy a zajišťuje, že všechny metody označené jako abstraktní musí být implementovány v odvozených třídách.
abstractmethod:

abstractmethod je dekorátor, který lze použít k označení metod ve třídě jako "abstraktní". To znamená, že tato metoda musí být definována v každé odvozené třídě, která dědí z abstraktní základní třídy. Pokud je třída odvozena z abstraktní základní třídy a neimplementuje všechny abstraktní metody, nemůže být instanciována (tj. nelze vytvořit její objekty).
Dekorátor abstractmethod umožňuje vývojářům definovat, které metody by měly být považovány za esenciální pro fungování třídy a zajišťuje, že tyto metody jsou implementovány všemi odvozenými třídami.
'''



# Base Pizza class
class Pizza(ABC):
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    def __str__(self):
        return f"{self.name} with {' and '.join(self.toppings)}"

    def add_topping(self, topping):
        if topping not in self.toppings:
            self.toppings.append(topping)

# Pizza Factory using registration to avoid modifying the factory when adding new pizza types
class PizzaFactory:
    pizza_types = {}

    @staticmethod
    def register_pizza(pizza_type, constructor):
        PizzaFactory.pizza_types[pizza_type] = constructor

    @staticmethod
    def create_pizza(pizza_type, *args):
        constructor = PizzaFactory.pizza_types.get(pizza_type)
        if not constructor:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
        return constructor(*args)

# Payment strategies
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} by card.")

# Order handling
class Order:
    def __init__(self, payment_method, logger):
        self.pizzas = []
        self.payment_method = payment_method
        self.logger = logger

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def checkout(self):
        total_cost = len(self.pizzas) * 10  # Example cost calculation
        self.payment_method.pay(total_cost)
        for pizza in self.pizzas:
            print(pizza)
        self.logger.log(self.pizzas)

# Logger class
class Logger(ABC):
    @abstractmethod
    def log(self, data):
        pass

class FileLogger(Logger):
    def log(self, data):
        with open("orders.txt", "a") as file:
            for item in data:
                file.write(str(item) + "\n")

# Registering pizza types
PizzaFactory.register_pizza("margherita", lambda: Pizza("Margherita", ["tomato sauce", "mozzarella"]))
PizzaFactory.register_pizza("pepperoni", lambda: Pizza("Pepperoni", ["tomato sauce", "mozzarella", "pepperoni"]))
PizzaFactory.register_pizza("hawaiian", lambda: Pizza("Hawaiian", ["tomato sauce", "mozzarella", "pineapple", "ham"]))
PizzaFactory.register_pizza("vegan", lambda: Pizza("Vegan", ["tomato sauce", "vegan cheese"]))
PizzaFactory.register_pizza("custom", lambda toppings: Pizza("Custom", toppings))

# Example usage
payment_method = CardPayment()
logger = FileLogger()
order = Order(payment_method, logger)
order.add_pizza(PizzaFactory.create_pizza("margherita"))
order.add_pizza(PizzaFactory.create_pizza("custom", ["onion", "bell peppers"]))
order.checkout()


'''
popis SOLID principu na ukolu
Princip jediné zodpovědnosti (Single Responsibility Principle, SRP):

Třídy Pizza: Každá podtřída Pizza je zodpovědná pouze za definování svých ingrediencí. Tím je zajištěno, že třídy pizz neřeší nic jiného, jako například vytváření instancí nebo správu typů pizz.
Třída Order: Tato třída nyní spravuje pouze objednávky – sleduje objednané pizzy a zpracovává platby. Již přímo nezpracovává detaily plateb a nezabývá se logováním dat, což znamená, že tato třída se soustředí jen na své klíčové funkce.
Třídy Logger: Zavedení abstraktní třídy Logger a podtřídy FileLogger odděluje zodpovědnost za logování detailů objednávek od logiky zpracování objednávek, čímž se dodržuje SRP přiřazením zodpovědnosti za logování výhradně vyhrazené třídě.
Princip otevřenosti/zavřenosti (Open/Closed Principle, OCP):

Pizza Factory: Díky systému registrace typů pizz může PizzaFactory být rozšířena bez změny stávajícího kódu. Nové typy pizz lze snadno přidat registrací nových funkcí bez nutnosti změny vnitřní logiky továrny.
Implementace Logger: Rozhraní Logger umožňuje přidávat nové mechanismy logování bez úpravy existujícího kódu pro logování. Můžete vytvořit různé typy loggerů (například DatabaseLogger nebo CloudLogger), které implementují rozhraní Logger, aniž byste museli měnit logiku zpracování objednávek.
Liskovův substituční princip (Liskov Substitution Principle, LSP):

Metody platby: Abstraktní třída PaymentMethod zajistí, že všechny její podtřídy (jako CashPayment a CardPayment) dodržují stejné rozhraní, což znamená, že jakákoli metoda platby může být zaměněna za jinou bez ovlivnění chování systému.
Typy Logger: Různé implementace loggerů mohou být bezproblémově zaměněny, pokud dodržují rozhraní Logger. To umožňuje flexibilitu v tom, jak jsou data objednávek logována, aniž by to ovlivnilo správu objednávek.
Princip segregace rozhraní (Interface Segregation Principle, ISP):

Rozhraní pro platby a logování: Tato rozhraní jsou navržena tak, aby byla minimální a specifická pro potřeby jejich uživatelů. Klienti rozhraní PaymentMethod a Logger nejsou nuceni záviset na metodách, které nepoužívají, čímž se dodržuje ISP.
Princip inverze závislostí (Dependency Inversion Principle, DIP):

Injektáž závislostí v třídě Order: Třída Order nyní přijímá závislosti (metodu platby a logger) jako parametry konstruktoru, což znamená, že závisí na abstrakcích, nikoli na konkrétních implementacích. To zlepšuje modularitu a testovatelnost kódu.
Použití abstrakce: Všechny funkcionality pro platbu a logování jsou závislé na abstraktních třídách nebo rozhraních, což znamená, že vysokoúrovňové moduly (jako je Order) nejsou závislé na nízkoúrovňových modulech, ale na abstrakcích.

'''
