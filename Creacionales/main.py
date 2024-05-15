import os
import AbstractFactory
import Builder

def clear_console():
    # Clear the console based on the operating system
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/MacOS

def display_creation_patterns():
    print("Seleccione el patrón de diseño creacional que desea conocer:")
    print("1. Abstract Factory")
    print("2. Builder")
    
    choice = input("Ingrese el número de su elección: ")

    if choice == '1':
        print("Ha seleccionado Abstract Factory")
        print("Seleccione la plataforma:")
        print("1. Windows")
        print("2. MacOS")
        
        platform_choice = input("Ingrese el número de su elección: ")
        
        if platform_choice == '1':
            AbstractFactory.run('windows')
        elif platform_choice == '2':
            AbstractFactory.run('mac')
        else:
            print("Elección no válida")
    
    elif choice == '2':
        print("Ha seleccionado Builder")
        Builder.run()
    
    else:
        print("Elección no válida")

def main():
    clear_console()
    
    print("Bienvenido al programa de demostración de patrones de diseño de software")
    print("Seleccione la categoría de patrones de diseño que desea conocer:")
    print("1. Patrones de Creación")
    print("2. Patrones Estructurales")
    print("3. Patrones de Comportamiento")
    
    choice = input("Ingrese el número de su elección: ")

    if choice == '1':
        clear_console()
        display_creation_patterns()
    elif choice == '2':
        print("Patrones Estructurales - Esta sección se implementará en el futuro.")
    elif choice == '3':
        print("Patrones de Comportamiento - Esta sección se implementará en el futuro.")
    else:
        print("Elección no válida")

if __name__ == "__main__":
    main()
