import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import os
import geopandas as gpd
from shapely.geometry import Point


# %% [code] {"execution":{"iopub.status.busy":"2023-12-07T18:24:43.823515Z","iopub.execute_input":"2023-12-07T18:24:43.823958Z","iopub.status.idle":"2023-12-07T18:30:23.127122Z","shell.execute_reply.started":"2023-12-07T18:24:43.823921Z","shell.execute_reply":"2023-12-07T18:30:23.125706Z"}}
water_dataset_path = '/kaggle/input/flu-dataset/field_results.csv'
preprocessed_water_data_path = "/kaggle/input/flu-dataset/water_spatial_join_output.csv"
flu_by_county = "/kaggle/input/flu-dataset/flu_by_county.csv"
combined_flu_water_contamination_data = '/kaggle/working/flu_water_combined.csv'
counties_shapefile_path = '/kaggle/input/flu-dataset/CA_Counties_TIGER2016.shp'
output_dir = '/kaggle/working/heatmaps_final_results'  # Use the correct path for your Kaggle notebook
os.makedirs(output_dir, exist_ok=True)
zip_file_path = "/kaggle/working"
zip_file_name = 'heatmaps_final_results.zip'


water_data = pd.read_csv(water_dataset_path, low_memory=False)
water_data['sample_date'] = pd.to_datetime(water_data['sample_date'], errors='coerce')

water_data.dropna(subset=['sample_date', 'latitude', 'longitude'], inplace=True)
water_data = water_data[water_data['sample_date'].dt.year >= 2001]


# Create geometry points
water_data['geometry'] = water_data.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

# Convert the DataFrame to a GeoDataFrame and set its CRS
gdf_water = gpd.GeoDataFrame(water_data, geometry='geometry')
gdf_water.set_crs(epsg=4326, inplace=True)

ca_counties = gpd.read_file(counties_shapefile_path)
ca_counties = ca_counties.to_crs(gdf_water.crs)
ca_counties['COUNTYNS'] = ca_counties['COUNTYNS'].str.lstrip('0')
## Uncommend=t below code if wanna calculate gdf spatial_join
# gdf_your_data = gpd.GeoDataFrame(
#     water_data,
#     geometry=gpd.points_from_xy(water_data.longitude, water_data.latitude)
# )

# gdf_your_data.set_crs(epsg=4326, inplace=True)  

# gdf_ca_map = gpd.read_file("/kaggle/input/flu-dataset/CA_Counties_TIGER2016.shp")
# gdf_your_data['geometry'] = gdf_your_data.geometry.buffer(0.0001)  # Buffer by 0.0001 degrees

# if gdf_your_data.crs != gdf_ca_map.crs:
#     gdf_your_data = gdf_your_data.to_crs(gdf_ca_map.crs)

# gdf_spatial_join = gpd.sjoin(gdf_your_data, gdf_ca_map[['COUNTYNS', 'geometry']], how='left', op='intersects')

## Load Already pre-processed data by us
gdf_spatial_join = pd.read_csv(preprocessed_water_data_path)

selected_columns = ['sample_date', 'parameter', 'fdr_result', 'COUNTYNS']
gdf_spatial_join = gdf_spatial_join[selected_columns]
df = gdf_spatial_join
df['year'] = pd.to_datetime(df['sample_date']).dt.year
yearly_data = df.groupby(['year', 'parameter', 'COUNTYNS'])['fdr_result'].mean().reset_index()

df_flu = pd.read_csv(flu_by_county)
df_flu['year'] = pd.to_datetime(df_flu['weekending'], format='%m/%d/%Y', errors='coerce').dt.year
annual_flu_data = df_flu.groupby(['year', 'region']).agg({
    'Total_ILI': 'sum', 
    'Total_Patients_Seen': 'sum',
    'Percent_ILI': 'mean', 
    'Number_Providers_Reporting': 'sum' 
}).reset_index()
annual_flu_data
def safe_convert_to_int(value, default=0):
    try:
        return int(float(value))
    except ValueError:
        return default
df['region'] = gdf_spatial_join['COUNTYNS'].apply(safe_convert_to_int).astype(str)
df.drop("COUNTYNS", axis = 1, inplace = True)
df_flu['region'] = df_flu['region'].str.lstrip('0')
df_flu.drop("season", axis = 1, inplace = True)
df['region'] = df['region'].astype(str)
df_flu['region'] = df_flu['region'].astype(str)
combined_data = pd.merge(df, df_flu, on=['region', 'year'], how='left')

combined_data.to_csv(combined_flu_water_contamination_data', index=False)

# %% [code] {"execution":{"iopub.status.busy":"2023-12-07T22:14:30.127575Z","iopub.execute_input":"2023-12-07T22:14:30.128427Z","iopub.status.idle":"2023-12-07T22:19:42.866637Z","shell.execute_reply.started":"2023-12-07T22:14:30.128391Z","shell.execute_reply":"2023-12-07T22:19:42.865085Z"}}
combined_data['region'] = combined_data['region'].astype(str)

ca_counties['COUNTYNS'] = ca_counties['COUNTYNS'].astype(str)

gdf_combined = combined_data.merge(ca_counties, left_on='region', right_on='COUNTYNS')

gdf_combined = gpd.GeoDataFrame(gdf_combined, geometry='geometry')

heatmap_files = []
unique_years = gdf_combined['year'].unique()
unique_parameters = gdf_combined['parameter'].unique()

heatmap_files = []
for year in unique_years:
    for parameter in unique_parameters:
        data_filtered = gdf_combined[(gdf_combined['parameter'] == parameter) & (gdf_combined['year'] == year)]
        
        fig, ax = plt.subplots(1, figsize=(10, 10))
        data_filtered.plot(column='fdr_result', ax=ax, cmap='viridis', legend=True,
                           legend_kwds={'label': "FDR", 'orientation': "horizontal"})
        plt.title(f'Average FDR of {parameter} for {year}')
        plt.axis('off')
        heatmap_filename_fdr = f'heatmap_fdr_{parameter}_{year}.png'
        plt.show()
        plt.savefig(os.path.join(output_dir, heatmap_filename_fdr), dpi=300)
        plt.close()
        heatmap_files.append(os.path.join(output_dir, heatmap_filename_fdr))

        fig, ax = plt.subplots(1, figsize=(10, 10))
        data_filtered.plot(column='Total_ILI', ax=ax, cmap='Reds', legend=True,
                           legend_kwds={'label': "Total ILI", 'orientation': "horizontal"})
        plt.title(f'Average Total ILI of {parameter} for {year}')
        plt.axis('off')
        heatmap_filename_ili = f'heatmap_ili_{parameter}_{year}.png'
        plt.savefig(os.path.join(output_dir, heatmap_filename_ili), dpi=300)
        plt.close()
        
        parameter_safe = parameter.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
        heatmap_filename = f'{parameter_safe}_{year}.png'
        heatmap_path = os.path.join(output_dir, heatmap_filename)
        plt.savefig(heatmap_path, dpi=300)
        plt.close()
        heatmap_files.append(heatmap_path)

zip_filepath = os.path.join(zip_file_path, zip_file_name)
with zipfile.ZipFile(zip_filepath, 'w') as zipf:
    for file in heatmap_files:
        zipf.write(file, os.path.basename(file))
