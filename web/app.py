import numpy as np
import pickle
from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
model=pickle.load(open('model_web_etc','rb'))


@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'Genero': 'Selecciona el genero'}, {'Genero': 'Femenino'},
              {'Genero': 'masculino'}],
        data1=[{'hora': 'Selecciona la hora de la visita'}, {'hora': 8}, {'hora': 9}, {'hora': 10}, {'hora': 11}, {'hora': 12}, {'hora': 13},
               {'hora': 14}, {'hora': 15}, {'hora': 16}, {'hora': 17}, {'hora': 18}, {'hora': 19}, {'hora': 20}, {'hora': 21}],
        data2=[{'fallado': '¿Ha fallado antes?'}, {
            'fallado': 'Si'}, {'fallado': 'No'}],
        data3=[{'tto': "Selecciona el tipo de tratamiento a realizar"},{'tto': "Primera visita"}, {'tto': "Revision"}, {'tto': "Atm"},
               {'tto': 'Cirugia'}, {'tto': "Estetica y rehabilitacion oral"}, {'tto': "Endodoncia"}, {'tto': "Odontopediatria"},
               {'tto': 'Ortodoncia'}, {'tto': "Pacientes especiales"},{'tto': "Periodoncia"}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    a = input_data[5]
    b = input_data[1]
    c = input_data[4]
    the_date=datetime.strptime(input_data[0],"%Y-%m-%d")
    d = the_date.isoweekday()
    e = the_date.isocalendar()[1]
    if input_data[6] == 'No':
        f = 0
    elif input_data[6] == 'Si':
        f = 1
    if input_data[7] == "Primera visita":
        g = 0.185608
    elif input_data[7]=="Revision":
        g=0.185608
    elif input_data[7] == "Atm":
        g = 0.217256
    elif input_data[7] == "Cirugia":
        g = 0.151298
    elif input_data[7] == "Estetica y rehabilitacion oral":
        g = 0.200360
    elif input_data[7] == "Endodoncia":
        g = 0.186241
    elif input_data[7] == "Odontopediatria":
        g = 0.242105
    elif input_data[7] == "Ortodoncia":
        g = 0.143814
    elif input_data[7] == "Pacientes especiales":
        g = 0.221316
    elif input_data[7] == "Periodoncia":
        g = 0.162169

    if input_data[3] == "Femenino":
        i = 1
    else:
        i=0
    if input_data[3] == "Masculino":
        h = 1
    else:
        h = 0
    if input_data[2] == "Español":
        j = 1
        k = 0
    else:
        j = 0
        k = 1

    input_values = [a, b, c, d, e, f, g, h, i, j, k]
    arr_val = [np.array(input_values)]
    prediction = model.predict_proba(arr_val)
    output = '{0:.{1}f}'.format((prediction[0][1])*100, 2)
    return render_template('index.html', prediction_text=" La probabilidad de que el paciente acuda a la visita es {} %".format(output),
                            data=[{'Genero': 'Genero'}, {'Genero': 'Femenino'},
                                   {'Genero': 'masculino'}],
                            data1=[{'hora': 'Hora de la visita'}, {'hora': 8}, {'hora': 9}, {'hora': 10}, {'hora': 11}, {'hora': 12}, {'hora': 13},
                                {'hora': 14}, {'hora': 15}, {'hora': 16}, {'hora': 17}, {'hora': 18}, {'hora': 19}, {'hora': 20}, {'hora': 21}],
                            data2=[{'fallado': 'Ha fallado antes?'}, {
                                'fallado': 'Si'}, {'fallado': 'No'}],
                            data3=[{'tto': "Primera visita"}, {'tto': "Revision"}, {'tto': "Atm"},
                                {'tto': 'Cirugia'}, {'tto': "Estetica y rehabilitacion oral"}, {'tto': "Endodoncia"}, {'tto': "Odontopediatria"},
                                {'tto': 'Ortodoncia'}, {'tto': "Pacientes especiales"},{'tto': "Periodoncia"}])



if __name__ == '__main__':
    app.run(debug=True)
