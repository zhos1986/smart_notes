from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json


notes = {
    'Название заметки':
{
    'текст' : 'очень важный текст заметки',
    'теги' : ['черновик', 'мысли']
    }
}

with  open('f.json', 'w') as file:
    json.dump(notes, file)


app = QApplication([])
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])


def show_note(): #показывает выбранную заметку:)
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])

def save_note(): #сохраняет заметку('/_;)
    if list_notes.selectedItems():  
        text = field_text.toPlainText()
        name_1 = list_notes.selectedItems()[0].text()
        notes[name_1]['текст'] = text
        with  open('f.json', 'w') as file:
            json.dump(notes, file)

def del_note(): # удаляет выбранную заметку(;
    if list_notes.selectedItems():
        name = list_notes.selectedItems()[0].text()
        del notes[name]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file)


def add_tag(): #добавляет тег к заметке'_'
    if list_notes.selectedItems():
        tag = field_tag.text()
        name = list_notes.selectedItems()[0].text()
        if tag != '' and tag not in notes[name]['теги']:
            notes[name]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file)


def del_tag(): #убирает выбранный тег у заметки(!_!)
    if list_notes.selectedItems() and list_tags.selectedItems():
        tag = list_tags.selectedItems()[0].text()
        name = list_notes.selectedItems()[0].text()
        notes[name]['теги'].remove(tag)
        list_tags.takeItem(list_tags.row(list_tags.selectedItems()[0]))
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file)


def search_tag(): # ищет заметки по тегу (возвращает весь список)))("...")
    tag = field_tag.text()
    if tag != '':
        list_notes.clear()
        for note in notes:
            if tag in notes[note]['теги']:
                list_notes.addItem(note)
    else:
        list_notes.clear()
        list_notes.addItems(notes)





'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(1100, 800)


#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')



#появляется окно с полем "Введите имя заметки"
button_note_create = QPushButton('Создать заметку') 
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')
    #расположение виджетов по лэйаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
#запуск приложения 

with open('f.json', 'r') as file:
    notes = json.load(file)
    list_notes.addItems(notes)

list_notes.itemClicked.connect(show_note)
button_note_create.clicked.connect(add_note)
button_note_del.clicked.connect(del_note)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)

notes_win.show()
app.exec_()