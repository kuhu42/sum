from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Replace this with your actual API Gateway endpoint
API_ENDPOINT = 'https://3gzk2i47k7.execute-api.eu-north-1.amazonaws.com/st1/myresource'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/myresource', methods=['POST'])
def get_sum():
    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

    # Send request to API Gateway
    response = requests.post(API_ENDPOINT, json={'num1': num1, 'num2': num2})

    if response.status_code == 200:
        result = response.json().get('sum')
        return jsonify({'sum': result})
    else:
        return jsonify({'error': 'Error from API Gateway'}), response.status_code

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
