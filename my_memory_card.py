#создай приложение для запоминания информации
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,  QPushButton, QLabel, QButtonGroup)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question1 = Question('Что?', 'Ничего', 'Норм', 'Найс', 'Хорошо')
question_list.append(question1)
question2 = Question('Ты кто?', 'чел', 'Человек', 'Животное', 'Инапланитянен')
question_list.append(question2)
question3 = Question('Ку', 'Здравствуй', 'Куку', 'Че?', 'Прив')
question_list.append(question3)


app = QApplication([])
window = QWidget()

window.setWindowTitle('MemoCard')
window.move(0,0)
window.resize(400,300)

lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
qrbutton1 = QRadioButton('Вариант 1')
qrbutton2 = QRadioButton('Вариант 2')
qrbutton3 = QRadioButton('Вариант 3')
qrbutton4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(qrbutton1)
layout_ans2.addWidget(qrbutton2)
layout_ans3.addWidget(qrbutton3)
layout_ans3.addWidget(qrbutton4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('ты прав или нет')
lb_correct = QLabel('ответ будет тут')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)
AnsGroupBox.setLayout(layout_res)

button_ok = QPushButton('Ответить')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addWidget(button_ok)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)

window.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button_ok.setText('Следующий вопрос')
    print('Процент правильных ответов', score/asked_questions * 100)


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button_ok.setText('Ответить')
    button_group = QButtonGroup()

    button_group.addButton(qrbutton1)
    button_group.addButton(qrbutton2)
    button_group.addButton(qrbutton3)
    button_group.addButton(qrbutton4)

    button_group.setExclusive(False)
    qrbutton1.setChecked(False)
    qrbutton1.setChecked(False)
    qrbutton3.setChecked(False)
    qrbutton4.setChecked(False)
    button_group.setExclusive(True)

answers = [qrbutton1,qrbutton2,qrbutton3,qrbutton4]

def ask():
    global asked_questions
    asked_questions += 1

    shuffle(question_list)
    ask_question =  question_list[0]

    shuffle(answers)
    answers[0].setText(ask_question.right_answer)
    answers[1].setText(ask_question.wrong1)  
    answers[2].setText(ask_question.wrong2)
    answers[3].setText(ask_question.wrong3)

    lb_result.setText(ask_question.question)
    lb_correct.setText(ask_question.right_answer)

    show_question()

def check_answer():
    if answers[0].isChecked():
        global score
        score += 1

        lb_result.setText('Правильно')
        show_result()

    if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        lb_result.setText('Неверно')
        show_result()

def click_ok():
    if button_ok.text() == 'Ответить':
        check_answer()

    else:
        ask()

score = 0
asked_questions = 0


button_ok.clicked.connect(click_ok)

ask()
window.show()
app.exec_()


