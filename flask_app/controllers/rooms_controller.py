
from flask import render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.user import User
from flask_app.models.room import Room
from flask_app.models.technology import Techonology


@app.route("/add-new-room")
def add_new_room():
    if 'user_id' not in session:
        return redirect('/')
    data={
        "id":session["user_id"]
    }

    technologies=Techonology.get_all()

    user=User.get_by_id(data)

    return render_template("add_room.html", technologies=technologies, user=user)



@app.route("/add-new-room-confirm", methods=["POST"])
def add_new_room_confirm():
    if 'user_id' not in session:
        return redirect('/')

    if not Room.valida_room(request.form):
        return redirect("/add-new-room")
    
    Room.save(request.form)
    

    return redirect("/dashboard")


@app.route("/view-room-<int:id>")
def view_room_id(id):
    if "user_id" not in session:
        return redirect("/")
    
    data={
        "id":session["user_id"]
    }
    user=User.get_by_id(data)

    data_room = {
        "id": id
    }

    room_details = Room.get_by_id(data_room)
    
    return render_template("room.html", user=user, room_details=room_details)

@app.route("/search-tech-room", methods=["GET"])
def search_tech_room():
    print(request.form)
    if "user_id" not in session:
        return redirect("/")
    data={
        "id":session["user_id"]
    }
    formulario={
        "main_search_tech": request.args.get("main_search_tech")
    }
    user=User.get_by_id(data)

    rooms=Room.get_all_rooms_by_text(formulario)
    print(rooms)

    return render_template("dashboard_search.html",rooms=rooms, user=user)

@app.route("/delete/room/<int:id>")
def delete_room(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id":id
    }

    Room.delete(data)
    return redirect("/dashboard")


@app.route("/edit/room/<int:id>")
def edit_room(id):
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)

    data_room = {
        "id": id
    }
    room_select = Room.get_by_id(data_room)
    technologies=Techonology.get_all()

    return render_template('edit_room.html',technologies=technologies, user=user, room_select=room_select)


@app.route("/update/room", methods=["POST"])
def update_room():
    if 'user_id' not in session:
        return redirect('/')

    if not Room.valida_room(request.form):
        return redirect("/edit/room/"+request.form['id'])
    
    Room.update(request.form)
    print("%"*10)
    print(request.form)

    return redirect("/dashboard")