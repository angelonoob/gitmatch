from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello weird"


# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         value_one = int(request.form.get('first'))
#         value_two = int(request.form.get('second'))
#         total = value_one + value_two
#         data = {"total": str(total)}
#         return jsonify(data)
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # user input
        value_one = request.form.get('first')
        value_two = request.form.get('second')
        # api call
        url = 'https://api.github.com/search/users?q=location:{0}+language:{1}'.format(value_one, value_two)
        respons_dict = requests.get(url).json()
        return jsonify(respons_dict)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)