from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')

import os
genai.configure(api_key='AIzaSyABsXXlaIPy-JrIqc671ptSudrjvp5dn2A')  # Replace with your API key here

app = Flask(__name__)

user_info = {} # for storing information about user


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


@app.route('/', methods=['POST', 'GET'])
def index():
    global user_info

    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            question = prompt.strip().lower()

            if 'call' in question:
                return "Sure! Before we proceed, could you please provide your name, phone number, and email?"

            # elif 'name' in question:
            #     user_info['name'] = prompt
            #     return "Thank you! Could you please provide your phone number now?"

            elif 'phone number' in question:
                user_info['phone'] = prompt
                return "Great! Lastly, could you please provide your email?"

            elif 'email' in question:
                user_info['email'] = prompt
                return "Thank you! We will contact you shortly."

            else:
                response = model.generate_content(question)

                if response.text:
                    return response.text
                else:
                    return "Sorry, error is occurring"
        except Exception as e:
            print("Error:", e)
            return "An error occurred while processing your request. Details: {}".format(e)

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
