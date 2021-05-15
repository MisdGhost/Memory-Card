#!/usr/bin/python
# -*- coding: utf8 -*-
#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QPushButton, QRadioButton, QWidget, QGroupBox, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from random import shuffle

Ap = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

gl = QLabel("Какой национальности не существует?")
pl = QGroupBox('Варианты ответов')
pl2 = QGroupBox('Результаты теста')
pl2.hide()
o1 = QRadioButton('Энцы')
o2 = QRadioButton('Смурфы')
o3 = QRadioButton('Чулымцы')
o4 = QRadioButton('Алеуты')
knopka = QPushButton('Ответить')
gl2 = QLabel("Правильно/Неправильно")
gl3 = QLabel("Правильный ответ")

RadioGroup = QButtonGroup()
RadioGroup.addButton(o1)
RadioGroup.addButton(o2)
RadioGroup.addButton(o3)
RadioGroup.addButton(o4)

l1 = QHBoxLayout()
l2 = QHBoxLayout()
l4 = QHBoxLayout()
l3 = QVBoxLayout()

#pl
l5_group = QVBoxLayout()
l6_group = QHBoxLayout()
l7_group = QVBoxLayout()

#pl2
l8_group = QHBoxLayout()
l9_group = QVBoxLayout()
l10_group = QHBoxLayout()

l4.addStretch(1)
l4.addWidget(knopka, stretch = 3)
l4.addStretch(1)
l2.addWidget(pl)
l2.addWidget(pl2)
l1.addStretch(1)
l1.addWidget(gl, stretch = 3)
l1.addStretch(1)

#pl
l5_group.addWidget(o1)
l5_group.addWidget(o3)
l7_group.addWidget(o2)
l7_group.addWidget(o4)

#pl2
l8_group.addWidget(gl2)
l10_group.addWidget(gl3, alignment = Qt.AlignCenter)


l3.addLayout(l1)
l3.addSpacing(10)
l3.addLayout(l2)
l3.addSpacing(10)
l3.addLayout(l4)
l3.addSpacing(10)

#pl
l6_group.addLayout(l5_group)
l6_group.addLayout(l7_group)
pl.setLayout(l6_group)

#pl2
l9_group.addLayout(l8_group)
l9_group.addLayout(l10_group)
pl2.setLayout(l9_group)

def show_result():
    gl.show()
    gl3.show()
    knopka.setText("Следующий вопрос")
    pl.hide()
    pl2.show()
    

def show_question():
    gl3.hide()
    gl.show()
    knopka.setText("Ответить")
    pl.show()
    pl2.hide()
    RadioGroup.setExclusive(False)
    o1.setChecked(False)
    o2.setChecked(False)
    o3.setChecked(False)
    o4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [o1, o2, o3, o4]
def start_test():
    if knopka.text() == 'Ответить':
        show_result()
    else:
        show_question()
def ask(question, right_answer, wrong1, wrong2,wrong3):
    shuffle(answers)

def check_answer():
    if answer[0].isChecked() == True:
        res = True
        show_correct(res)
    else:
        res = False
        show_correct(res)
def show_correct(res):
    if res == True:
        gl3.setText(right_answer)
        gl2.setText("Правильно")
    else:
        gl3.setText()
knopka.clicked.connect(start_test)

main_win.setLayout(l3)
main_win.show()
Ap.exec()