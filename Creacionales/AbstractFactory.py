# Abstract Factory Pattern Example

# Abstract Products
class Button:
    def click(self):
        pass

class Checkbox:
    def check(self):
        pass

# Concrete Products
class MacOSButton(Button):
    def click(self):
        return "Clicking a MacOS button."

class WindowsButton(Button):
    def click(self):
        return "Clicking a Windows button."

class MacOSCheckbox(Checkbox):
    def check(self):
        return "Checking a MacOS checkbox."

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Checking a Windows checkbox."

# Abstract Factory
class GUIFactory:
    def create_button(self):
        pass

    def create_checkbox(self):
        pass

# Concrete Factories
class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

# Client code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    
    print(button.click())
    print(checkbox.check())

def run(platform):
    if platform == 'mac':
        factory = MacOSFactory()
    elif platform == 'windows':
        factory = WindowsFactory()
    else:
        raise ValueError("Plataforma no soportada")
    
    client_code(factory)

    explanation = """
    Abstract Factory Pattern:

    El patrón Abstract Factory proporciona una interfaz para crear familias de objetos relacionados o dependientes sin especificar sus clases concretas.
    Este patrón es particularmente útil cuando se necesita garantizar que los productos creados sean compatibles entre sí.

    En este ejemplo, hemos creado una interfaz de fábrica GUIFactory con métodos para crear botones y checkboxes. Las fábricas concretas, MacOSFactory y WindowsFactory,
    implementan esta interfaz para crear productos específicos (MacOSButton, WindowsButton, MacOSCheckbox, WindowsCheckbox) para cada plataforma.

    Al utilizar el patrón Abstract Factory, podemos cambiar fácilmente la familia de productos que se utiliza en nuestra aplicación cambiando la fábrica concreta,
    sin tener que modificar el código cliente que utiliza los productos.
    """
    print(explanation)
