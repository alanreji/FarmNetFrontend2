from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    render_template('index-2.html')

@app.route("/orders")
def orders():
    return "order"

@app.route("/account")
def account():
    return "account"

@app.route("/checkout")
def checkout():
    return "Checkout"

@app.route("/checkout_confirm")
def checkout_confirm():
    return "checkout_confirm"

@app.route("/invoice")
def invoice():
    return "invoice"

@app.route("/listing")
def listing():
    return "listing"

@app.route("/item")
def item():
    return "item"


if __name__ == '__main__':
    app.run()
