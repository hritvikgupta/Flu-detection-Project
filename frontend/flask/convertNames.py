import datetime
import os

def convertFilename( filename ):
    # Extract the date part of the filename
    datePart = filename.split( '.') [0]

    # Parse the date
    dateObj = datetime.datetime.strptime(datePart, '%Y-%m-%d')

    # Get the year and the week number
    year = dateObj.strftime( '%Y' )
    weekNumber = dateObj.isocalendar()[1]

    # Format the new filename
    new_filename = f"{year}{weekNumber:02d}.png"
    return new_filename

dir = 'static/fluRegionMaps/pred_maps/'
l = set()
for filename in os.listdir( dir ):
    if filename.endswith( '.png' ):
        newName = convertFilename( filename )
        if newName in l:
          print( f"{newName} already exists from {filename}" )
        l.add( newName )
        try:
          os.rename( os.path.join( dir, filename ), os.path.join( dir, newName ) )
        except OSError as e:
          print( e )
        print( f"Renamed {filename} to {newName}" )
