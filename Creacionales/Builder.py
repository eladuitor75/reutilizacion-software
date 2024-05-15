# Builder Pattern Example

# Product
class Car:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ", ".join(self.parts)

# Builder Interface
class CarBuilder:
    def reset(self):
        pass

    def set_engine(self):
        pass

    def set_wheels(self):
        pass

    def set_gps(self):
        pass

# Concrete Builders
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_engine(self):
        self.car.add("Sports Engine")

    def set_wheels(self):
        self.car.add("Sports Wheels")

    def set_gps(self):
        self.car.add("GPS")

    def get_result(self):
        return self.car

class CityCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_engine(self):
        self.car.add("City Engine")

    def set_wheels(self):
        self.car.add("City Wheels")

    def set_gps(self):
        self.car.add("Basic GPS")

    def get_result(self):
        return self.car

# Director
class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_sports_car(self):
        self._builder.reset()
        self._builder.set_engine()
        self._builder.set_wheels()
        self._builder.set_gps()
        return self._builder.get_result()

    def construct_city_car(self):
        self._builder.reset()
        self._builder.set_engine()
        self._builder.set_wheels()
        self._builder.set_gps()
        return self._builder.get_result()

# Client code
def run():
    sports_car_builder = SportsCarBuilder()
    city_car_builder = CityCarBuilder()

    director = Director(sports_car_builder)
    sports_car = director.construct_sports_car()
    print("Sports Car built with parts:", sports_car.list_parts())

    director = Director(city_car_builder)
    city_car = director.construct_city_car()
    print("City Car built with parts:", city_car.list_parts())

    explanation = """
    Builder Pattern:

    El patrón Builder permite construir objetos complejos paso a paso. A diferencia de otros patrones de creación, el patrón Builder no requiere que los productos tengan una interfaz común.
    Este patrón es particularmente útil cuando se necesita crear diferentes representaciones de un objeto complejo.

    En este ejemplo, hemos creado una clase Car que representa el producto complejo. La interfaz CarBuilder define los métodos necesarios para construir las partes del coche.
    Las clases concretas SportsCarBuilder y CityCarBuilder implementan esta interfaz para construir coches específicos (deportivo y de ciudad).

    El Director, que recibe un objeto builder, se encarga de dirigir el proceso de construcción del coche llamando a los métodos del builder en un orden específico.
    De esta manera, podemos crear diferentes representaciones del coche utilizando diferentes builders concretos.
    """
    print(explanation)
