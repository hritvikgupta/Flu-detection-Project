from flask import Flask, render_template, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# Define the folder where your images are stored
IMAGE_FOLDER = os.path.join('static', 'flueRegionMaps')

@app.route('/heatmap')
def heatmap():
    data = {
        'knownData': {
            'range' : [ [2001, 40], [2020, 39] ],
            'path': "static/popDensity/maps/"
        },
        'predictions': {
            'range' : [ [2020, 40], [2023, 30] ],
            'path': "static/popDensity/pred_maps/"
        }
    }
    return render_template('heatmap.html', data=data )

@app.route( '/fluByRegion' )
def fluByRegion():
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
    return render_template('fluByRegion.html', data=data )
    
    

@app.route('/')
def index():
    return render_template('index.html' )



if __name__ == '__main__':
    app.run(debug=True)
    