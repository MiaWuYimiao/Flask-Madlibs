from flask import Flask, render_template, request
from stories import stories

app = Flask(__name__)

@app.route('/')
def home_page():
    """Show home page"""
    return render_template('home.html', stories=stories.values())

@app.route('/form')
def form_page():
    """Show home page with a form to submit story"""
    stype = request.args["story_type"]
    story = stories[stype]
    prompts = story.prompts
    return render_template('form.html',prompts=prompts, story_type=stype)

@app.route('/story')
def your_story():
    """Show your story"""
    stype=request.args["story_type"]
    story=stories[stype]
    ans = request.args
    print(request.args)
    text = story.generate(ans)
    return render_template('story.html',story=text)
