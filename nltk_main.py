
from nltk.corpus import stopwords, wordnet
from nltk import FreqDist,sent_tokenize, word_tokenize
import json
from speech_part import return_speech_part_information
from tokenize_training import training

class Text_Statistics:
    # metoda przyjmujaca tekst i liczbe slow do wyswietlenia i
    #  zwracajaca najpopularniejsze slowa i ich licznosc
    def word_frequency_list(text, number, stopwords):
        # wyswietla f najpopularniejszych slow w tekscie
        if stopwords is True:
            stop_words = set(stopwords.words("english"))
            res = [w for w in text if w not in stop_words]
        elif stopwords is False:
            res = [w for w in text]
        f = FreqDist(res)
        return f.most_common(number)

    # wyswietla wyrazy z ciagiem znakow podanym w characters
    def search_words_with_characters(text, characters):
        return [w for w in set(text) if characters in w]




class Model:
    def __init__(self):
        self.syn_list = []
    # metoda przyjmuje slowo i zwraca jego  synonimy
    def Add_Synonyms(self, word):
        if word[-1] == '.':
            word = word[0:-1]

        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                self.syn_list.append(l.name())

        self.syn_list =  list(set(self.syn_list))

        return self.syn_list





# funkcja odpowiadajaca za znalezienie kliknietego slowa i zdania w akapicie
# przyjmujaca jako cursor_position pozycje kursora w edytorze oraz tekst (akapit)
#i zwracajaca klikniete slowo i klikniete zdanie
def click_event_processing(cursor_position, text):
    cursor_position = int(cursor_position)
    text = str(text)
    l = text.split()
    if cursor_position >= len(text):
        return['','']
    #jesli akapit jest pusty zwraca klikniete slowo i zdanie jako empty
    elif len(text)==0:
        return['empty','empty']
    else:
        word_counter = 0
        # length_of_line_to_clicked_word to zmienna zwiekszana do czasu
        # az nie bedzie rowna lub wieksza od cursor_position
        length_of_line_to_clicked_word = 0
        while length_of_line_to_clicked_word <= cursor_position:
            length_of_line_to_clicked_word += len(l[word_counter])+1
            word_counter += 1
        # uzycie wbudowanej w nltk funkcji dzielenia lancucha znakow na zdania
        sentences = sent_tokenize(text)
        list_of_words_in_sentences = [word.split() for word in sentences]

        length_counter = 0
        sentence_number = 0
        #petla dodajaca kolejne wyrazy do dopoki
        # counter nie bedzie rownal sie  kliknietemu slowu
        while length_counter <= word_counter-1:
            length_counter += len(list_of_words_in_sentences[sentence_number])
            sentence_number+=1
        # zwrocenie kliknietego slowa i zdania
        return [l[word_counter-1], sentences[sentence_number-1]]


# funkcja zwracajaca czesci mowy danego zdania
# przyjmujaca jako argument zdanie i zwracajaca liste slownikow  {slowo: czesc mowy}
def return_speech_part_dict(sent):
    dict_list = []
    c = training(sent)
    if c is not None:
        for i in range(len(c)):
            dict2 = {}
            word = str(c[i][0])
            #a2 = str(c[i][1])
            speech_part_description = return_speech_part_information(str(c[i][1]))
            dict2['word'] = word
            dict2['speech_part'] = speech_part_description[0]
            dict_list.append(dict2)
        return(dict_list)
    else:
        return(' ')





# funkcja zwracajaca czesci mowy
def return_speech_parts_and_count(state):
    editor_state = json.loads(state)
    list_of_lines = []
    text = ''

    # petla przetwarzajaca wyslany stan edytora
    # na liste akapitow
    for line in range(len(editor_state['blocks'])):
        list_of_lines.append([editor_state['blocks'][line]['text']])
        text += ' ' + editor_state['blocks'][line]['text']
    speech_parts = return_speech_part_dict(text)

    tab2 = []
    # instrukcja warunkowa pozwalajaca uniknac bledu, gdy w edytorze jest
    # wpisany tylko jeden znak
    if len(speech_parts) == 1 and speech_parts[0] == ' ':
        return[' ',' ']
    else:
        for i in range(len(speech_parts)):
            # tworzenie string wyswietlanego w edytorze
            # jako slowo : czesc mowy
            s = ''
            s += str(speech_parts[i]['word']) + ':   '+ str(speech_parts[i]['speech_part'])
            tab2.append(s)

        # czesc odopwiadajaca za czesci zdania w danym akapicie
        text = word_tokenize(text)
        word_count = Text_Statistics.word_frequency_list(text, number=10, stopwords = False)
        tab = []
        for i in range(len(word_count)):
            w = ''
            w += word_count[i][0]+ ': '+str(word_count[i][1])
            tab.append(w)


        res = []
        res.append(tab)
        res.append(tab2)
        return res


# funkcja przyjmujaca lancuch znakow i zwracajaca czesci mowy
def return_speech_parts(text):
    if len(text)!= 0:
        speech_parts = return_speech_part_dict(text)
        tab2 = []
        for i in range(len(speech_parts)):
            s = ''
            s += str(speech_parts[i]['word']) + ':   ' + str(speech_parts[i]['speech_part'])
            tab2.append(s)
        return tab2
    else:
        return ' '










