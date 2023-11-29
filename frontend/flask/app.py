from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# Define the folder where your images are stored
IMAGE_FOLDER = os.path.join('static', 'flueRegionMaps')

@app.route('/test')
def heatmap():
    return render_template('heatmap.html' )

@app.route('/')
def index():
    data = {
        'knownData': {
            'range' : [ [2001, 40], [2020, 39] ],
            'path': "static/fluRegionMaps/maps/"
        },
        'predictions': {
            'range' : [ [2020, 40], [2023, 30] ],
            'path': "static/fluRegionMaps/pred_maps/"
        }
    }
    return render_template('index.html', data=data )



if __name__ == '__main__':
    app.run(debug=True)
    