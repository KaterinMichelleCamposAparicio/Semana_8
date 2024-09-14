"""Este programa es una aplicación gráfica desarrollada con PyQt5 que implementa un formulario simple en el que el
 usuario puede ingresar su género y edad. Luego, al enviar los datos, se muestra una ventana con los resultados 
 ingresados. A continuación, se ofrece una explicación detallada de lo que hace el programa y el problema que resuelve:

Objetivo del programa:
El programa tiene como objetivo proporcionar una interfaz gráfica fácil de usar para recopilar la información de género
 y edad de un usuario, permitiéndole seleccionar entre varios géneros y edades dentro de un rango. Luego, muestra los
datos ingresados en una nueva ventana de confirmación. El diseño está estilizado con colores y fuentes 
personalizados para ofrecer una experiencia visual atractiva.

Estructura del programa:

Ventana principal (SuperStylishApp):
La ventana principal contiene los elementos del formulario, como botones de opción (radio buttons) para seleccionar el 
género, un selector de edad (QSpinBox), y un botón para enviar los datos.
El formulario incluye tres géneros predefinidos: "Masculino", "Femenino" y "Otro".
El selector de edad permite seleccionar una edad en un rango de 0 a 120 años.

Estilización personalizada:
El programa aplica estilos visuales personalizados usando hojas de estilo (CSS-like). Esto incluye la configuración de colores para 
el fondo, botones, y etiquetas, así como el uso de fuentes modernas como Arial.
Los elementos tienen bordes redondeados, efectos hover, y esquemas de colores basados en tonos rosados y rojos.

Recopilación de datos:
Al hacer clic en el botón "Enviar", el programa recopila el género y la edad ingresados. Si el usuario no selecciona un género, el 
programa muestra un cuadro de diálogo de advertencia indicando que debe seleccionar uno.
Si los datos son válidos, abre una nueva ventana que muestra los datos ingresados.

Ventana de resultados (ResultWindow):
Cuando se recopilan los datos correctamente, se abre una nueva ventana que muestra el género y la edad seleccionados. Esta ventana también
está estilizada de manera similar a la ventana principal, con una estética suave y moderna.

Validación de entrada:
El programa incluye una validación mínima: no permite enviar el formulario si el usuario no ha seleccionado un género. Sin embargo, 
no valida otros posibles errores, como el ingreso de edades inválidas, ya que el rango del SpinBox ya limita los valores permitidos 
(0-120).

¿Qué problema resuelve el programa?
El programa aborda el problema de ofrecer una interfaz simple y atractiva para que los usuarios ingresen información básica, como su 
género y edad. En muchos casos, las aplicaciones necesitan recolectar este tipo de información para personalizar la experiencia del 
usuario o para obtener datos básicos en formularios de registro. Este programa facilita el ingreso de datos de manera interactiva y 
elegante, asegurando que los usuarios completen los campos esenciales antes de proceder.

Ventajas de esta solución:
Facilidad de uso: El formulario es intuitivo y solo requiere hacer clic en los botones de opción y ajustar un selector de números. 
Esto es adecuado para usuarios con poca experiencia técnica.

Validación mínima: El programa evita errores comunes al requerir la selección de un género antes de enviar los datos, lo cual garantiza
que se ingrese la información necesaria.

Estética atractiva: Los estilos personalizados mejoran la experiencia del usuario al proporcionar una interfaz más agradable visualmente,
lo que puede aumentar la satisfacción del usuario y la eficiencia en la recolección de datos.

Extensibilidad: El código es modular y podría ampliarse fácilmente para incluir más campos o validaciones, como la entrada de nombre o
dirección, o incluir más opciones de género.

Este tipo de aplicaciones podría utilizarse en un entorno más amplio, como parte de un sistema de encuestas, formularios de registro en 
línea, o incluso aplicaciones móviles y web que requieran la recolección de datos de usuario."""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QSpinBox, QPushButton, QVBoxLayout, QMessageBox, QDialog
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt

# Clase principal de la aplicación
class SuperStylishApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configura la ventana principal
        self.setWindowTitle('Formulario')  # Título de la ventana
        self.setGeometry(100, 100, 400, 300)  # Posición y tamaño de la ventana
        self.setup_ui()  # Llamada para configurar los widgets
        self.apply_styles()  # Llamada para aplicar los estilos personalizados

    # Método que configura los widgets en la ventana
    def setup_ui(self):
        # Etiqueta para la selección de género
        self.gender_label = QLabel('Selecciona tu género:')
        self.gender_label.setFont(QFont('Arial', 14, QFont.Bold))  # Cambia la fuente de la etiqueta

        # Botones de opción para seleccionar el género
        self.male_radio = QRadioButton('Masculino')
        self.female_radio = QRadioButton('Femenino')
        self.other_radio = QRadioButton('Otro')

        # Etiqueta para la selección de edad
        self.age_label = QLabel('Edad:')
        self.age_label.setFont(QFont('Arial', 14, QFont.Bold))  # Cambia la fuente de la etiqueta

        # SpinBox para seleccionar la edad (de 0 a 120 años)
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setRange(0, 120)  # Rango de la edad
        # Aplicación de estilos al SpinBox
        self.age_spinbox.setStyleSheet("""
            QSpinBox {
                padding: 10px;
                border-radius: 15px;
                background-color: #ffe6e6;
                font-size: 18px;
                border: 2px solid #ff9999;
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 20px;
                border-radius: 10px;
                background-color: #ffcccc;
            }
        """)

        # Botón de enviar datos
        self.submit_button = QPushButton('Enviar')
        self.submit_button.clicked.connect(self.submit_data)  # Conecta el botón al método que procesa los datos

        # Layout para los botones de opción (género)
        gender_layout = QVBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_layout.addWidget(self.other_radio)

        # Layout principal que organiza todos los widgets en la ventana
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.gender_label)
        main_layout.addLayout(gender_layout)
        main_layout.addWidget(self.age_label)
        main_layout.addWidget(self.age_spinbox)
        main_layout.addWidget(self.submit_button)

        self.setLayout(main_layout)  # Asigna el layout a la ventana

    # Método que aplica los estilos personalizados
    def apply_styles(self):
        # Cambia la paleta de colores de la ventana
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 240, 240))  # Fondo rosado suave
        palette.setColor(QPalette.Button, QColor(255, 128, 128))  # Botones rosados
        palette.setColor(QPalette.ButtonText, Qt.white)  # Texto de los botones en blanco
        palette.setColor(QPalette.WindowText, QColor(102, 0, 0))  # Texto oscuro
        self.setPalette(palette)

        # Aplicación de estilos a las etiquetas
        self.gender_label.setStyleSheet("font-size: 18px; color: #660000; padding: 10px;")
        self.age_label.setStyleSheet("font-size: 18px; color: #660000; padding: 10px;")

        # Estilos para los botones de opción (radio buttons) con efectos hover
        self.male_radio.setStyleSheet("""
            QRadioButton {
                color: #660000;
                font-size: 16px;
                padding: 8px;
                border-radius: 10px;
                background-color: #ffe6e6;
            }
            QRadioButton::hover {
                background-color: #ffcccc;
            }
        """)
        self.female_radio.setStyleSheet("""
            QRadioButton {
                color: #660000;
                font-size: 16px;
                padding: 8px;
                border-radius: 10px;
                background-color: #ffe6e6;
            }
            QRadioButton::hover {
                background-color: #ffcccc;
            }
        """)
        self.other_radio.setStyleSheet("""
            QRadioButton {
                color: #660000;
                font-size: 16px;
                padding: 8px;
                border-radius: 10px;
                background-color: #ffe6e6;
            }
            QRadioButton::hover {
                background-color: #ffcccc;
            }
        """)

        # Estilos para el botón de enviar
        self.submit_button.setStyleSheet("""
            QPushButton {
                background-color: #ff4d4d;
                border-radius: 20px;
                padding: 15px;
                font-size: 18px;
                font-weight: bold;
                color: white;
            }
            QPushButton:hover {
                background-color: #ff6666;
            }
        """)

    # Método que se llama cuando se presiona el botón "Enviar"
    def submit_data(self):
        # Captura el género seleccionado
        gender = ''
        if self.male_radio.isChecked():
            gender = 'Masculino'
        elif self.female_radio.isChecked():
            gender = 'Femenino'
        elif self.other_radio.isChecked():
            gender = 'Otro'

        # Captura la edad seleccionada
        age = self.age_spinbox.value()

        # Si se selecciona un género, abre la ventana de resultados
        if gender:
            result_window = ResultWindow(gender, age)
            result_window.exec_()  # Muestra la ventana de resultados
        else:
            # Si no se selecciona ningún género, muestra una advertencia
            QMessageBox.warning(self, 'Error', 'Por favor selecciona un género.')

# Ventana de resultados que muestra los datos ingresados
class ResultWindow(QDialog):
    def __init__(self, gender, age):
        super().__init__()
        
        # Configura la ventana de resultados
        self.setWindowTitle('Datos Enviados')  # Título de la ventana
        self.setGeometry(150, 150, 300, 200)  # Tamaño y posición
        self.setup_ui(gender, age)  # Configura los widgets
        self.apply_styles()  # Aplica estilos personalizados

    # Método que configura los widgets en la ventana de resultados
    def setup_ui(self, gender, age):
        # Etiqueta que muestra los datos (género y edad)
        self.result_label = QLabel(f'Género: {gender}\nEdad: {age}')
        self.result_label.setFont(QFont('Arial', 14, QFont.Bold))  # Cambia la fuente de la etiqueta

        # Layout para organizar los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        self.setLayout(layout)  # Asigna el layout a la ventana

    # Método que aplica estilos personalizados a la ventana de resultados
    def apply_styles(self):
        # Estilo similar a la ventana principal
        self.setStyleSheet("""
            QWidget {
                background-color: #ffe6e6;
                font-family: 'Arial', sans-serif;
            }
            QLabel {
                font-size: 18px;
                color: #660000;  # Texto oscuro
                padding: 10px;
            }
        """)

# Entrada principal de la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)  # Crea la aplicación
    window = SuperStylishApp()  # Crea la ventana principal
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el ciclo de eventos

