from flask import Flask, render_template, request, session, redirect

from db_methods import methods, config
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdkjhlsdfg'
execute = methods(config)

@app.route('/', methods=["GET","POST"])
def login():
    form = request.form.to_dict()
    if 'first' in form and 'last' in form and 'birthday' in form and 'provider' in form:
        session['first'] = first = form['first']
        session['last'] = last = form['last']
        session['birthday'] = birthday = form['birthday']
        session['provider'] = provider = form['provider']
        session['spot'] = spot = execute.new_spot()
        execute.new_entry(first, last, birthday, provider, spot)
        return redirect('/queues')
    return render_template('login.html')

@app.route('/queues')
def queues():
    first = session['first']
    last = session['last']
    tem_spot = execute.get_spot(first, last)
    session['spot'] = tem_spot[0]
    infront = execute.total_infront(first, last)
    return render_template('queues.html', name = session['first'], spot = session['spot'], total_infront = infront)

@app.route('/leave')
def leave():
    first = session['first']
    last = session['last']
    spot = session['spot']
    execute.leave(first, last, spot)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)

#connect heroku database