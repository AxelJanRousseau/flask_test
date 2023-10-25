from ast import AsyncFunctionDef
from flask import Flask, render_template, stream_with_context, request, Response, flash, stream_template, stream_template_string, url_for
import flask
from time import sleep
import random
import openai

import os
from dotenv import load_dotenv

load_dotenv()
# OPENAI_KEY=os.getenv('OPENAI_API_KEY')
SYSTEM_PROMPT ="Jij ben een schrijver van kinderverhaaltjes. Je krijgt een beschrijving van kindje en schrijft een gepersonaliseerd verhaaltje over hun avonturen op de wetenschapsbeurs."
app = Flask(__name__)


data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def generate(data):
    # could be used to stream story, instructions here: 
    # https://cookbook.openai.com/examples/how_to_stream_completions,
    # but would require to load a new page to work with ninja's templating.
    # otherwise, you could try polling in js 
    for item in data:
        yield item
        sleep(random.uniform(0.,0.1))

@app.route('/stream')
def stream_view():
    # just text, maybe for ajax call?
    # rows = generate(data)
    return data, {"Content-Type": "text/plain"}

@app.route('/stream2')
def stream_view2():
    # stream tempalte html
    rows = generate(data)
    return stream_template('stream_template.html', rows=rows)

@app.route('/stream3')
def stream_view3():
    return Response(stream_with_context(generate(data)))

@app.route('/')
def start():
    # return flask.send_file('templates/post_test.html')
    return render_template('post_test.html')

def get_story(prompt: str) -> str:
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              temperature=1.,
                                              stream=False,
                                              messages=[{"role": "system", "content": SYSTEM_PROMPT},
                                                        {"role": "user", "content": prompt}])
    return (completion.choices[0].message.content)


@app.post('/story')
def get_story_promt():
    print('generating story')
    prompt = request.form['prompt']
    story=get_story(prompt)
    return story

if __name__ == '__main__':
    app.debug = True
    app.run()