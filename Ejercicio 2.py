"""Construir un programa que muestre una ventana y que lea una clave secreta sin mostrar los caracteres que la componen."""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Clase para la ventana de confirmación con la clave ingresada
class ConfirmationWindow(QDialog):
    def __init__(self, password):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Clave Secreta Ingresada")
        self.setGeometry(150, 150, 400, 200)

        # Estilo de fondo con gradiente
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #FFAD60, stop: 1 #D95F59
                );
            }
        """)

        # Layout para la ventana de confirmación
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # Etiqueta con la clave secreta ingresada
        password_label = QLabel(f"Su clave secreta es: {password}")
        password_label.setFont(QFont("Verdana", 14, QFont.Bold))
        password_label.setStyleSheet("color: white;")
        password_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(password_label)

        # Establecemos el layout
        self.setLayout(layout)

# Clase principal para la ventana de ingreso de la clave secreta
class PasswordWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuramos el título y el tamaño de la ventana
        self.setWindowTitle("Clave Secreta ")
        self.setGeometry(100, 100, 450, 250)

        # Estilo de fondo con gradiente moderno
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #3A1C71, stop: 1 #D76D77, stop: 0.5 #D95F59
                );
            }
        """)  # Gradiente de colores de morado a rosado

        # Layout vertical para organizar los widgets
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 30, 40, 30)

        # Etiqueta descriptiva
        label = QLabel("Ingrese su clave secreta:", self)
        label.setFont(QFont("Helvetica Neue", 16, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: white;")
        layout.addWidget(label)

        # Campo de texto para ingresar la clave secreta
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar el texto ingresado
        self.password_input.setFont(QFont("Arial", 12))
        self.password_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #FFFFFF;
                border-radius: 15px;
                padding: 12px;
                background-color: rgba(255, 255, 255, 0.2);
                color: #FFFFFF;
                font-size: 14px;
            }
            QLineEdit:hover {
                background-color: rgba(255, 255, 255, 0.4);
            }
        """)
        layout.addWidget(self.password_input)

        # Botón para confirmar la clave
        submit_button = QPushButton("Confirmar", self)
        submit_button.setFont(QFont("Arial", 12, QFont.Bold))
        submit_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6F61;
                color: white;
                padding: 12px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #FF8861;
            }
        """)
        submit_button.clicked.connect(self.submit_password)  # Conectamos el botón con la función
        layout.addWidget(submit_button)

        # Establecemos el layout en la ventana principal
        self.setLayout(layout)

    # Función para mostrar la ventana de confirmación con la clave ingresada
    def submit_password(self):
        password = self.password_input.text()  # Obtener la clave secreta ingresada

        # Si el campo de contraseña no está vacío, mostramos la clave en una ventana personalizada
        if password:
            confirmation_window = ConfirmationWindow(password)
            confirmation_window.exec_()  # Mostrar la ventana de confirmación
        else:
            # Mostramos advertencia si no se ingresó ninguna clave
            QMessageBox.warning(self, "Error", "No ha ingresado ninguna clave.")

# Código principal para ejecutar la aplicación
if __name__ == '__main__':
    # Crear la aplicación
    app = QApplication(sys.argv)
    # Crear la ventana principal
    window = PasswordWindow()
    # Mostrar la ventana
    window.show()
    # Ejecutar el loop principal de eventos
    sys.exit(app.exec_())