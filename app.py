from flask import Flask, render_template, request
import bll

app = Flask(__name__)


@app.route('/')
def index():
    table = bll.get_five_recent_questions()
    return render_template('index.html', table=table, page_title='Main Page')


@app.route('/list')
def list_all_questions():
    table = bll.get_all_questions()
    return render_template('list.html', table=table, page_title='Questions')


if __name__ == '__main__':
    app.run(debug=True)
