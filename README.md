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

# Plan de Pruebas: Sistema de Formas Geométricas POO

Este documento define la estrategia, el alcance, los criterios de aceptación y el cronograma para las actividades de verificación y validación del Sistema de Formas Geométricas basado en Programación Orientada a Objetos.

---

## 3. Alcance de las Pruebas

### 2.1 Elementos que SE probarán (En Alcance)
* **Lógica Matemática:** Validaciones de entrada (números negativos/cero) y fórmulas de conversión (despeje del radio a partir de $\pi$).
* **Estructura y Arquitectura:** Correcta implementación de la herencia y comportamiento polimórfico de las subclases (`Circulo`, `Cuadrado`, `Triangulo`) al interactuar con la clase base `Forma`.
* **Componente Gráfico (UI):** Inicialización de la ventana de `turtle`, propiedades del lienzo (colores, título, grosores) y persistencia del dibujo.
* **Flujos de Control:** Manejo de excepciones ante entradas tipográficas incorrectas y caminos lógicos del menú principal.

### 3.2 Elementos que NO se probarán (Fuera de Alcance)
* Rendimiento del hardware o de la tarjeta de video del usuario al renderizar gráficos de gran escala.
* Compatibilidad con versiones obsoletas de Python (versiones anteriores a la 3.8).

---

## 4. Estrategia y Enfoque de Pruebas

El proceso de verificación seguirá un enfoque piramidal (de lo micro a lo macro), automatizando las pruebas lógicas y ejecutando de forma manual/guiada los aspectos puramente visuales de la interfaz.

### 4.1 Niveles de Prueba Aplicados
1. **Pruebas de Componentes (Unitarias):** Automatizadas con `pytest`. Se enfocan en el aislamiento total de los constructores de clase y la verificación de fórmulas.
2. **Pruebas de Integración:** Se evalúa la fusión de la lógica orientada a objetos con las llamadas de la API de `turtle`, utilizando objetos simulados (*Mocks*).
3. **Pruebas de Sistema / Caja Negra:** Verificación del flujo completo de la aplicación (Consola $\rightarrow$ Procesamiento $\rightarrow$ Interfaz Gráfica).

---

## 5. Criterios de Entrada y Salida

### 5.1 Criterios de Entrada (¿Cuándo empezamos?)
* El código fuente de `figuras.py` debe estar completo, sin errores de sintaxis y listo para ejecución.
* El entorno de desarrollo debe contar con Python 3.8+ y la librería `pytest` instalada.
* El set de pruebas de automatización (`test_figuras.py`) debe estar estructurado y sin errores previos.

### 5.2 Criterios de Salida (¿Cuándo terminamos?)
* El **100%** de las pruebas unitarias e integradas en `pytest` deben ejecutarse con estado exitoso (*Passed*).
* Se debe lograr una cobertura de caminos de control (cobertura de ramas) del **100%** en la captura de errores de entrada.
* Cero (0) defectos críticos abiertos (como bloqueos inexplicables de la interfaz o cálculos matemáticos erróneos).

---

## 6. Matriz de Cronograma y Responsabilidades

Para un desarrollo ágil de este software, las actividades se planifican en un ciclo corto de 4 pasos fundamentales:

| Fase | Actividad | Responsable | Entregable | Tiempo Estimado |
| :--- | :--- | :--- | :--- | :--- |
| **1. Diseño** | Definición de escenarios de prueba y preparación del script `test_figuras.py`. | Analista de QA / Desarrollador | Script de prueba base. | 2 horas |
| **2. Ejecución Automatizada** | Corrida del comando `pytest -v` para evaluar componentes, caminos e integración. | Desarrollador | Reporte de consola de Pytest. | 5 minutos |
| **3. Ejecución Manual** | Pruebas de interfaz (UI), persistencia del lienzo gráfico y clics de cierre. | Tester de QA | Matriz de aceptación visual. | 1 hora |
| **4. Cierre** | Documentación de resultados y liberación del software. | Líder de Proyecto | Reporte final de calidad. | 30 minutos |

---

## 6. Entorno de Pruebas (Test Environment)

Para asegurar la repetibilidad de las pruebas, se define el siguiente entorno controlado:
* **Sistema Operativo:** Windows 10/11, macOS o Linux (Entorno de escritorio para soportar interfaces tipo GUI).
* **Lenguaje:** Python 3.8 o superior (con las librerías nativas `math` y `turtle`).
* **Herramienta de Automatización:** `pytest` (última versión estable).
* **Terminal:** Consola de comandos del sistema operativo (Bash, PowerShell o CMD).

---

## 7. Criterios de Suspensión y Reanudación

* **Criterio de Suspensión:** Las pruebas se detendrán inmediatamente si el módulo `turtle` falla al inicializar en el sistema operativo del entorno de pruebas de forma consistente (falla de entorno gráfico), o si se detecta un error de desbordamiento de memoria que congele el equipo.
* **Criterio de Reanudación:** Las pruebas se retomarán una vez que el desarrollador aplique un parche correctivo para el bloqueo o se reconfigure el soporte gráfico de la máquina de pruebas.
