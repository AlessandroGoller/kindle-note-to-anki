import genanki
import os

import random


# C:\Users\aless\Downloads\Telegram Desktop\Come_funziona_la_musica_La_scienza_dei_suoni_bell_Notebook.html

title = ''
marx_char_title = 100
lista_note = []
id_model = 16061997 #''
id_deck = 116061997 #''
name_model = 'from_kindle_highlight'
col = ''

def main()-> None:
    global title, id_model
    title=''
    #id_model = random.randrange(1<<30, 1<<31)

    # Chiediamo all'utente di inserire il nome del file da analizzare
    filename = input('Inserisci il nome del file da analizzare: ')

    # Verifichiamo che il file sia un file html
    if os.path.splitext(filename)[1] in ['.html', '.htm']:
        # Analizziamo il testo del file
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            title=text.split('<div class="bookTitle">',1)[1].split('</div>',1)[0]
            if len(title)> marx_char_title:
                title=title[0:marx_char_title]
            analyze_text(text)
    else:
        print('Il file inserito non è un file HTML.')

def analyze_text(text: str) -> None:
    global title, col, id_deck

    # Creiamo il nuovo mazzo
    print(f"Il titolo è {title}")
    deck = genanki.Deck(id_deck, 'Books::'+title)

    n_times = text.count('noteText')
    for _i in range(n_times-1):
        # print(text)
        txt_to_add = text.split('noteHeading">',1)[1].split(' - ',1)[1].split('</div>',1)[0]
        txt_to_add += text.split('<div class="noteText">',1)[1].split('</div>',1)[0]
        insert_into_anki(deck, txt_to_add)
        text = text.split('<div class="noteText">',1)[1].split('</div>',1)[1]

    # Salviamo il deck
    genanki.Package(deck).write_to_file('books.apkg')

def insert_into_anki(deck, text) -> None:
    global col, lista_note, id_model, name_model
    
    my_model = genanki.Model(id_model,name_model,
        fields=[
            {'name': 'Text'}
        ],
        templates=[
            {
            'name': 'Card 1',
            'qfmt': '{{Text}}',
            'afmt': '{{FrontSide}} - ',
            },
        ])
    
    note = genanki.Note(
        model=my_model,
        fields=[text])
    # Aggiungiamo la nota al deck
    deck.add_note(note)

if __name__ == "__main__":
    main()