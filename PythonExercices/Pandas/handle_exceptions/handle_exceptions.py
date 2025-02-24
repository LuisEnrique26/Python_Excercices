result = None
numero_x = 10
numero_y = 2

try:
    numero_x = int(input("Ingresa un numero para x: "))
    numero_y = int(input("Ingresa un numero para y: "))
    result = numero_x / numero_y
    print(f"El resultado de la division es: {result}")
except ZeroDivisionError as e:
    print(f"La exepción es la siguiente: {e}")
except ValueError as e:
    print(f"La excepcion de ValueError es la siguiente: {e}")
except Exception as e:
    print(f"La excepcion de ValueError es la siguiente: {e}")
finally:
    print("\nEl programa ha finalizado")
