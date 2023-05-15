from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/', methods=['GET'])
def counter():
    if 'count' not in session: session['count'] = 0    
    else: session['count'] += 1

    if 'visits' not in session: session['visits'] = 1
    else: session['visits'] += 1
    
    return render_template("index.html")

@app.route('/add2', methods=['POST'])
def add2():

    session['count'] += 1
    print(session['count'])
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

@app.route('/destroy_session', methods=['GET'])
def destroy_session():

    session.clear()
    return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():

    session['count'] = 0
    session['visits'] = 0
    print(session['count'])
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

@app.route('/increment_by', methods=['POST'])
def increment_by():
    
    session['count'] = session['count'] + int(request.form['increment']) - 1
    
    return redirect('/')

if __name__ == ("__main__"):
    app.run(debug=True )