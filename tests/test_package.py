import unittest
import leafmap.foliumap as leafmap
from folium.plugins import FloatImage
from folium.raster_layers import ImageOverlay

def display_map(center, zoom, geo_json, orthomosaic, layer_title, legend_url, detected=False, opacity=0.7):
    
    """
    Display a map with a satellite tile layer, an orthomosaic image, a health indicator layer,
    and a legend image. 

    Parameters
    ----------
    center: tuple
        A tuple of two floats representing the latitude and longitude of the map center.
    zoom: int
        An integer representing the initial zoom level of the map.
    geo_json: dict
        A GeoJSON object representing the health indicator layer.
    orthomosaic: str
        The URL or path to the orthomosaic image to be displayed on the map.
    layer_title: str
        The name of the orthomosaic layer to be displayed on the map.
    legend_url: str
        The URL or path to the legend image to be displayed on the map.
    detected: bool, optional
        If True, the health indicator layer will be displayed on the map. Default is False.
    opacity: float, optional
        The initial opacity of the orthomosaic layer. Default is 0.7.

    Returns
    -------
    leafmap.Map
        The generated map object.
    """


    map = leafmap.Map(center = center, zoom=zoom)
    map.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
    )

    if detected:
        map.add_geojson(geo_json, layer_name="Health Indicator")

    ImageOverlay(orthomosaic,
                [[33.672652308289614,73.12770497102615], [33.67436783460362,73.1307913403036]],
                opacity=opacity, name=layer_title
                ).add_to(map)
    
    FloatImage(legend_url, bottom=30, left=90, width=10).add_to(map)

    return map 

class MyTest(unittest.TestCase):
    def test_display_map():
        center = (33.6739, 73.1151)
        zoom = 16
        geo_json = {"type": "FeatureCollection", "features": []}
        orthomosaic = "https://example.com/orthomosaic.png"
        layer_title = "Orthomosaic Layer"
        legend_url = "https://example.com/legend.png"
        detected = True
        opacity = 0.5

        map = display_map(center, zoom, geo_json, orthomosaic, layer_title, legend_url, detected, opacity)
        print(map)
        assert isinstance(map, leafmap.Map)
        assert map.location == center
        assert map.zoom == zoom
        assert len(map.layers) == 3
        assert map.layers[0].name == "Google Satellite"
        assert map.layers[1].name == "Health Indicator"
        assert map.layers[2].name == layer_title
        assert isinstance(map.layers[2], ImageOverlay)
        assert map.layers[2].url == orthomosaic
        assert isinstance(map.layers[2]._bounds, list)
        assert map.layers[2].opacity == opacity
        assert isinstance(map.layers[3], FloatImage)
        assert map.layers[3].url == legend_url
        
    def test_subtraction(self):
        self.assertEqual(5-3, 2)
        
    def test_multiplication(self):
        self.assertEqual(2*3, 6)
        
if __name__ == '__main__':
    # Create a TestSuite object
    suite = unittest.TestSuite()
    
    # Add the tests to the TestSuite object
    suite.addTest(MyTest('test_display_map'))
    suite.addTest(MyTest('test_subtraction'))
    suite.addTest(MyTest('test_multiplication'))
    
    # Create a TextTestRunner object
    runner = unittest.TextTestRunner()
    
    # Run the tests and get the results
    results = runner.run(suite)
    
    # Print the number of tests passed and failed
    print('Tests passed:', results.testsRun - len(results.failures) - len(results.errors))
    print('Tests failed:', len(results.failures) + len(results.errors))