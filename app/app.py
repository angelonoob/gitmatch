import requests, requests_cache, tempfile

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

requests_cache.install_cache('{}/cache'.format(tempfile.gettempdir()),expire_after=180)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # user input
        value_one = request.form.get('first')
        value_two = request.form.get('second')
        # api call
        url = 'https://api.github.com/search/users?q=location:{0}+language:{1}'.format(value_one, value_two)
        respons_dict = requests.get(url).json()
        # return json
        return jsonify(respons_dict)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)