from flask import Flask, redirect, url_for, render_template, request

import braintree

app = Flask(__name__)
app.config.from_pyfile("application.cfg")

gateway = braintree.Configuration.configure(
    braintree.Environment.Sandbox,
    app.config['BT_MERCHANT_ID'],
    app.config['BT_PUBLIC_KEY'],
    app.config['BT_PRIVATE_KEY']
)

@app.route('/')
def index():
    return redirect(url_for('new_checkout'))

@app.route('/checkouts/new')
def new_checkout():
    client_token = braintree.ClientToken.generate()
    return render_template('checkouts/new.html', client_token=client_token)

@app.route('/checkouts/<transaction_id>')
def show_checkout(transaction_id):
    transaction = braintree.Transaction.find(transaction_id)
    return render_template('checkouts/show.html', transaction=transaction)

@app.route('/checkouts', methods=['POST'])
def create_checkout():
    result = braintree.Transaction.sale({
        "amount": request.form["amount"],
        "payment_method_nonce": request.form["payment_method_nonce"],
    })
    return redirect(url_for('show_checkout',transaction_id=result.transaction.id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
