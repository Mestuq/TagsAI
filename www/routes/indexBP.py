from flask import Blueprint,Flask,render_template, request, jsonify, url_for, redirect
from flask_socketio import SocketIO
from app import app, socketio

import csv

from routes import videosBP,channelsBP,favoritesBP

index_bp = Blueprint('index', __name__)

# INDEX.HTML

@index_bp.route('/', methods=['GET', 'POST'])
def advanced():
    channelsBP.load_channels()
    videosBP.load_videos()

    #resultsLogisticRegression
    #resultsRandomForest
    #accuracyLogisticRegression
    #accuracyRandomForest
    accuracy = load_csv("Accuracy.csv")
    resultsLogisticRegression = load_csv("LinearRegression.csv")
    resultsRandomForest = load_csv("RandomForest.csv")
    listOfDownloadedChannels = videosBP.getListOfDownloadedChannels()
    favorites = favoritesBP.getFavorites()
    videosSorted =sorted(videosBP.video_data, key=lambda x: int(x[2]) if x[2].isdigit() else float('inf'), reverse=True)
    return render_template('./advanced.html', 
                           channels=channelsBP.channels,
                           videos=videosSorted,
                           accuracy=accuracy, 
                           resultsLogisticRegression=resultsLogisticRegression, 
                           resultsRandomForest=resultsRandomForest, 
                           DownloadedChannels=listOfDownloadedChannels, 
                           favorites=favorites)

@socketio.on('connect', namespace='/test')
def test_connect():
    socketio.emit('connected', {'data': 'Connected'}, namespace='/test')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

def load_csv(source):
    try:
        with open(source, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        data = []
    return data