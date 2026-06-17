Documentación Técnica del Software: Sistema de Formas Geométricas POO

Este documento contiene la especificación, los requerimientos, el diseño de arquitectura (UML), el código fuente completo y las instrucciones de ejecución para el sistema interactivo de dibujo de formas geométricas desarrollado en Python.

---

## 1. Descripcion del Software
Pequeño programa que utiliza la libreria turtle para dibujar formas geometricas en pantalla
### 1.1 Objetivo del Software
El objetivo principal de este software es proporcionar una herramienta educativa e interactiva que permita visualizar figuras geométricas (Círculos, Cuadrados y Triángulos) en una interfaz gráfica bidimensional. El sistema aplica los pilares fundamentales de la **Programación Orientada a Objetos (POO)** —como la herencia, el encapsulamiento y el polimorfismo— para calcular las dimensiones espaciales de cada figura de manera autónoma y renderizarlas dinámicamente según los parámetros proporcionados por el usuario.

### 1.2 Requerimientos Implementados

#### Requerimientos Funcionales (RF)
* **RF-01: Selección de Figura:** El sistema debe permitir al usuario seleccionar entre tres tipos de figuras geométricas: Círculo, Cuadrado y Triángulo Equilátero.
* **RF-02: Entrada de Dimensiones por Atributo Específico:** * Para el **Círculo**, el sistema debe solicitar el **área** como parámetro de entrada y calcular internamente el radio utilizando el valor matemático de $\pi$.
  * Para el **Cuadrado**, el sistema debe solicitar la longitud de un **lado**.
  * Para el **Triángulo**, el sistema debe solicitar la longitud de un **lado** (asumiendo un triángulo equilátero).
* **RF-03: Validación de Entradas:** El sistema debe validar que las dimensiones ingresadas por el usuario sean números estrictamente mayores que cero. En caso contrario, debe lanzar un error controlado.
* **RF-04: Renderizado Gráfico Dinámico:** El sistema debe abrir una ventana gráfica independiente y dibujar la figura seleccionada con el tamaño exacto calculado, utilizando colores distintivos para cada una.
* **RF-05: Centrado Relativo del Dibujo:** El cursor de dibujo (tortuga) debe reubicarse automáticamente antes de trazar la figura para asegurar que quede centrada en la pantalla.

#### Requerimientos No Funcionales (RNF)
* **RNF-01: Paradigma de Desarrollo:** El código debe estar diseñado bajo el paradigma de Programación Orientada a Objetos (POO), utilizando una clase base abstracta y clases hijas especializadas.
* **RNF-02: Portabilidad y Dependencias:** El software debe ejecutarse en cualquier sistema operativo con soporte para Python 3.x utilizando únicamente librerías estándar (`math` y `turtle`), eliminando la necesidad de instalar dependencias externas.
* **RNF-03: Robustez (Manejo de Errores):** El sistema debe capturar excepciones de tipo `ValueError` (por ejemplo, ingreso de texto en lugar de números o valores negativos) sin corromper la ejecución ni cerrarse inesperadamente.
* **RNF-04: Usabilidad de Interfaz:** La ventana de dibujo debe permanecer abierta de forma síncrona hasta que el usuario decida cerrarla mediante un clic explícito en la pantalla (`exitonclick`).

---

## 2. Artefactos UML

A continuación se presenta la estructura de clases del sistema representada mediante un modelo estructurado de texto y jerarquía de datos. El diseño evidencia el uso de **Polimorfismo**, donde la función de control interactúa exclusivamente con la interfaz de la clase base `Forma`.

```text
+-------------------------------------------------------------+
|                           Forma                             |
+-------------------------------------------------------------+
| - color: str                                                |
+-------------------------------------------------------------+
| + __init__(color: str)                                      |
| + dibujar(t: turtle.Turtle) [Abstracto]                     |
+-------------------------------------------------------------+
                               ^
                               |
        +----------------------+----------------------+
        |                      |                      |
+-----------------------+ +-----------------------+ +-----------------------+
|        Circulo        | |       Cuadrado        | |       Triangulo       |
+-----------------------+ +-----------------------+ +-----------------------+
| - radio: float        | | - lado: float         | | - lado: float         |
+-----------------------+ +-----------------------+ +-----------------------+
| + __init__(area, col) | | + __init__(lado, col) | | + __init__(lado, col) |
| + dibujar(t)          | | + dibujar(t)          | | + dibujar(t)          |
+-----------------------+ +-----------------------+ +-----------------------+

        +-----------------------------------------------------+
        |                 Modulo Principal                    |
        +-----------------------------------------------------+
        | + ejecutar_dibujo(figura: Forma)                    |
        | + main()                                            |
        +-----------------------------------------------------+
                               | (Instancia y envía)
                               v
                         [ Polimorfismo ]
