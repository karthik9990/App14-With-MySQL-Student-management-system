import sys
from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit,
                             QPushButton, QComboBox)


class AverageCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance: ")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time (hours) : ")
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric(Km)', 'Imperial(M)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_time)

        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_time(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        speed = distance/time

        if self.unit_combo.currentText() == 'Metric(Km)':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.unit_combo.currentText() == 'Imperial(M)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        self.output_label.setText(f"Avergae Speed: {speed} {unit}")


app = QApplication(sys.argv)
age_calculator = AverageCalculator()
age_calculator.show()
sys.exit(app.exec())
