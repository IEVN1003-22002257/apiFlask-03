from flask import Flask, jsonify, request
from flask_mysqldb import MySQL  
from flask_cors import CORS
from config import config 

app = Flask(__name__)
CORS(app)  


app.config.from_object(config['development'])

conexion = MySQL(app)

@app.route('/alumnos', methods=['GET'])
def listar_alumnos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos"
        cursor.execute(sql)
        datos = cursor.fetchall()
        alumnos = []
        for fila in datos:
            
            apellido_completo = f"{fila[2]} {fila[3]}"
            
            alumno = {
                'matricula': fila[0],
                'nombre': fila[1],
                'apellido': apellido_completo, 
                'correo': fila[4]         
            }
            alumnos.append(alumno)
            

        return jsonify({'alumnos': alumnos, 'mensaje': 'Alumnos encontrados', "exito": True})
    
    except Exception as ex:
        return jsonify({'mensaje': f'Error al listar alumnos: {ex}', "exito": False})


@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe</h1>", 404


def leer_alumno_bd(matricula):
    try:
        cursor = conexion.connection.cursor()

        sql = "SELECT matricula, nombre, apaterno, amaterno, correo FROM alumnos WHERE matricula = %s"
        cursor.execute(sql, (matricula,)) # Pasamos la matrícula como tupla
        datos = cursor.fetchone()
        if datos != None:
            alumno = {'matricula': datos[0], 'nombre': datos[1], 'apaterno': datos[2], 'amaterno': datos[3], 'correo': datos[4]}
            return alumno
        else:
            return None
    except Exception as ex:
        raise ex

@app.route('/alumnos/<mat>', methods=['GET'])
def leer_curso(mat):  
    try:
        alumno = leer_alumno_bd(mat) 
        if alumno != None:
            return jsonify({'alumno': alumno, 'mensaje': "Alumno encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Alumno no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': f"Error: {ex}", 'exito': False})


if __name__ == '__main__':
    app.run()