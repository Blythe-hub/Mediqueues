from flask import Flask, render_template, request, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdkjhl2938h82h43ph9f0h8(*&go9d8fg'
io = SocketIO(app)

@app.route('/login', methods=["GET","POST"])
def login():
    form = request.form.to_dict()
    session['first'] = form['first']
    session['last'] = form['last']
    session['address'] = form['address']
    session['provider'] = form['provider']
    session['spot'] = #getting max from db
    render_template('login.html')

@app.route('/queues', methods=["GET","POST"])
def queues():
    form = request.form
    session['spot'] = #getting users new spot
    render_template('queues.html', name = session['first'], spot = session['spot'])

@app.route('/leave')
def leave():
    #delete user from db
    pass
if __name__ == '__main__':
    io.run(app, debug = True)