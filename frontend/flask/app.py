from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import random

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
    nav = render_template( 'nav.html' )
    return render_template('heatmap.html', data=data, nav=nav, r=random.randint(1, 1000) )

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
    nav = render_template( 'nav.html' )
    return render_template('fluByRegion.html', data=data, nav=nav, r=random.randint(1, 1000) )
    
@app.route( '/water-flu' )
def waterFlu():
    feats = ['AirTemperature', 'Algae_Description', 'All', 'BottomChlorophyll_Fluorescence', 'BottompH', 'BottomTurbidity', 'BottomWater_Depth_at_Station', 'Bottom_DissolvedOxygen', 'Bottom_SpecificConductance', 'Bottom_WaterTemperature', 'Carbon_Dioxide', 'Chlorophyll_Fluorescence', 'Chlorophyll_Volume', 'CROP', 'Crop_Height', 'Crop_Height_Range', 'Density', 'Discharge', 'DissolvedOxygen', 'ElectricalConductance', 'Field_Notes', 'Field_Status', 'Flow,_channel', 'Flow,_pipe', 'Foam_Description', 'Gauge_Height', 'InflowMeter_Reading', 'Irrigation_Status', 'Meter_Reading', 'Microcystis_aeruginosa', 'NorthLatitude', 'Odor_Description', 'OutflowMeter_Reading', 'Percent_Cloud_Cover', 'pH', 'pH_w_time', 'Redox_Potential', 'Reference_Point_to_Water_Surface_RPTOWS', 'Secchi_Depth', 'SoilRedox_Potential', 'SpecificConductance', 'SpecificConductance_EC_w_time', 'Specific_Gravity', 'Tide_Time', 'Turbidity', 'Turbidity_Description', 'Turbidity_w_time', 'WaterColor_Description', 'WaterTemperature', 'WaterTemperature_w_time', 'Water_Depth_at_Station', 'Weather_Observations', 'WestLongitude', 'Wind_Direction', 'Wind_Velocity', 'Wind_Velocity_and_Direction', 'Wind_Velocity_Range']
    data = {
        'water': {
            'path': 'static/water/maps/',
            'feats' : feats,
            'limits' : [2001]
        },
        'flu': {
            'knownData': {
            'range' : [ [2001, 40], [2020, 39] ],
            'path': "static/fluRegionMaps/maps/"
            },
            'predictions': {
                'range' : [ [2020, 40], [2023, 30] ],
                'path': "static/fluRegionMaps/pred_maps/"
            }
        }
    }
    nav = render_template( 'nav.html' )
    return render_template('water-flu.html', feats=feats, data=data, nav=nav, r=random.randint(1, 1000) )

@app.route( '/vaccines' )
def vaccineStatic():
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
    nav = render_template( 'nav.html' )
    return render_template('vaccine.html', data=data, nav=nav, r=random.randint(1, 1000) )

@app.route('/')
def index():
    nav = render_template( 'nav.html' )
    return render_template('index.html', nav=nav, r=random.randint(1, 1000) )



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, port=5000)
    