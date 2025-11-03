from flask import Flask,render_template, request
import forms

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

@app.route('/Alumnos', methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    alumnos_clase=forms.UserForm(request.form)
    
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.correo.data
    return render_template('alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em)

@app.route('/figuras', methods=['GET', 'POST'])
def figuras():
    resultado = ""
    figuras_form = forms.FigurasForm(request.form)
    
    if request.method == 'POST' and figuras_form.validate():
        
        figura = figuras_form.figura.data
        v1 = figuras_form.valor1.data
        v2 = figuras_form.valor2.data 

        if figura == 'triangulo':
            if v2 is None:
                resultado = "Error: El triángulo necesita 'Valor 2' (Altura)."
            else:
                area = (v1 * v2) / 2
                resultado = f"El área del triángulo es: {area}"
                
        elif figura == 'rectangulo':
            if v2 is None:
                resultado = "Error: El rectángulo necesita 'Valor 2' (Ancho)."
            else:
                area = v1 * v2
                resultado = f"El área del rectángulo es: {area}"
                
        elif figura == 'circulo':
            area = 3.1416 * (v1 ** 2)
            resultado = f"El área del círculo es: {area:.2f}"
            
        elif figura == 'pentagono':
            if v2 is None:
                resultado = "Error: El pentágono necesita 'Valor 2' (Apotema)."
            else:
                area = (5 * v1 * v2) / 2
                resultado = f"El área del pentágono es: {area}"
    
    return render_template('figuras.html', resultado=resultado, form=figuras_form)
    
@app.route('/index')
def index():

    titulo="IEVN1003 - PWA"
    listado=["Opera 1", "Opera 2", "Opera 3", "Opera 4"]
    return render_template('index.html', titulo=titulo, listado = listado)

@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/operas', methods=['GET', 'POST'])
def operas():
    resultado = "" 
    if request.method=='POST':
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        resultado=n1+n2 
    
    return render_template('operas.html', resultado=resultado)

@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route('/about')
def abaout():
    return "<h1>This is the about page.</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola "+ user

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID:{} nombre:{}".format(id,username)

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/prueba")
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
    <p>Esto es un parrafo</p>
    <ul>
        <li>Elemento 1</li>
        <li>Elemento 2</li>
        <li>Elemento 3</li>
    </ul>
'''

if __name__=='__main__':
    app.run(debug=True)
    
