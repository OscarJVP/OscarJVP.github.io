# Librerias
from flask import *
import sqlite3
from sqlite3 import Error

# Basico
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/index.html");

# Uso de BD
@app.route("/registro")
def registro():
    return render_template("registro.html");

@app.route("/iniciarS")
def iniciarS():
    return render_template("iniciarS.html");

@app.route("/favoritos")
def favoritos():
    return render_template("favoritos.html");

@app.route("/agregar_favorito")
def agregar_favorito():
    return render_template("agregar_favorito.html");

@app.route("/borrar_favorito")
def borrar_favorito():
    return render_template("borrar_favorito.html");

@app.route("/registrar", methods = ["POST","GET"])
def registrar():
    mensaje = "mensaje base"
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            apellido_p = request.form["apellido_p"]
            apellido_m = request.form["apellido_m"]
            alias = request.form["alias"]
            password = request.form["password"]
            password_conf = request.form["password_conf"]
            
            if password == password_conf:
                conexion = sqlite3.connect("data.db")
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO usuarios (nombre, apellido_p, apellido_m, alias, password) VALUES (?,?,?,?,?);", (nombre,apellido_p,apellido_m,alias,password))
                conexion.commit()
                mensaje = "Usuario registrado"
            else:
                mensaje = "Confirmación de contraseña diferente, usuario no registrado"
            
        except Error as e:
            print(f"Error message: {e}")
            conexion.rollback()
            mensaje = "No se hizo el registro"
            
        finally:
            return render_template("respuesta.html", mensaje = mensaje);
            conexion.close()

@app.route("/actualizar", methods = ["POST","GET"])
def actualizar():
    mensaje = "mensaje base"
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            apellido_p = request.form["apellido_p"]
            apellido_m = request.form["apellido_m"]
            alias = request.form["alias"]
            password = request.form["password"]
            
            conexion = sqlite3.connect("data.db")
            cursor = conexion.cursor()
            cursor.execute("UPDATE usuarios SET nombre=?, apellido_p=?, apellido_m=?, alias=?, password=? WHERE alias=?;", (nombre,apellido_p,apellido_m,alias,password,alias))
            conexion.commit()
            mensaje = "Cambios registrados"
            
        except Error as e:
            print(f"Error message: {e}")
            conexion.rollback()
            mensaje = "No se hizo el cambio"
            
        finally:
            return render_template("respuesta.html", mensaje = mensaje);
            conexion.close()

@app.route("/usuario", methods = ["POST","GET"])
def usuario():
    mensaje = "mensaje base"
    display = "display base"
    row = []
    if request.method == "POST":
        try:
            alias_ingreso = request.form["alias_ingreso"]
            password_ingreso = request.form["password_ingreso"]
            conexion = sqlite3.connect("data.db")
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE alias=?", ([alias_ingreso]))
            row = cursor.fetchone()
            if row[-1] == password_ingreso:
                display = "usuario_lista.html"
            else:
                display = "respuesta.html"
                mensaje = "Contraseña incorrecta"
                
        except Error as e:
            print(f"Error message: {e}")
            conexion.rollback()
            mensaje = "No se encontró usuario"    
        finally:
            return render_template(display, mensaje = mensaje, fila = row);
            conexion.close()
    

@app.route("/guardar_receta", methods = ["POST","GET"])
def guardar_receta():
    mensaje = "mensaje base"
    if request.method == "POST":
        try:
            titulo = request.form["titulo"]
            conexion = sqlite3.connect("data.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO recetas (titulo) VALUES (?);", ([titulo]))
            conexion.commit()
            mensaje = "Receta agregada"
            
        except Error as e:
            print(f"Error message: {e}")
            conexion.rollback()
            mensaje = "No se agregó receta"
            
        finally:
            return render_template("respuesta.html", mensaje = mensaje);
            conexion.close()

@app.route("/borrar_receta", methods = ["POST","GET"])
def borrar_receta():
    mensaje = "mensaje base"
    if request.method == "POST":
        try:
            titulo = request.form["titulo"]
            conexion = sqlite3.connect("data.db")
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM recetas WHERE titulo=?", ([titulo]))
            conexion.commit()
            mensaje = "Receta eliminada"
            
        except Error as e:
            print(f"Error message: {e}")
            conexion.rollback()
            mensaje = "No se borró receta"
            
        finally:
            return render_template("respuesta.html", mensaje = mensaje);
            conexion.close()

@app.route("/listar_favoritos")  
def listar_favoritos():
    conexion = sqlite3.connect("data.db")
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM recetas")
    rows = cursor.fetchall()
    return render_template("favoritos_lista.html", filas = rows);

# Articulos
@app.route("/articulo_dia")
def articulo_dia():
    return render_template("articulo_dia.html");

@app.route("/articulo_mes")
def articulo_mes():
    return render_template("articulo_mes.html");

@app.route("/articulo_semana")
def articulo_semana():
    return render_template("articulo_semana.html");

# Recetas
@app.route("/arrozL")
def arrozL():
    return render_template("arrozL.html");

@app.route("/berenjenasR")
def berenjenasR():
    return render_template("berenjenasR.html");

@app.route("/burritosP")
def burritosP():
    return render_template("burritosP.html");

@app.route("/galletasA")
def galletasA():
    return render_template("galletasA.html");

@app.route("/galloE")
def galloE():
    return render_template("galloE.html");

@app.route("/jacobosJ")
def jacobosJ():
    return render_template("jacobosJ.html");

@app.route("/pechugaP")
def pechugaP():
    return render_template("pechugaP.html");

@app.route("/piernaA")
def piernaA():
    return render_template("piernaA.html");

@app.route("/pizzaR")
def pizzaR():
    return render_template("pizzaR.html");

@app.route("/polloR")
def polloR():
    return render_template("polloR.html");

@app.route("/smoothieF")
def smoothieF():
    return render_template("smoothieF.html");

@app.route("/tacosC")
def tacosC():
    return render_template("tacosC.html");

@app.route("/tartaH")
def tartaH():
    return render_template("tartaH.html");

@app.route("/tostadaA")
def tostadaA():
    return render_template("tostadaA.html");

@app.route("/tostadaM")
def tostadaM():
    return render_template("tostadaM.html");

# Ejecucion
if __name__ == '__main__':
    app.run(port=3000, debug=True)