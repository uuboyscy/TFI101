from flask import Flask, request, jsonify
import poker as p
import seriesFunction as s

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/hello/<username>')
def hello(username):
    return 'Hello {}'.format(username)

@app.route('/add/<x>/<y>')
def add(x, y):
    return str(int(x) + int(y))

@app.route('/api/get_class_student_list/<classid>')
def get_class_student_list(classid):
    sql = """
    SELECT studentid, studentname 
    FROM class 
    WHERE classid='{}'
    """.format(classid)
    # result = query(sql)
    return sql

## /hello_get?name=Allen&age=22
@app.route('/hello_get')
def hello_get():
    name = request.args.get('name')
    age = request.args.get('age')
    if name == None:
        return 'Who are you?'
    if age == None:
        return 'Hello {}.'.format(name)
    outputString = "<h1>Hello {}, you are {} years old.</h1>"
    return outputString.format(name, age)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <form action="/hello_post" method="POST">
        What is your name?
        <br>
        <input name="username">
        <button type="submit">SUBMIT</button>
    </form>
    """
    requestMethod = request.method
    if requestMethod == 'POST':
        username = request.form.get('username')
        outStr += """
        <h1>Hello {}!</h1>
        """.format(username)

    return outStr

# /poker?player=5
@app.route('/poker')
def poker():
    player = int(request.args.get('player'))
    player_cards = p.poker(player)
    # a = doSomething1()
    # b = doSomething2(a)

    return jsonify(player_cards)

# /getSeries?n=5
@app.route('/getSeries')
def getSeries():
    n = int(request.args.get('n'))
    return str(s.Func(n))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

