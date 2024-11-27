from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for
from database import Database
import random
import string
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
db = Database()

def read_flag():
    try:
        with open('flag.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return 'Flag file not found.'

FLAG = read_flag()

INDEX_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTF Coupon Shop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        h1 { color: #333; }
        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Welcome to CTF Coupon Shop</h1>
    <p>Your coupon code is: <strong>{{ coupon }}</strong></p>
    <p>You can only use this coupon once to Buy.</p>
    <a href="{{ url_for('checkout') }}" class="button">Proceed to Checkout</a>
</body>
</html>
'''

CHECKOUT_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Checkout - CTF Coupon Shop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }
        h1, h2 {
            color: #333;
            text-align: center;
        }
        .order-summary {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .item, .total {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }
        .total {
            font-weight: bold;
            border-top: 1px solid #ddd;
            padding-top: 10px;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        label {
            margin-bottom: 5px;
        }
        input[type="text"] {
            width: 100%;
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .btn-primary {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn-primary:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Checkout</h1>
        <div class="order-summary">
            <h2>Order Summary</h2>
            <div class="item">
                <span>CTF Pro Hacker Package</span>
                <span>$99.99</span>
            </div>
            <div class="total">
                <span>Total</span>
                <span>$99.99</span>
            </div>
        </div>
        <form action="{{ url_for('process') }}" method="post">
            <label for="coupon">Coupon Code</label>
            <input type="text" id="coupon" name="coupon" placeholder="Enter your coupon code">
            <button type="submit" class="btn-primary">Place Order</button>
            <a href="{{ url_for('index') }}" class="button">New Coupon?</a>
        </form>
    </div>
</body>
</html>
'''

ERROR_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error - CTF Coupon Shop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        h1 { color: #333; }
        img {
            max-width: 100%;
            height: auto;
            margin: 20px 0;
        }
        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>Oops! Something went wrong</h1>
    <img src="https://media.giphy.com/media/3o7aTskHEUdgCQAXde/giphy.gif" alt="Funny error GIF">
    <p>{{ message }}</p>
    <a href="{{ url_for('checkout') }}" class="button">Try Again</a>
    <a href="{{ url_for('index') }}" class="button">New Coupon?</a>
</body>
</html>
'''

SUCCESS_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Successful - CTF Coupon Shop</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            max-width: 600px;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            text-align: center;
        }
        h1 {
            color: #4CAF50;
        }
        p {
            color: #333;
            margin-bottom: 20px;
        }
        .flag {
            background-color: #ffe6e6;
            border: 1px solid #ff9999;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
            margin-top: 20px;
        }
        .button {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Order Successful!</h1>
        <p>Thank you for your purchase of the CTF Pro Hacker Package.</p>
        {% if flag %}
        <p class="flag">Congratulations! Here's your flag: {{ flag }}</p>
        {% endif %}
        <a href="{{ url_for('checkout') }}" class="button">Back to Checkout</a>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    coupon = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    session['coupon'] = coupon
    db.add_coupon(coupon)
    return render_template_string(INDEX_TEMPLATE, coupon=coupon)

@app.route('/checkout')
def checkout():
    return render_template_string(CHECKOUT_TEMPLATE)

@app.route('/process', methods=['POST'])
def process():
    coupon = request.form.get('coupon')
    
    if coupon != session.get('coupon'):
        return redirect(url_for('error', message='Invalid coupon code'))

    if db.is_coupon_valid(coupon, app):
        # Enter here if coupon is valid and code is used 0 times.
        time.sleep(0.5)  # Simulate processing
        use_count = db.get_coupon_use_count(coupon, app)
        app.logger.info('use_count', use_count)
        if use_count == 0:
            db.increment_coupon_use(coupon)
            return render_template_string(SUCCESS_TEMPLATE, flag=None)
            # return jsonify({'success': True, 'message': 'Purchase successful!'})
        elif use_count >= 1:
            db.increment_coupon_use(coupon)
            return redirect(url_for('error', message=f'Coupon already used. Nice try! Here\'s your flag: {FLAG}'))
    else:
        return redirect(url_for('error', message='Invalid coupon code or Coupon already used. Sorry'))

@app.route('/error')
def error():
    message = request.args.get('message', 'An error occurred')
    return render_template_string(ERROR_TEMPLATE, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)