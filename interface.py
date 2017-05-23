from nltk_main import Text_Statistics
from tokenize_training import print_speech_table

def menu():
    print ('Narzędzie do analizy wczytanego tekstu lub wpisanego zdania')
    print('-----------------------------------------')
    l = []

    #a = input('wpisz nazwe pliku do analizy')

    for line in open("example.txt"):
        for word in line.split():
            l.append(word.lower())

    #print (l)
    print ('-----------------------------------------------')
    print('Menu wyboru wybierz co chcesz zrobić')
    print('Wybierz 1 aby wyswietlic 50 najpopularniejszych slow')
    print('Wybierz 2 aby wyswietlic statystyki tekstu')
    print('Wybierz 3 aby wyszukać slowa z podanym ciągiem znaków')
    print('Wybierz 4 aby wypisac czesci mowy dla wpisanego zdania')

    opcja = int(input('wpisz numer opcji z menu wyboru  '))

    if opcja ==1:
        print(Text_Statistics.word_frequency_list(l, 50))
    elif opcja ==2:
        print('roznorodnosc slownictwa')
        print(Text_Statistics.lexical_diversity(l))
    elif opcja ==3:
        zm = input('wpisz ciag zankow ktory ma zostac wyszukany')
        print(Text_Statistics.search_words_with_characters(l, '%s'%zm))
    elif opcja ==4:
        zm = str(input('wpisz zdanie'))
        print(print_speech_table(zm))


    else:
        print('nieznana metoda')

if __name__ == "__main__":
    menu()



#print('------------------------------------------------')
#print('50 najczesciej powtarzajacych sie slow w tescie')
#print (Text_Statistics.word_frequency_list(l,50))
