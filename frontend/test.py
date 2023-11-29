import folium
from folium.plugins import HeatMapWithTime

# Create a map object
m = folium.Map(location=[37.7749, -122.4194], zoom_start=1)

# Create a list of data points with timestamps
data_points = [
    [37.7749, -122.4194, "2023-01-01T12:00:00"],
    [38.7749, -122.4194, "2023-01-01T12:00:00"],
    [39.7749, -122.4194, "2023-01-01T12:00:00"],
    [40.7749, -122.4194, "2023-01-01T12:00:00"],
    [37.7749, -121.4194, "2023-01-01T12:00:00"],
    [37.7749, -120.4194, "2023-01-01T12:00:00"],
    [37.7749, -119.4194, "2023-01-01T12:00:00"],
    [37.7749, -118.4194, "2023-01-01T12:00:00"],
    [37.7749, -117.4194, "2023-01-01T12:00:00"],
    [37.7749, -116.4194, "2023-01-01T12:00:00"],
    [37.7749, -115.4194, "2023-01-01T12:00:00"],
    [37.7749, -114.4194, "2023-01-01T12:00:00"],
    [37.7749, -113.4194, "2023-01-01T12:00:00"],
    [37.7749, -112.4194, "2023-01-01T12:00:00"],
    [37.7749, -111.4194, "2023-01-01T12:00:00"],
    [37.7749, -110.4194, "2023-01-01T12:00:00"],
    [37.7749, -122.4194, "2023-01-01T12:00:00"],
    [37.7749, -122.4194, "2023-01-02T14:30:00"],
    [37.7749, -122.4294, "2023-01-03T10:15:00"],
    [37.7649, -122.4194, "2023-01-04T16:45:00"],
    [37.7549, -122.4194, "2023-01-05T08:20:00"],
    [37.7749, -122.4194, "2023-01-06T17:30:00"],
    [37.7849, -122.4194, "2023-01-07T09:10:00"],
    # Add more data points with the same format
]

# Create a HeatMapWithTime layer
HeatMapWithTime(data_points).add_to(m)

# Save the map to an HTML file
m.save("flask/templates/heatmap.html")