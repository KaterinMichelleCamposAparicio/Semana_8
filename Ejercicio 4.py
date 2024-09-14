"""Construir un programa que muestre una ventana a través de la cual se pueda leer tres datos básicos de 3 mascotas
 diferentes"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QDialog
from PyQt5.QtCore import Qt

class PetsWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Datos de Mascotas")
        self.setGeometry(100, 100, 500, 400)  # Tamaño de la ventana

        # Configurar fondo morado pastel con degradado
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #D8BFD8, stop:1 #BA55D3
                );
            }
            QLabel {
                color: #4B0082;
                font-size: 14px;
                margin-bottom: 5px;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #E6E6FA;
                color: #4B0082;
                font-size: 12px;
                padding: 8px;
                border: 2px solid #4B0082;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            QPushButton {
                background-color: #8A2BE2;
                color: #ffffff;
                font-size: 14px;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #9370DB;
            }
        """)

        # Crear etiquetas y campos para las mascotas
        self.name_inputs = [QLineEdit() for _ in range(3)]
        self.age_inputs = [QLineEdit() for _ in range(3)]
        self.type_inputs = [QLineEdit() for _ in range(3)]

        # Añadir placeholders para los campos de entrada
        for i in range(3):
            self.name_inputs[i].setPlaceholderText("Nombre")
            self.age_inputs[i].setPlaceholderText("Edad")
            self.type_inputs[i].setPlaceholderText("Tipo (e.g., Perro)")

        # Botón para enviar la información
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_pets_info)

        # Layout principal
        main_layout = QVBoxLayout()

        # Organizar por columnas: Nombre | Edad | Tipo
        header_layout = QHBoxLayout()
        header_layout.addWidget(QLabel("Nombre"))
        header_layout.addWidget(QLabel("Edad"))
        header_layout.addWidget(QLabel("Tipo"))

        main_layout.addLayout(header_layout)

        # Agregar campos de cada mascota en una fila
        for i in range(3):
            pet_layout = QHBoxLayout()
            pet_layout.addWidget(self.name_inputs[i])
            pet_layout.addWidget(self.age_inputs[i])
            pet_layout.addWidget(self.type_inputs[i])

            main_layout.addLayout(pet_layout)

        # Añadir el botón al layout principal
        main_layout.addWidget(self.submit_button)

        # Establecer el layout principal a la ventana
        self.setLayout(main_layout)

    def show_pets_info(self):
        # Obtener la información ingresada y mostrarla en una nueva ventana
        pet_info_window = PetInfoDialog(self.name_inputs, self.age_inputs, self.type_inputs)
        pet_info_window.exec_()

class PetInfoDialog(QDialog):
    def __init__(self, name_inputs, age_inputs, type_inputs):
        super().__init__()

        # Configurar la ventana del diálogo
        self.setWindowTitle("Información de Mascotas")
        self.setGeometry(150, 150, 400, 300)

        # Estilos de la ventana
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #D8BFD8, stop:1 #BA55D3
                );
            }
            QLabel {
                color: #4B0082;
                font-size: 14px;
                margin-bottom: 5px;
                font-weight: bold;
            }
        """)

        # Layout para mostrar la información
        layout = QVBoxLayout()

        # Mostrar la información de las mascotas
        for i in range(3):
            name = name_inputs[i].text()
            age = age_inputs[i].text()
            pet_type = type_inputs[i].text()

            pet_info_label = QLabel(f"Mascota {i+1}: Nombre: {name}, Edad: {age}, Tipo: {pet_type}")
            layout.addWidget(pet_info_label)

        # Establecer el layout del diálogo
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PetsWindow()
    window.show()

    sys.exit(app.exec_())

