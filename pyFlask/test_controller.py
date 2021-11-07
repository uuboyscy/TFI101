from flask import Blueprint

test_controller1 = Blueprint('test_controller', __name__)

@test_controller1.route('/test')
def test():
    return '<h1>TEST</h1>'