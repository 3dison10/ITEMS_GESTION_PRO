from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM cliente")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar usuarios en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    nombrecl = request.form['nombre_cliente']
    direccioncl = request.form['direccion_cliente']
    telefonocl = request.form['telefono_cliente']
    correocl = request.form['correo_cliente']

    if nombrecl and direccioncl and telefonocl and correocl:
        cursor = db.database.cursor()
        sql = "INSERT INTO cliente (nombre_cliente, direccion_cliente, telefono_cliente, correo_cliente) VALUES (%s, %s, %s, %s)"
        data = (nombrecl, direccioncl, telefonocl, correocl)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM cliente WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    nombrecl = request.form['nombre_cliente']
    direccioncl = request.form['direccion_cliente']
    telefonocl = request.form['telefono_cliente']
    correocl = request.form['correo_cliente']

    if nombrecl and direccioncl and telefonocl and correocl:
        cursor = db.database.cursor()
        sql = "UPDATE cliente SET nombre_cliente= %s, direccion_cliente %s, telefono_cliente %s, correo_cliente %s WHERE id= %s"
        data = (nombrecl, direccioncl, telefonocl, correocl, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)