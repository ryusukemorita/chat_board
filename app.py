from flask import Flask, render_template, request, session, redirect, jsonify
import pickle, random, string

app = Flask(__name__)

# Create Rondom String
def randomCharacter(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])

# Create new secret_key
app.secret_key = randomCharacter(8)

# Define Variable
member_data = {}
message_data = []
member_data_file = 'member_data.dat'
message_data_file = 'message_data.dat'

# Load member_data from file
try:
    with open(member_data_file, "rb") as f:
        list = pickle.load(f)
        if list != None:
            member_data = list
except:
    pass

# Load message_data from file
try:
    with open(message_data_file, "rb") as f:
        list = pickle.load(f)
        if list != None:
            message_data = list
except:
    pass

# Access top page
@app.route('/', methods=['GET'])
def index():
    global message_data
    return render_template('message.html', \
                            login = False, \
                            title = 'Chat Board', \
                            message = 'NOT logined...', \
                            data = message_data )

# Post message
@app.route('/post', methods=['POST'])
def postMsg():
    global message_data
    id = request.form.get('id')
    msg = request.form.get('comment')
    message_data.append((id, msg))
    if len(message_data) > 25:
        message_data.pop(0)
    try:
        with open(message_data_file, 'wb') as f:
            pickle.dump(message_data, f)
    except:
        pass
    return 'True'

# Get messages
@app.route('/messages', methods=['POST'])
def getMsg():
    global message_data
    return jsonify(message_data)

# Login from sended
@app.route('/login', methods=['POST'])
def login_post():
    global member_data, message_data
    id = request.form.get('id')
    pswd = request.form.get('pass')
    if id in member_data:
        if pswd == member_data[id]:
            flg = 'True'
        else:
            flg = 'False'
    else:
        member_data[id] = pswd
        flg = 'True'
        try:
            with open(member_data_file, 'wb') as f:
                pickle.dump(member_data, f)
        except:
            pass
    return flg

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
