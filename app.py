from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    try:
        user_id = int(request.args.get('user_id', 1))
    except ValueError:
        user_id = 1
    return f'<h1>Hello, {user_id}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)