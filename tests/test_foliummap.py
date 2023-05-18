#!/usr/bin/env python

"""Tests for `leafmap` module."""


import unittest
import logging
import leafmap.foliumap as leafmap

class TestFoliumap(unittest.TestCase):
    """Tests for `foliumap` module."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.logger = logging.getLogger(__name__)


    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_add_basemap(self):
        """Check basemaps"""
        self.logger.info("Running test_add_basemap")
        m = leafmap.Map()
        m.add_basemap("TERRAIN")
        out_str = m.to_html()
        assert "Google Terrain" in out_str


    def test_add_geojson(self):
        """Check GeoJSON"""
        self.logger.info("Running test_add_geojson")
        m = leafmap.Map()
        in_geojson = "https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/cable_geo.geojson"
        m.add_geojson(in_geojson, layer_name="Cable lines")
        out_str = m.to_html()
        assert "Cable lines" in out_str


    def test_add_tile_layer(self):
        """Check adding tile layer"""
        self.logger.info("Running test_add_tile_layer")
        m = leafmap.Map()
        m.add_tile_layer(
            url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            name="Google Satellite",
            attribution="Google",
        )
        out_str = m.to_html()
        assert "Google Satellite" in out_str

 
    def test_image_overlay(self):
        """Check image overlay"""
        self.logger.info("Running test_image_overlay")
        with self.assertRaises(NotImplementedError):
            m = leafmap.Map()
            url = "https://www.mrlc.gov/sites/default/files/NLCD_Colour_Classification_Update.jpg"
            bounds = [(28, -128), (35, -123)]
            m.image_overlay(url=url, bounds=bounds, name="NLCD legend")
            out_str = m.to_html()
            assert "NLCD legend" in out_str

    def test_layer_opacity(self):
        """Check layer opacity"""
        self.logger.info("Running test_layer_opacity")
        with self.assertRaises(NotImplementedError):
            m = leafmap.Map()
            m.layer_opacity("OpenStreetMap", 0.5)
            layer = m.find_layer("OpenStreetMap")
            self.assertEqual(layer.opacity, 0.5)

 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[logging.FileHandler("test.log"), logging.StreamHandler()])
    
    suite = unittest.TestSuite()
    suite.addTest(TestFoliumap('test_add_basemap'))
    suite.addTest(TestFoliumap('test_add_geojson'))
    suite.addTest(TestFoliumap('test_add_tile_layer'))
    suite.addTest(TestFoliumap('test_image_overlay'))
    suite.addTest(TestFoliumap('test_layer_opacity'))

    runner = unittest.TextTestRunner()
    results = runner.run(suite)
    print('Tests passed:', results.testsRun - len(results.failures) - len(results.errors))
    print('Tests failed:', len(results.failures) + len(results.errors))
    # unittest.main(testRunner=runner)