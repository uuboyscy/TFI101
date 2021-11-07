from flask import Flask, request, jsonify, render_template
import poker as p
import seriesFunction as s
import model
from test_controller import test_controller1

app = Flask(__name__, static_url_path='/source', static_folder='./static')
app.register_blueprint(test_controller1, url_prefix='/otherfunctions')

@app.route('/')
def index():
    return '<a href="/source/css/style.css">Hello Flask!</a>'
    # return '<img src="/static/image.jpg">'

@app.route('/hello/<username>')
def hello(username):
    return 'Hello {}'.format(username)

@app.route('/hello2/<username>')
def hello2(username):
    return render_template('hello.html', username=username)

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

@app.route('/hello_get2')
def hello_get2():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('hello_get.html', name=name, age=age)

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
@app.route('/hello_post2')
def hello_post2():
    username = ''
    requestMethod = request.method
    if requestMethod == 'POST':
        username = request.form.get('username')
    return render_template(
        'hello_post.html',
        username=username,
        requestMethod=requestMethod
    )


# /poker?player=5
@app.route('/poker')
def poker():
    player = int(request.args.get('player'))
    player_cards = p.poker(player)
    # a = doSomething1()
    # b = doSomething2(a)

    return jsonify(player_cards)

@app.route('/poker2', methods=['GET', 'POST'])
def poker2():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html'
                           ,request_method=request_method
                           ,cards=cards)

# /getSeries?n=5
@app.route('/getSeries')
def getSeries():
    n = int(request.args.get('n'))
    return str(s.Func(n))

@app.route('/show_staff')
def show_staff():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

