# cs225/226 joint group

## Flu Data instruction

To run the flu data scripts which are located in `fluregion_final.ipynb` you need the following folders
and data: empty folders `backend/flu_region/maps`, `backend/flu_region/pred_maps` `backend/flu_region/pred_by_dates`, and then shapefile data for `backend/data/CA_Counties/CA_Counties_TIGER2016.shp`. Then run the notebook line by line to get the output of flu region data in map in the following folders: ``backend/flu_region/maps` and `backend/flu_region/pred_maps` which can then be placed into the flask frontend in the corresponding folders

## Flu Heatmap instructions

The heatmap code is located in `OSM.ipynb` to run this code it assumes there are data files set up for flu data. it needs the following folders `backend/flu_region/`, `backend/flu_region/flu_by_dates`, `backend/flu_region/pred_by_dates` which contain semi-parse csv folders. It also need the california county shape file that exists in `backend/data/CA_Counties/CA_Counties_TIGER2016.shp`. Then run the notebook line by line. The output will be placed into the folder `backend/popDensity/maps` & `backend/popDensity/pred_maps` these can then be placed into the `frontend/flask/static/popDensity/` folder

## Water Contamination instructions

To run the flu data scripts which are located in `water-contamination.ipynb` confirm the dataset `field_results.csv` exists in `backend/water-contamination/` and the california county shape file that exists in `backend/data/CA_Counties/CA_Counties_TIGER2016.shp` then run the python notebook and it will parse the data and generate the heat maps. Once it is generated it can be moved to the frontend `static/water/` folder

## Vaccine Instructions

To run the vaccine scripts which are located in `vaccine_region_final.ipynb` you need the following folders
and data: empty folders `vaccine_region/county_vac_by_dimension` and `vaccine_region/state_vac_by_dimension`, and the shapefile data for `backend/data/CA_Counties/CA_Counties_TIGER2016.shp`, `backend/data/states/cb_2018_us_state_500k.shp`, and `backend/data/us_counties/UScounties.shp`. Then run the notebook line by line to get the output of vaccine data in map in the following folders: `backend/vaccine_region/state_vac_by_dimension/state_Age`, `backend/vaccine_region/state_vac_by_dimension/age_maps`, `backend/vaccine_region/state_vac_by_dimension/re_maps`, and `backend/vaccine_region/county_vac_by_dimension/c_maps` which can then be placed into the flask frontend in the corresponding folders

## Front-end Instructions

To run the flask app navigate to the `frontend/flask/` directory and run `python app.py`

For the site to run correctly you need to have all the static data from the backend moved into the `frontend/static/` folder. For your convenience this data can be downloaded from the google drive containing the data sets as it takes a long time to get results and move and name them correctly.

## Members

Group Members:

* Asma Khan asma.khan@email.ucr.edu ( CS225 only )
* Jourdon Freeman jfree010@ucr.edu,
* Hritvik Gupta hgupt010@ucr.edu,
* Manojsai Kalaganti mkala011@ucr.edu,
* Michael Risher mrish001@ucr.edu
