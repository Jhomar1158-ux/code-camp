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
