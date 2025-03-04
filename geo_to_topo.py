
import geopandas as gpd
import topojson as tp
import geojson
import argparse
from pathlib import Path

def main(input_file : str, precision : float, string_cols : list[str]):
    """
	input_file: any  geospatial file readable by geopandas.
	precision (optional): the precision of the final map in degrees. This will simplify the geometry and compress it.
    string_cols: columns to cast as string so they don't become floats. Will throw warnings and may not work.
	"""	
    if string_cols is not None:
        gdf = gpd.read_file(input_file, dtypes = {col: 'str' for col in string_cols if string_cols is not None})
    else:
        gdf = gpd.read_file(input_file)
    if precision != 0:
        gdf['geometry'] = gdf.simplify(precision)
    else :
        gdf['geometry'] = gdf.geometry

    gdf.info()
    #convert GeoDataFrame to GeoJson
    this_json = gdf.to_json()

    #convert GeoJSON to TopoJSON
    topo = tp.Topology(this_json)
    
    path = Path(input_file)
    filename = path.stem
    directory = path.parent
    save_path = directory / (filename + '.topojson.json')
    topo.to_json(str(save_path), 'wgs84')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert geography to TopoJSON')
    parser.add_argument('input_geo_file', type=str, help='Input file path to geography. It can be a geojson or a shapefile, or any other geopandas compatable file.')
    #add the optional precision argument
    parser.add_argument('-p', '--precision', type=float, default=0.0001, help='''
                        Simplification precision of the TopoJSON output in decimal degrees. 
                        The default is 0.0001 degrees which is around 8 to 11 meters. Enter 0 to disable simplification''')
    parser.add_argument('-s', "--string_cols", nargs='+', help='List of columns to convert to string')
    args = parser.parse_args()
    input_file = args.input_geo_file
    precision = args.precision
    string_cols = args.string_cols
    main(input_file, precision, string_cols)
