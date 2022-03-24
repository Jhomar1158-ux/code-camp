
from flask import render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.user import User
from flask_app.models.room import Room
from flask_app.models.technology import Techonology



from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    rooms=Room.get_all()
    return render_template("index.html",rooms=rooms)

@app.route("/register-view")
def register_view():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():
    if not User.valida_usuario(request.form):
        return redirect("/")
    # Agregamos nuestro nuevo PASSWORD ENCRIPTADO
    pwd=bcrypt.generate_password_hash(request.form["password"])
    # CREAMOS nuestro nuevo diccionario con la PASSSWORD PROTEGIDA
    formulario={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"],
        "password":pwd,
    }
    id = User.save(formulario)

    session["user_id"]=id

    return redirect("/dashboard")

@app.route("/login-view")
def login_view():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user=User.get_by_email(request.form)
    if not user:
        flash("Email no encontrado" , "login")
        return redirect("/")

    if not (bcrypt.check_password_hash(user.password, request.form["password"])):
        flash("Password Incorrecto", "login")
        return redirect("/")

    session["user_id"] = user.id

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    
    data={
        "id":session["user_id"]
    }

    # Le mando mis datos y recibo un OBJETO USUARIO   
    # Usuario que INICIÓ SESIÓN  
    user=User.get_by_id(data)

    # Agregamos las rooms
    rooms=Room.get_all()


    return render_template("dashboard.html",user=user, rooms=rooms)


@app.route("/logout")
def logout():
    # COn este clear() borramos todas nuestras sessiones
    session.clear()
    return redirect("/")