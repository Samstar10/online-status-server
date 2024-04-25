import base64
from flask import request, session, jsonify
from flask_restful import Resource, reqparse
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from cloudinary.uploader import upload
from werkzeug.datastructures import FileStorage
from flask_socketio import emit

from config import app, db, api, socketio

active_users = 0

@app.route('/')
def index():
    return 'Hello, World!'

# class ActiveUsers(Resource):
#     def get(self):
#         return jsonify(active_users=active_users)
    
#     @socketio.on('connect')
#     def on_connect():
#         global active_users
#         active_users += 1
#         emit('active_users', active_users, broadcast=True)
    
#     @socketio.on('disconnect')
#     def on_disconnect():
#         global active_users
#         active_users -= 1
#         emit('active_users', active_users, broadcast=True)
    

# api.add_resource(ActiveUsers, '/active_users')

@app.route('/active_users')
def get_active_users():
    return jsonify(active_users=active_users)

@socketio.on('connect')
def on_connect():
    global active_users
    active_users += 1
    emit('active_users', active_users, broadcast=True)

@socketio.on('disconnect')
def on_disconnect():
    global active_users
    active_users -= 1
    emit('active_users', active_users, broadcast=True)



if __name__ == '__main__':
    socketio.run(app)