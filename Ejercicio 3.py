"""Construir un programa que muestre una ventana a través de la cual se pueda leer su número de cédula y 
su nombre completo"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Clase para la ventana de confirmación con los datos ingresados
class ConfirmationWindow(QDialog):
    def __init__(self, name, cedula):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle("Datos Ingresados")
        self.setGeometry(150, 150, 400, 200)
        
        # Estilo de fondo con gradiente para la ventana de confirmación
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #009688, stop: 1 #C68FE6
                );
            }
        """)

        # Layout para la ventana de confirmación
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # Etiqueta con los datos del nombre ingresado
        name_label = QLabel(f"Nombre: {name}")
        name_label.setFont(QFont("Verdana", 14, QFont.Bold))
        name_label.setStyleSheet("color: white;")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)

        # Etiqueta con los datos de la cédula ingresada
        cedula_label = QLabel(f"Cédula: {cedula}")
        cedula_label.setFont(QFont("Verdana", 14, QFont.Bold))
        cedula_label.setStyleSheet("color: white;")
        cedula_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(cedula_label)

        # Establecemos el layout
        self.setLayout(layout)

# Clase principal para la ventana de ingreso de datos
class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuramos el título y el tamaño de la ventana
        self.setWindowTitle("Información Personal")
        self.setGeometry(100, 100, 500, 300)

        # Estilo de fondo con gradiente moderno
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #4A148C, stop: 1 #CE93D8
                );
            }
        """)

        # Creamos un layout vertical para organizar los widgets
        layout = QVBoxLayout()
        layout.setSpacing(20)  # Espaciado entre elementos
        layout.setContentsMargins(40, 30, 40, 30)  # Márgenes internos

        # Etiqueta para el nombre completo
        name_label = QLabel("Nombre Completo:", self)
        name_label.setFont(QFont("Verdana", 14, QFont.Bold))  # Fuente estilizada
        name_label.setAlignment(Qt.AlignCenter)
        name_label.setStyleSheet("color: white;")
        layout.addWidget(name_label)

        # Campo de texto para el nombre completo
        self.name_input = QLineEdit(self)
        self.name_input.setFont(QFont("Arial", 12))
        self.name_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #FFFFFF;
                border-radius: 15px;
                padding: 10px;
                background-color: rgba(255, 255, 255, 0.2);
                color: #FFFFFF;
            }
        """)
        layout.addWidget(self.name_input)

        # Etiqueta para la cédula
        cedula_label = QLabel("Número de Cédula:", self)
        cedula_label.setFont(QFont("Verdana", 14, QFont.Bold))
        cedula_label.setAlignment(Qt.AlignCenter)
        cedula_label.setStyleSheet("color: white;")
        layout.addWidget(cedula_label)

        # Campo de texto para la cédula
        self.cedula_input = QLineEdit(self)
        self.cedula_input.setFont(QFont("Arial", 12))
        self.cedula_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #FFFFFF;
                border-radius: 15px;
                padding: 10px;
                background-color: rgba(255, 255, 255, 0.2);
                color: #FFFFFF;
            }
        """)
        layout.addWidget(self.cedula_input)

        # Botón para enviar la información
        submit_button = QPushButton("Enviar", self)
        submit_button.setFont(QFont("Arial", 12, QFont.Bold))
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #8E24AA;
                color: white;
                padding: 12px;
                border-radius: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #AB47BC;
            }
        """)
        submit_button.clicked.connect(self.submit_info)  # Conectamos el botón a la función
        layout.addWidget(submit_button)

        # Establecemos el layout en la ventana principal
        self.setLayout(layout)

    # Función para enviar la información
    def submit_info(self):
        name = self.name_input.text()  # Obtener el nombre ingresado
        cedula = self.cedula_input.text()  # Obtener la cédula ingresada

        # Si ambos campos están completos, mostramos la nueva ventana con la información
        if name and cedula:
            confirmation_window = ConfirmationWindow(name, cedula)
            confirmation_window.exec_()  # Mostrar la ventana de confirmación
        else:
            # Mostrar advertencia si algún campo está vacío
            QMessageBox.warning(self, "Error", "Debe completar ambos campos.")

# Código principal para ejecutar la aplicación
if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)
    # Crear la ventana
    window = PersonalInfoWindow()
    # Mostrar la ventana
    window.show()
    # Ejecutar el loop principal de eventos
    sys.exit(app.exec_())