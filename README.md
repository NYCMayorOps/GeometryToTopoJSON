#######################################
### Geometry To Topo JSON Converter ###
###        By Steve Scott           ###
#######################################

# converting a geospatial file to a topojson. #
## Why convert to a TopoJSON? ##
Most geojson files are coordinate based. A topoJSON uses a series of arcs to store its geometry. Why use TopoJSON? Because PowerBI's Shape Map visulaization component only works with TopoJSON files.

## requirements ###
```bash
pip install geopandas==1.0.1
pip install topojson
pip install geojson
pip install pytest
```
To use:

```powershell
python \Path\To\repo\convert_to_topo.py \path\of\file\to\convert\<filename>.geojson
```

This will generate a file named <filename>_topojson.json

arguments:
- 'input_geo_file', 
-- type: string , 
-- Input file path to geography. It can be a geojson or a shapefile, or any other geopandas compatable file
    
- '-p', '--precision', 
-- type : float
-- default=0.0001 

-- Simplification precision of the TopoJSON output in decimal degrees. The default is 0.0001 degrees which is around 8 to 11 meters. Enter 0 to disable simplification.

- '-s', "--string_cols"
-- type: list of strings 
-- List of columns to convert to string.
