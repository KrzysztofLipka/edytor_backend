from flask import Flask, render_template, make_response , jsonify, request, url_for, json
from nltk_main import Model
from speech_part import return_speech_part_information
from tokenize_training import training
from nltk import FreqDist,sent_tokenize

def return_speech_part_dict(sent):

    dict_list = []
    c = training(sent)
    for i in range(len(c)):
        dict2 = {}
        a1 = str(c[i][0])
        a2 = str(c[i][1])
        a3 = return_speech_part_information(a2)
        dict2['word'] = a1
        dict2['speech_part'] = a3[0]
        dict_list.append(dict2)
    return(dict_list)






