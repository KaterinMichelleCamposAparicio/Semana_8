"""Construir un programa que muestre una ventana a través de la cual se puedan leer 10 datos característicos de
 una persona"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, QDialog
from PyQt5.QtCore import Qt

class PersonDataWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar la ventana
        self.setWindowTitle("Datos de Persona")
        self.setGeometry(100, 100, 400, 500)  # Tamaño de la ventana

        # Configurar fondo celeste con degradado
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #E0FFFF, stop:1 #00BFFF
                );
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QLabel {
                font-size: 16px;
                color: #004080;
                margin-right: 10px;
            }
            QLineEdit {
                font-size: 14px;
                padding: 10px;
                border: 2px solid #004080;
                border-radius: 12px;
                background-color: #FFFFFF;
                color: #004080;
                margin-bottom: 15px;
            }
            QPushButton {
                background-color: #00BFFF;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border: none;
                border-radius: 12px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #1E90FF;
            }
        """)

        # Crear etiquetas y campos de entrada
        self.labels = ["Nombre", "Edad", "Dirección", "Teléfono", "Correo Electrónico",
                       "Fecha de Nacimiento", "Género", "Nacionalidad", "Ocupación", "Estado Civil"]
        self.inputs = [QLineEdit() for _ in range(10)]

        # Crear un layout para la entrada de datos
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)  # Alineación de etiquetas

        # Añadir etiquetas y campos de entrada al layout
        for label, input_field in zip(self.labels, self.inputs):
            form_layout.addRow(QLabel(label), input_field)

        # Botón para enviar la información
        self.submit_button = QPushButton("Enviar")
        self.submit_button.clicked.connect(self.show_person_data)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.submit_button, alignment=Qt.AlignCenter)  # Centrar el botón

        # Establecer el layout principal a la ventana
        self.setLayout(main_layout)

    def show_person_data(self):
        # Crear y mostrar la ventana de resultados
        result_window = ResultWindow(self.labels, self.inputs)
        result_window.exec_()

class ResultWindow(QDialog):
    def __init__(self, labels, inputs):
        super().__init__()

        # Configurar la ventana del diálogo
        self.setWindowTitle("Información de Persona")
        self.setGeometry(150, 150, 400, 500)  # Tamaño de la ventana

        # Configurar fondo celeste con degradado
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #E0FFFF, stop:1 #00BFFF
                );
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QLabel {
                font-size: 16px;
                color: #004080;
                margin-bottom: 10px;
            }
        """)

        # Layout para mostrar la información
        layout = QVBoxLayout()

        # Mostrar la información de la persona
        for label, input_field in zip(labels, inputs):
            data_label = QLabel(f"{label}: {input_field.text()}")
            layout.addWidget(data_label)

        # Establecer el layout del diálogo
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = PersonDataWindow()
    window.show()

    sys.exit(app.exec_())
