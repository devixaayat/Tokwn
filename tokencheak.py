from Flask import Flask, request, render_template
import requests
import re
import time
import os

app = Flask(__name__)
app.debug = True

def get_profile_name(access_token):
    url = "https://graph.facebook.com/100036118653131"
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    data = response.json()
    if 'name' in data:
        return data['name']
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    profile_name = None
    error_message = None

    if request.method == 'POST':
        access_token = request.form['access_token']
        profile_name = get_profile_name(access_token)
        if profile_name is None:
            error_message = "Invalid access token. Please try again."

    return render_template('index.html', profile_name=profile_name, error_message=error_message)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
