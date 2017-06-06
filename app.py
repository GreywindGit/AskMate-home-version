from flask import Flask, render_template, request, redirect
import bll
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    table = bll.get_five_recent_questions()
    return render_template('index.html', table=table, page_title='Main Page')


@app.route('/list')
def list_all_questions():
    table = bll.get_all_questions()
    return render_template('list.html', table=table, page_title='Questions')


@app.route('/new-question', methods=["GET"])
def show_question_form():
    return render_template('new-question.html', page_title='New Question')


@app.route('/new-question', methods=["POST"])
def ask_new_question():
    submission_time = datetime.now()
    view_number = 0
    vote_number = 0
    question_title = request.form['question_title']
    question_message = request.form['question_content']
    new_question = [submission_time, view_number, vote_number, question_title, question_message]
    bll.add_new_question(new_question)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
