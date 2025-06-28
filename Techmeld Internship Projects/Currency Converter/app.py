# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined exchange rates based on USD
rates = {
    'USD': 1.0,
    'INR': 83.2,
    'EUR': 0.92,
    'GBP': 0.79,
    'JPY': 157.3
}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', result=None)

@app.route('/convert', methods=['GET'])
def convert():
    try:
        amount = float(request.args.get('amount'))
        from_currency = request.args.get('from_currency')
        to_currency = request.args.get('to_currency')

        if from_currency not in rates or to_currency not in rates:
            return render_template('index.html', result="❌ Invalid currency")

        usd = amount / rates[from_currency]
        converted = usd * rates[to_currency]
        result = f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}"
        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result="⚠️ Please enter a valid amount")

if __name__ == '__main__':
    app.run(debug=True)
