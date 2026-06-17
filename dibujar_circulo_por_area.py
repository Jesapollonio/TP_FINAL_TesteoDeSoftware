import math
import turtle


# --- Clase Base ---
class Forma:

    def __init__(self, color="blue"):
        self.color = color

    def dibujar(self, t):
        """Método abstracto que cada figura implementará"""
        pass


# --- Clase Círculo (Basado en el Área) ---
class Circulo(Forma):

    def __init__(self, area, color="blue"):
        super().__init__(color)
        if area <= 0:
            raise ValueError("El área debe ser mayor que cero.")
        # r = sqrt(Area / pi)
        self.radio = math.sqrt(area / math.pi)

    def dibujar(self, t):
        t.color(self.color)
        t.penup()
        t.goto(0, -self.radio)  # Centrar el círculo
        t.pendown()
        t.circle(self.radio)


# --- Clase Cuadrado (Basado en el Lado) ---
class Cuadrado(Forma):

    def __init__(self, lado, color="red"):
        super().__init__(color)
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero.")
        self.lado = lado

    def dibujar(self, t):
        t.color(self.color)
        t.penup()
        # Centrar el cuadrado aproximadamente
        t.goto(-self.lado / 2, -self.lado / 2)
        t.pendown()
        for _ in range(4):
            t.forward(self.lado)
            t.left(90)


# --- Clase Triángulo Equilátero (Basado en el Lado) ---
class Triangulo(Forma):

    def __init__(self, lado, color="green"):
        super().__init__(color)
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero.")
        self.lado = lado

    def dibujar(self, t):
        t.color(self.color)
        t.penup()
        # Centrar el triángulo aproximadamente
        t.goto(-self.lado / 2, -self.lado / 3)
        t.pendown()
        for _ in range(3):
            t.forward(self.lado)
            t.left(120)


# --- Función del Sistema de Dibujo ---
def ejecutar_dibujo(figura):
    """Esta función no necesita saber qué figura es,

    solo llama al método .dibujar() de la clase.
    """
    screen = turtle.Screen()
    screen.title("Dibujando Formas con POO")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)

    # Polimorfismo en acción: la figura sabe cómo dibujarse
    figura.dibujar(t)

    print("Haz clic en la ventana gráfica para cerrarla.")
    screen.exitonclick()


# --- Bloque Principal / Demostración ---
if __name__ == "__main__":
    print("Selecciona una figura para dibujar:")
    print("1. Círculo (definido por su Área)")
    print("2. Cuadrado (definido por su Lado)")
    print("3. Triángulo Equilátero (definido por su Lado)")

    opcion = input("Elige una opción (1-3): ")

    try:
        if opcion == "1":
            area = float(input("Introduce el área del círculo: "))
            objeto_forma = Circulo(area, color="purple")
        elif opcion == "2":
            lado = float(input("Introduce el lado del cuadrado: "))
            objeto_forma = Cuadrado(lado, color="crimson")
        elif opcion == "3":
            lado = float(input("Introduce el lado del triángulo: "))
            objeto_forma = Triangulo(lado, color="darkgreen")
        else:
            print("Opción no válida.")
            objeto_forma = None

        if objeto_forma:
            # Llamamos a la función unificada
            ejecutar_dibujo(objeto_forma)

    except ValueError as e:
        print(f"Error: {e}. Por favor introduce un número válido.")
