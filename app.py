from flask import Flask, request, render_template
import pickle
import model

app = Flask(__name__)
reg = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def start():
    return render_template('login.html')


data = {'test': 'test', 'krishnil': 'admin'}


@app.route('/index', methods=['POST'])
def index():
    username = request.form['username']
    password = request.form['password']
    if username not in data:
        return render_template('login.html', info='Invalid User')
    else:
        if data[username] != password:
            return render_template('login.html', info='Incorrect Password')
        else:
            return render_template('index.html')


@app.route('/estimate', methods=['POST'])
def estimate():
    form_year = request.form['year']
    form_odometer = request.form['odometer']
    form_title_status = request.form['title_status']
    form_transmission = request.form['transmission']
    form_drive = request.form['drive']
    form_state = request.form['state']

    try:
        values = [[int(form_year), int(form_odometer), model.title[form_title_status],
                   model.transmission[form_transmission], model.drive[form_drive], model.state[form_state.lower()]]]
        prediction = reg.predict(values)
        price = round(prediction[0], 2)
        return render_template('index.html', prediction_text='Price = $ {}' .format(price))
    except ValueError:
        return render_template('index.html', prediction_text='Invalid input')


if __name__ == '__main__':
    app.run()

