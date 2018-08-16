from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello Heroku!</h1>
    <p>The time is currently: {time}.</p>
    """.format(time=the_time)


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)
