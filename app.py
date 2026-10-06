from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll_no = request.form['roll_no']
    return render_template('success.html', name=name, roll_no=roll_no)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
