from flask import Flask, render_template, request

app = Flask(__name__)

from sklearn.naive_bayes import MultinomialNB
import pickle
import os
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer

nltk.download("stopwords")

filename = os.path.join(app.root_path, 'email_classifier.sav')
with open(filename, 'rb') as file:  
    classifier = pickle.load(file)

filename = os.path.join(app.root_path, 'vectorizer.pickle')
with open(filename, 'rb') as file:  
    vectorizer = pickle.load(file)

def process_email(email):
    # lets pull out the non punctuation characters from email body
  no_punc_chars = [char for char in email.lower() if char not in string.punctuation]
  no_punc_body = "".join(no_punc_chars)

  # now we will filter the words which are not stopwords
  clean_words = [word for word in no_punc_body.split() if word.lower() not in stopwords.words('english')]

  return " ".join(clean_words)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/check",methods = ['POST'])
def check():
    email = request.get_json()['email']
    vectors = vectorizer.transform([process_email(email)])
    is_spam = classifier.predict(vectors)
    return {"is_spam": int(is_spam[0])}
    
if __name__ == "__main__":
    app.run(debug=True)