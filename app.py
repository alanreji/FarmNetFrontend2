from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', transparent=True)


@app.route("/orders")
def orders():
    return "order"


@app.route("/account")
def account():
    return "account"


@app.route("/logout")
def logout():
    return "logout"


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")


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
    return render_template("item.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run()
