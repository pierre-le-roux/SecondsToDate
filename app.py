import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
)
from PySide6.QtCore import QDateTime
from datetime import datetime


class TimeCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.inputField = QLineEdit()
        self.inputField.setPlaceholderText("Enter date and time (YYYY-MM-DD HH:MM:SS)")
        layout.addWidget(self.inputField)

        self.calculateButton = QPushButton("Calculate Seconds")
        self.calculateButton.clicked.connect(self.calculateSeconds)
        layout.addWidget(self.calculateButton)

        self.resultLabel = QLabel("Seconds: ")
        layout.addWidget(self.resultLabel)

        self.setLayout(layout)
        self.setWindowTitle("Time Calculator")

    def calculateSeconds(self):
        input_text = self.inputField.text()
        try:
            input_datetime = datetime.strptime(input_text, "%Y-%m-%d %H:%M:%S")
            current_datetime = datetime.now()
            delta = input_datetime - current_datetime
            seconds = delta.total_seconds()
            self.resultLabel.setText(f"Seconds: {seconds}")
        except ValueError:
            self.resultLabel.setText("Invalid date format. Use YYYY-MM-DD HH:MM:SS")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeCalculator()
    window.show()
    sys.exit(app.exec())
