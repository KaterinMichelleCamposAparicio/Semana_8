"""Construir un programa que muestre una ventana en la cual aparezca su nombre completo y su edad centrados."""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QFont

class GradientWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Perfil Personal")
        self.setGeometry(100, 100, 400, 250)
        
        # Estilo de fondo con gradiente
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #6A5ACD, stop: 1 #9370DB
                );
            }
        """)
        
        # Layout principal
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Etiquetas con estilo elegante
        name_label = QLabel("Nombre completo: Katerin Michelle Campos Aparicio", self)
        age_label = QLabel("Edad: 20 años", self)
        
        # Fuente moderna
        font = QFont("Verdana", 16, QFont.Bold)
        name_label.setFont(font)
        age_label.setFont(font)
        
        # Colores y sombra en las etiquetas
        name_label.setStyleSheet("""
            color: #FFFFFF;
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 10px;
        """)
        age_label.setStyleSheet("""
            color: #FFFFFF;
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 10px;
        """)
        
        # Centrar las etiquetas
        name_label.setAlignment(Qt.AlignCenter)
        age_label.setAlignment(Qt.AlignCenter)
        
        # Añadir widgets al layout
        layout.addWidget(name_label)
        layout.addWidget(age_label)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GradientWindow()
    window.show()
    sys.exit(app.exec_())
