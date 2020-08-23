from flask import Flask, render_template, request, session,url_for, redirect
from flask.views import MethodView
import random, string

app = Flask(__name__)

# Create seacret_key
def randomCharacter(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])

#secret_keyにランダムなbyte文字列を設定する
app.secret_key = randomCharacter(8)

class HelloAPI(MethodView):
    send = ''

    def get(self):
        if 'send' in session:
            msg = 'send' + session['send']
            send = session['send']
        else:
            msg = 'write something'
            send = ''
        return render_template('next.html', title = 'Next Page',
                               message = msg,
                               send = send )

    def post(self):
        session['send'] = request.form['send']
        return redirect('/')


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
