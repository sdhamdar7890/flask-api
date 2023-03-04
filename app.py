from flask import Flask,request,redirect,url_for

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method== 'POST':
        user = request.form['user']
        return redirect(url_for('home', user=user))
    else:
        return redirect



if __name__=='__main__':
    app.run()