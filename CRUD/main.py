from flask import Flask, render_template, request, redirect, url_for
import sqlite3

import sqlite3

app = Flask(__name__)

DB_path = f"/home/mkono/Delta-data_CRUD/DataBase/DeltaDataDB.db" #ruta de la base de datos, se utiliza una ruta absoluta

#Base de datos
def init_db():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    #si no existe la tabla crea la tabla correspondiente
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS creditos(
            id INTEGER PRIMARY KEY NOT NULL, 
            cliente TEXT NOT NULL,
            monto REAL NOT NULL, 
            tasa_interes REAL NOT NULL, 
            plazo INTEGER NOT NULL, 
            fecha_otorgamiento TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#mostrar creditos
def get_credits():
    conn = sqlite3.connect(DB_path) #nota: la variable conn = connection 
    cursor = conn.cursor() #nota: la variable cursor apunta a el puntero que manejara las sentencias con SQL
    cursor.execute('SELECT * FROM creditos')
    credits = cursor.fetchall()
    conn.close()
    return credits

## NOTA IMPORTANTE ##
# la variable conn es para todas las funciones (variable local)
# la varuable cursor es para para todas las funciones (variable local)

#ingresar un nuevo credito
def add_credit(cliente, monto, tasa_interes, plazo, fecha_otorgamiento):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO creditos(cliente, monto, tasa_interes, plazo, fecha_otorgamiento) VALUES(?,?,?,?,?)', (cliente, monto, tasa_interes, plazo, fecha_otorgamiento))
    conn.commit()
    conn.close()

#actualizar tabla
def actualizar_tabla(id, cliente, monto, tasa_interes, plazo, fecha_otorgamiento):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE creditos SET cliente = ?, monto = ?, tasa_interes = ?, plazo = ?, fecha_otorgamiento = ? WHERE id = ?', (cliente, monto, tasa_interes, plazo, fecha_otorgamiento, id))
    conn.commit()
    conn.close()

#Borrar credito
def borrar_credito(id):
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM creditos WHERE id = ?', (id,))
    conn.commit()
    conn.close()

#index html
@app.route('/')
def index():
    credits = get_credits()
    return render_template('index.html', credits=credits)


#incluir credito VIA POST
@app.route('/add_credit', methods=['POST'])
def add_credit_route():
    cliente = request.form['cliente']
    monto = request.form['monto']
    tasa_interes = request.form['tasa_interes']
    plazo = request.form['plazo']
    fecha_otorgamiento = request.form['fecha_otorgamiento']
    add_credit(cliente, monto, tasa_interes, plazo, fecha_otorgamiento)
    return redirect(url_for('index'))

#ACTUALIZAR via POST request
@app.route('/update_credit/<int:id>', methods=['GET', 'POST'])
def update_credit_route(id):
    if request.method == 'POST':
            cliente = request.form['cliente']
            monto = request.form['monto']
            tasa_interes = request.form['tasa_interes']
            plazo = request.form['plazo']
            fecha_otorgamiento = request.form['fecha_otorgamiento']
            actualizar_tabla(id, cliente, monto, tasa_interes, plazo, fecha_otorgamiento)
            return redirect(url_for('index'))
    
    # llenar fomrulario desde los datos del uauario
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM creditos WHERE id = ?', (id,))
    credits = cursor.fetchone()
    conn.close()
    return render_template('actualizar_credito.html', credits=credits)

#Borrar VIA GET request
@app.route('/delete_credit/<int:id>', methods = ['GET'])
def delete_credit_route(id):
    borrar_credito(id)
    return redirect(url_for('index'))

#Implementacion de graficos
@app.route('/graphics')
def graphics():
    conn = sqlite3.connect(DB_path)
    cursor = conn.cursor()
    cursor.execute("SELECT cliente, monto FROM creditos")
    data = cursor.fetchall()
    conn.close()

    clientes = [row[0] for row in data]
    montos = [row[1] for row in data]
    return render_template("graphics.html", clientes = clientes, montos=montos)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)



