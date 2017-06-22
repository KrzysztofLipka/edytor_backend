from flask import Flask, render_template, make_response , jsonify, request, url_for, json
from nltk_main import Model, Text_Statistics,click_event_processing2, return_speech_parts_and_count,return_speech_part_dict, return_speech_parts
app = Flask(__name__)

# modul ktorego uruchomienie rozpoczyna dzialanie serwera

# funkcja wywolywana po wyslaniu z edytora zadania zwrocenia synonimow danego slowa
@app.route('/background_process')
def background_process():
    word = request.args.get('proglang', 0, type=str)
    syno_sets = Model().Add_Synonyms(word)
    return jsonify(result=syno_sets)

# funkcja wywolywana po edytowaniu stanu edytora i zwracajaca liczebnosc slow w edytorze oraz
# czesci mowy
@app.route('/send_editor_state')
def editor_state_handling():
    state = request.args.get('editor_state', 0)
    res = return_speech_parts_and_count(state)
    return jsonify(word_count = res[0], speech_parts = res[1])



@app.route("/")
def index():
    return render_template('index.html')

# funkcja wywolywana po kliknieciu  i zwracajaca synonim klikneitego slowa
# oraz czesci mowy kliknietego zdania
@app.route('/click_event=')
def click_event():
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res =  click_event_processing2(kursor_id, text)
    word = Model().Add_Synonyms(res[0])
    speech_part = return_speech_parts(res[1])
    return jsonify(synonims = word, speech_parts = speech_part)


if __name__ == "__main__":
    app.run()