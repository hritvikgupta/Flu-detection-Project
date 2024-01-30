from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import random
import requests

# shareable_link = "https://drive.google.com/drive/folders/1EiU67w-Ma6_sHkexAZFtGeS3vOSw8K-B?usp=sharing"
# file_id = shareable_link.split('/d/')[1].split('/view')[0]
# direct_link = f'https://drive.google.com/uc?export=download&id={file_id}'
# response = requests.get(direct_link)
# print(response)

if not os.path.exists( 'static/fluRegionMaps' ):
    os.makedirs( 'static/fluRegionMaps/maps' )
    os.makedirs( 'static/fluRegionMaps/pred_maps' )
if not os.path.exists( 'static/popDensity' ):
    os.makedirs( 'static/popDensity/maps' )
    os.makedirs( 'static/popDensity/pred_maps' )
if not os.path.exists( 'static/vaccines' ):
    os.makedirs( 'static/vaccines/c_maps' )
    os.makedirs( 'static/vaccines/maps' )
if not os.path.exists( 'static/water' ):
    x = ['AirTemperature', 'Algae_Description', 'All', 'BottomChlorophyll_Fluorescence', 'BottompH', 'BottomTurbidity', 'BottomWater_Depth_at_Station', 'Bottom_DissolvedOxygen', 'Bottom_SpecificConductance', 'Bottom_WaterTemperature', 'Carbon_Dioxide', 'Chlorophyll_Fluorescence', 'Chlorophyll_Volume', 'CROP', 'Crop_Height', 'Crop_Height_Range', 'Density', 'Discharge', 'DissolvedOxygen', 'ElectricalConductance', 'Field_Notes', 'Field_Status', 'Flow,_channel', 'Flow,_pipe', 'Foam_Description', 'Gauge_Height', 'InflowMeter_Reading', 'Irrigation_Status', 'Meter_Reading', 'Microcystis_aeruginosa', 'NorthLatitude', 'Odor_Description', 'OutflowMeter_Reading', 'Percent_Cloud_Cover', 'pH', 'pH_w_time', 'Redox_Potential', 'Reference_Point_to_Water_Surface_RPTOWS', 'Secchi_Depth', 'SoilRedox_Potential', 'SpecificConductance', 'SpecificConductance_EC_w_time', 'Specific_Gravity', 'Tide_Time', 'Turbidity', 'Turbidity_Description', 'Turbidity_w_time', 'WaterColor_Description', 'WaterTemperature', 'WaterTemperature_w_time', 'Water_Depth_at_Station', 'Weather_Observations', 'WestLongitude', 'Wind_Direction', 'Wind_Velocity', 'Wind_Velocity_and_Direction', 'Wind_Velocity_Range']
    for i in x:
        os.makedirs( f'static/water/{i}')

app = Flask(__name__, static_folder='static')


# Define the folder where your images are stored
IMAGE_FOLDER = os.path.join('static', 'flueRegionMaps')

@app.route('/heatmap')
def heatmap():
    base_url = "https://raw.githubusercontent.com/hritvikgupta/Flu-data/main/Downloads/"
    base_url = base_url.replace("watch?v=", "v/")
    data = {
        'knownData': {
            'range' : [ [2001, 40], [2020, 39] ],
            'path': base_url + "popDensity/maps/"
        },
        'predictions': {
            'range' : [ [2020, 40], [2023, 30] ],
            'path': base_url + "popDensity/pred_maps/"
        }
    }
    nav = render_template( 'nav.html' )
    return render_template('heatmap.html', data=data, nav=nav, r=random.randint(1, 1000) )

@app.route( '/fluByRegion' )
def fluByRegion():
    base_url = "https://raw.githubusercontent.com/hritvikgupta/Flu-data/main/"
    data = {
        'knownData': {
            'range' : [ [2001, 40], [2020, 39] ],
            'path': base_url + "/maps/"
        },
        'predictions': {
            'range' : [ [2020, 40], [2023, 30] ],
            'path': base_url + "/pred_maps/"
        }
    }
    nav = render_template( 'nav.html' )
    return render_template('fluByRegion.html', data=data, nav=nav, r=random.randint(1, 1000) )
    
@app.route( '/water-flu' )
def waterFlu():
    base_url = "https://raw.githubusercontent.com/hritvikgupta/Flu-data/main/Downloads/"
    flu_url = "https://raw.githubusercontent.com/hritvikgupta/Flu-data/main/"
    feats = ['AirTemperature', 'Algae_Description', 'All', 'BottomChlorophyll_Fluorescence', 'BottompH', 'BottomTurbidity', 'BottomWater_Depth_at_Station', 'Bottom_DissolvedOxygen', 'Bottom_SpecificConductance', 'Bottom_WaterTemperature', 'Carbon_Dioxide', 'Chlorophyll_Fluorescence', 'Chlorophyll_Volume', 'CROP', 'Crop_Height', 'Crop_Height_Range', 'Density', 'Discharge', 'DissolvedOxygen', 'ElectricalConductance', 'Field_Notes', 'Field_Status', 'Flow,_channel', 'Flow,_pipe', 'Foam_Description', 'Gauge_Height', 'InflowMeter_Reading', 'Irrigation_Status', 'Meter_Reading', 'Microcystis_aeruginosa', 'NorthLatitude', 'Odor_Description', 'OutflowMeter_Reading', 'Percent_Cloud_Cover', 'pH', 'pH_w_time', 'Redox_Potential', 'Reference_Point_to_Water_Surface_RPTOWS', 'Secchi_Depth', 'SoilRedox_Potential', 'SpecificConductance', 'SpecificConductance_EC_w_time', 'Specific_Gravity', 'Tide_Time', 'Turbidity', 'Turbidity_Description', 'Turbidity_w_time', 'WaterColor_Description', 'WaterTemperature', 'WaterTemperature_w_time', 'Water_Depth_at_Station', 'Weather_Observations', 'WestLongitude', 'Wind_Direction', 'Wind_Velocity', 'Wind_Velocity_and_Direction', 'Wind_Velocity_Range']
    data = {
        'water': {
            'path': base_url + 'water/maps/',
            'feats' : feats,
            'limits' : [2001]
        },
        'flu': {
            'knownData': {
            'range' : [ [2001, 40], [2020, 39] ],
            'path': flu_url + "maps/"
            },
            'predictions': {
                'range' : [ [2020, 40], [2023, 30] ],
                'path': flu_url + "pred_maps/"
            }
        }
    }
    nav = render_template( 'nav.html' )
    return render_template('water-flu.html', feats=feats, data=data, nav=nav, r=random.randint(1, 1000) )

@app.route( '/vaccines' )
def vaccineStatic():
    base_url = "https://raw.githubusercontent.com/hritvikgupta/Flu-data/main/Downloads/"
    features = {
        'age' : ['Age Range 18-64 Years', 'Age Range 6 Months - 17 Years', 'Age Range 13-17 Years', 'Age Range 6 Months - 4 Years', 'Age Range 18-49 Years at High Risk', 'Age Range 50-64 Years', 'Age Range ≥18 Years', 'Age Range ≥6 Months', 'Age Range 18-64 Years at High Risk', 'Age Range 5-12 Years', 'Age Range 18-49 Years', 'Age Range ≥65 Years', 'Age Range 18-49 Years not at High Risk', 'Age Range 18-64 Years not at High Risk'],
        're' : ['Hispanic', 'White, Non-Hispanic', 'American Indian or Alaska Native, Non-Hispanic', 'Black, Non-Hispanic', 'Other or Multiple Races, Non-Hispanic', 'Asian, Non-Hispanic']
    }
    d = {
        'feats' : {
            'age' : {
                'feats' : features['age'],
                'path' : base_url + 'vaccines/maps/age',
                'name' : 'Age by State'
            },
            're' : {
                'feats' : features['re'],
                'path' : base_url + 'vaccines/maps/re',
                'name' : 'Race & Ethnicity by State',
                'limit': []
            },
            'county' : {
                'path': base_url + 'vaccines/maps/county',
                'name' : 'Yearly by County',
                'limit': [2018,2021]
            }
        }
    }
    
    nav = render_template( 'nav.html' )
    return render_template('vaccine.html', data=d, nav=nav, r=random.randint(1, 1000) )

@app.route('/')
def index():
    nav = render_template( 'nav.html' )
    return render_template('index.html', nav=nav, r=random.randint(1, 1000) )



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, port=5000)
    
    
    