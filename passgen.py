'''
PASSWORD GENERATOR
Описание кода:
1. Импортируем необходимые модули.
2. Создаем класс PasswordGenerator, который наследует от класса QWidget.
3. Определяем конструктор класса, в котором инициализируем окно приложения,
устанавливаем иконку, задаем размер окна и шрифт.
'''

import random
import string
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QIcon(QPixmap("icon.png")))
        self.setFixedSize(500, 250)

        font = QFont("Arial", 16)

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        label_length = QLabel("Password length:")
        label_length.setFont(font)
        self.lineedit_length = QLineEdit()
        self.lineedit_length.setFont(font)
        self.lineedit_length.setPlaceholderText("Enter password length")
        self.lineedit_length.setFixedWidth(200)
        hbox1.addWidget(label_length)
        hbox1.addWidget(self.lineedit_length)

        label_characters = QLabel("Character types:")
        label_characters.setFont(font)
        self.checkbox_lowercase = QPushButton("Lowercase")
        self.checkbox_lowercase.setCheckable(True)
        self.checkbox_lowercase.setChecked(True)
        self.checkbox_lowercase.setFont(font)
        self.checkbox_uppercase = QPushButton("Uppercase")
        self.checkbox_uppercase.setCheckable(True)
        self.checkbox_uppercase.setChecked(True)
        self.checkbox_uppercase.setFont(font)
        self.checkbox_digits = QPushButton("Digits")
        self.checkbox_digits.setCheckable(True)
        self.checkbox_digits.setChecked(True)
        self.checkbox_digits.setFont(font)
        self.checkbox_symbols = QPushButton("Symbols")
        self.checkbox_symbols.setCheckable(True)
        self.checkbox_symbols.setChecked(False)
        self.checkbox_symbols.setFont(font)
        hbox2.addWidget(label_characters)
        hbox2.addWidget(self.checkbox_lowercase)
        hbox2.addWidget(self.checkbox_uppercase)
        hbox2.addWidget(self.checkbox_digits)
        hbox2.addWidget(self.checkbox_symbols)

        self.label_password = QLabel()
        self.label_password.setFont(font)
        self.label_password.setAlignment(Qt.AlignCenter)
        hbox3.addWidget(self.label_password)

        button_generate = QPushButton("Generate")
        button_generate.setFont(font)
        button_generate.clicked.connect(self.generate_password)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(button_generate)
        self.setLayout(vbox)

    def generate_password(self):
        length = int(self.lineedit_length.text())

        characters = ""
        if self.checkbox_lowercase.isChecked():
            characters += string.ascii_lowercase
        if self.checkbox_uppercase.isChecked():
            characters += string.ascii_uppercase
        if self.checkbox_digits.isChecked():
            characters += string.digits
        if self.checkbox_symbols.isChecked():
            characters += string.punctuation

        if not characters:
            self.label_password.setText("Please select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.label_password.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())
