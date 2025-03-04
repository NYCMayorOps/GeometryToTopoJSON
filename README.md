#######################################
# Geometry To Topo JSON Converter #
###        By Steve Scott           ###
#######################################

# Converting a geospatial file to a topojson #
## Why convert to a TopoJSON? ##
Most geojson files are coordinate based. A topoJSON uses a series of arcs to store its geometry. Why use TopoJSON? Because PowerBI's Shape Map visulaization component only works with TopoJSON files.

## requirements ###
```bash
pip install requirements.txt
```
To use:

```powershell
python \Path\To\repo\convert_to_topo.py \path\of\file\to\convert\<filename>.geojson
```

This will generate a file named <filename>_topojson.json

arguments:
### 'input_geo_file' ###
- type: string , 
- Input file path to geography. It can be a geojson, a zipped shapefile, or any other geopandas compatable file

### '-p', '--precision' ###
- type : float
- default=0.0001 
- Simplification precision of the TopoJSON output in decimal degrees. The default is 0.0001 degrees which is around 8 to 11 meters. Enter 0 to disable simplification.

### '-s', "--string_cols" ###
- type: list of strings 
- List of columns to convert to string. This may help if you have something like "Police Precinct" which is "1" or "32" which should be a string but is read as a float. This will attempt to coerce it to a str.
- Note, string columns will raise warnings that it is not supported. It may work on GeoJSON, it won't work on Shapefiles.
- If the coercion fails the program will still output a topojson, it will ignore this parameter import and cast it automatically to whatever geopandas sees fit.
