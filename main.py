from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the simple form example! Go to /form to see the form."

@app.route('/form', methods=['GET', 'POST'])
def simple_form():
    if request.method == 'POST':

        rup = request.form.get('rup')
        tiket = request.form.get('tiket')
        alasan = request.form.get('alasan')

        return render_template('result.html', rup=rup, tiket=tiket, alasan=alasan)

    else:

        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)