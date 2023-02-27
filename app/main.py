import genanki
import os

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

    # Ask the user to enter the name of the file to be analyzed
    filename = input('Inserisci il nome del file da analizzare: ')

    # Verify that the file is an html file
    if os.path.splitext(filename)[1] in ['.html', '.htm']:
        # Analyze the text of the file
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            title=text.split('<div class="bookTitle">',1)[1].split('</div>',1)[0]
            if len(title)> marx_char_title:
                title=title[0:marx_char_title]
            analyze_text(text)
    else:
        print('The file inserted is not a HTML file')

def analyze_text(text: str) -> None:
    global title, col, id_deck

    # Create the new deck
    print(f"Il titolo è {title}")
    deck = genanki.Deck(id_deck, 'Books::'+title)

    n_times = text.count('noteText')
    for _ in range(n_times-1):
        txt_to_add = text.split('noteHeading">',1)[1].split(' - ',1)[1].split('</div>',1)[0]
        txt_to_add += text.split('<div class="noteText">',1)[1].split('</div>',1)[0]
        insert_into_anki(deck, txt_to_add)
        text = text.split('<div class="noteText">',1)[1].split('</div>',1)[1]

    # Save the deck
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
    # Aadd note to the deck
    deck.add_note(note)

if __name__ == "__main__":
    main()