from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ciencia/')
def informacionc():
    return  render_template('informacionc.html')

@app.route('/salud/')
def salud():
    return  render_template('salud.html')

@app.route('/Informate/')
def manualp():
    return  render_template('manualp.html')


@app.route('/Aprendizaje/')
def psico():
    return  render_template('psico.html')


@app.route('/contacto/')
def contacto():
    return  render_template('contacto.html')



@app.route('/alimentación/')
def listasuper():
    return  render_template('listasuper.html')



@app.route('/entrenamiento/')
def entrenamiento():
    return  render_template('entrenamiento.html')


@app.route('/recreación/')
def recreacion():
    return  render_template('recreacion.html')



@app.route('/educación/')
def aprendizaje():
    return  render_template('aprendizaje.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")