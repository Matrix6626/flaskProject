from flask import Flask, url_for, request, render_template, make_response
import time

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['passwd']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/passwd'
#     return render_template('login.html',error=error)
@app.route('/user/<name>')
def profile(name=None):
    resp =make_response(render_template('hello.html', name=name))
    resp.set_cookie('username',name)
    return resp

with app.test_request_context():
    print url_for('index')
    # print url_for('login')
    # print url_for('login', next='/')
    print url_for('profile', name='John Doe')





if __name__ == '__main__':
    app.run(debug=True)
