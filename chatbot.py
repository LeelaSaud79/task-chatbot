from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

import os
genai.configure(api_key='AIzaSyABsXXlaIPy-JrIqc671ptSudrjvp5dn2A')

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt

            response = model.generate_content(question)

            if response.text:
                return response.text
            else:
                return "Sorry, error is occuring"
        except Exception as e:
                print("Error:", e)
                return "An error occurred while processing your request. Details: {}".format(e)


    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)