from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french(english_text):
    '''
    Translates English to French.
    '''
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return translation.get('translations')[0].get['translation']

@app.route("/frenchToEnglish")
def french_to_english(french_text):
    '''
    Translates French to English.
    '''
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return translation.get('translations')[0].get['translation']

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
