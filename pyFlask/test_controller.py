from flask import Blueprint

test_controller = Blueprint('test_controller', __name__)

@test_controller.route('/test')
def test():
    return '<h1>TEST</h1>'