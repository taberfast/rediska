#Imports
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sip
from random import randint

#Variables
count = 0

#Lists
questions = [
    'Ты любишь дышать нейротоксином?',
    'Ты готов поставить на управление лаболаторией спроектированного дурака Уитли?',
    'У тебя есть портальная пушка?',
    'Вы насаживаете POTAToS на свою портальную пушку по выходным?',
    'Вам нравится находиться в консервации 999999999999 дней?',
    'Вам нравятся нажи тесты?',
    'Вы готовы проходить тесты до конца ваших дней',
    'Ваше имя Челл?',
    'Ты в оранжевом костюме?',
    'Вы довольны обслуживанием в нашем отделении пенсионного фонда России',
    'Вы довольны обслуживанием в нашем отделении Почты России',
    'Вас устраивает зарплата в 100 рублей(возможно белорусских)',
    'Вы живете по воле божьей?',
    'Большие города?',
    'Вы клуб предугадывающих шутки?',
    'че?',
    'Ваши родители работают в телефонной компании',
    'Вы фанат нинтендо свич? (ответишь да я тебя найду и твою сине-красную консоль выкину в окно)',
    'Готовы к тому то что вашу картофельную подругу захавает птица?',
    'Вам нужен пульт от ядерки?'
]

#Create and setup app
app = QApplication([])

#Widgets
text = QLabel('ВАС ПРИВЕТСТВУЕТ ПСИХОЛОГИЧЕСКИЙ ТЕСТ ОТ APERTURE SCIENCE')
button = QPushButton('да')

#Layouts
vlayout1 = QVBoxLayout()
vlayout1.addWidget(text, alignment = Qt.AlignCenter)
vlayout1.addWidget(button, alignment = Qt.AlignCenter)

#Create and setup windows
mw = QWidget()
mw.setWindowTitle('психологический тест')
mw.resize(512, 512)
mw.setLayout(vlayout1)

#Functions
def rediska(question, btntxt):
    global text
    global button
    global count
    global vlayout1
    if count == 19 :
        #mw.hide
        text.setText('ПОЗДРАВЛЯЕМ ВЫ НА ВСЕ 100% ГЛАВНЫЙ ПЕРСОНАЖ ИГРЫ "Far Cry New Dawn"!!!!!!!!')
        vlayout1.removeWidget(button)
        sip.delete(button)
    else:
        text.setText(question)
        button.setText(btntxt)
    count += 1
button.clicked.connect(lambda:rediska(questions[count], 'да'))


mw.show()
app.exec_()