from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def web():
    return render_template("/webpage.html")

@app.route('/webpage')
def webp():
    return render_template('/webpage.html')
@app.route('/register')
def reg():
    return render_template("/register.html")

@app.route('/littilelend')
def lit():
    return render_template("/littilelend.html")

@app.route('/about')
def ab():
    return render_template("/about.html")

@app.route('/index')
def ind():
    return render_template('/index.html')

if("__main__"==__name__):
    app.run(debug=True,port=4000)


