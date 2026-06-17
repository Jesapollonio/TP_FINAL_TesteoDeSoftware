import math
import pytest
from unittest.mock import Mock, patch

# Asumimos que el código original está guardado en un archivo llamado 'figuras.py'
from figuras import Circulo, Cuadrado, Triangulo, Forma, ejecutar_dibujo


# ==============================================================================
# 1. PRUEBAS DE COMPONENTES (UNITARIAS)
# ==============================================================================

def test_cp_comp_01_despeje_radio_circulo():
    """CP-COMP-01: Verifica que el radio se calcule correctamente a partir del área."""
    area_prueba = 314.1592653589793
    circulo = Circulo(area_prueba)
    
    # El radio para un área de 314.159... debe ser exactamente 10
    assert pytest.approx(circulo.radio, rel=1e-3) == 10.0

@pytest.mark.parametrize("lado_invalido", [-5, 0, -0.01])
def test_cp_comp_02_validacion_limite_cuadrado(lado_invalido):
    """CP-COMP-02: Verifica que lados menores o iguales a cero lancen ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Cuadrado(lado_invalido)
    
    assert "El lado debe ser mayor que cero" in str(exc_info.value)

def test_cp_comp_03_validacion_limite_circulo_negativo():
    """Verifica que un área negativa lance ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Circulo(-10)
    assert "El área debe ser mayor que cero" in str(exc_info.value)


# ==============================================================================
# 2. PRUEBAS DE INTEGRACIÓN
# ==============================================================================

def test_cp_int_01_contrato_interfaz_y_polimorfismo():
    """
    CP-INT-01: Verifica que la función global acepte cualquier subclase de Forma
    y llame polimórficamente a su método .dibujar() usando un objeto simulado (Mock).
    """
    # Creamos un simulador (Mock) para el objeto de Turtle
    mock_turtle = Mock()
    
    # Instanciamos un triángulo real
    triangulo = Triangulo(lado=100)
    
    # Verificamos la herencia estructural (Integración de clases)
    assert isinstance(triangulo, Forma)
    
    # Ejecutamos el método dibujar pasándole el mock
    triangulo.dibujar(mock_turtle)
    
    # Verificamos que el triángulo interactuó correctamente con los comandos del motor
    assert mock_turtle.color.called
    assert mock_turtle.penup.called
    assert mock_turtle.pendown.called
    # Un triángulo equilátero avanza 3 veces
    assert mock_turtle.forward.call_count == 3
    assert mock_turtle.left.call_count == 3


# ==============================================================================
# 3. PRUEBAS DE CAJA NEGRA Y CAMINOS (LOGICA DE FLUJO)
# ==============================================================================

@patch('turtle.Screen')
@patch('turtle.Turtle')
def test_cp_ui_y_ejecucion_completa(mock_turtle_class, mock_screen_class):
    """
    CP-CN-01 / CP-UI-01: Prueba de integración con el módulo gráfico simulado.
    Garantiza que ejecutar_dibujo configure la pantalla y la tortuga sin fallos.
    """
    # Configurar los mocks para simular las clases de turtle
    mock_screen_instance = mock_screen_class.return_value
    mock_turtle_instance = mock_turtle_class.return_value
    
    cuadrado = Cuadrado(lado=150)
    
    # Ejecutamos la función que une la lógica con la interfaz gráfica
    ejecutar_dibujo(cuadrado)
    
    # Validamos requerimientos de interfaz (UI)
    mock_screen_instance.title.assert_called_with("Visualizador de Formas Geométricas - POO")
    mock_screen_instance.bgcolor.assert_called_with("#FAFAFA")
    mock_turtle_instance.speed.assert_called_with(3)
    mock_turtle_instance.pensize.assert_called_with(2)
    
    # Comprobamos que el cuadrado se haya dibujado (4 lados)
    assert mock_turtle_instance.forward.call_count == 4


# ==============================================================================
# 4. PRUEBAS DE RENDIMIENTO (PERFORMANCE)
# ==============================================================================

def test_cp_rend_01_escalas_masivas():
    """CP-REND-01: Evalúa el tiempo de respuesta ante entradas masivas."""
    import time
    
    area_gigante = 1000000000  # 1 mil millones
    
    inicio = time.perf_counter()
    circulo = Circulo(area_gigante)
    fin = time.perf_counter()
    
    tiempo_ejecucion = fin - inicio
    
    # El cálculo del radio debe ser casi instantáneo (menos de 5 milisegundos)
    assert tiempo_ejecucion < 0.005
    assert circulo.radio > 0
