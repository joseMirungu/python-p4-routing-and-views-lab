from flask import Flask

app = Flask(__name__)

# Route: Index
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# Route: Print String
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# Route: Count Numbers
@app.route('/count/<int:parameter>')
def count(parameter):
    return "<br>".join(str(i) for i in range(parameter))

# Route: Math Operations
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        if num2 != 0:
            return str(num1 / num2)
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation."

if __name__ == '__main__':
    app.run(port=5555)
