#!/usr/bin/env python

"""Tests for `leafmap` module."""

import os
import unittest
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
from unittest.mock import patch


class TestFoliumap(unittest.TestCase):
    """Tests for `foliumap` module."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_add_basemap(self):
        """Check basemaps"""
        m = leafmap.Map()
        m.add_basemap("TERRAIN")
        out_str = m.to_html()
        assert "Google Terrain" in out_str


    def test_add_geojson(self):
        """Check GeoJSON"""
        m = leafmap.Map()
        in_geojson = "https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/cable_geo.geojson"
        m.add_geojson(in_geojson, layer_name="Cable lines")
        out_str = m.to_html()
        assert "Cable lines" in out_str

    def test_add_kml(self):
        """Check KML"""
        m = leafmap.Map()
        in_kml = "https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/us_states.kml"
        m.add_kml(in_kml, layer_name="US States KML")
        out_str = m.to_html()
        assert "US States KML" in out_str


    def test_add_tile_layer(self):
        """Check adding tile layer"""
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
        with self.assertRaises(NotImplementedError):
            m = leafmap.Map()
            url = "https://www.mrlc.gov/sites/default/files/NLCD_Colour_Classification_Update.jpg"
            bounds = [(28, -128), (35, -123)]
            m.image_overlay(url=url, bounds=bounds, name="NLCD legend")
            out_str = m.to_html()
            assert "NLCD legend" in out_str

    def test_layer_opacity(self):
        """Check layer opacity"""
        with self.assertRaises(NotImplementedError):
            m = leafmap.Map()
            m.layer_opacity("OpenStreetMap", 0.5)
            layer = m.find_layer("OpenStreetMap")
            self.assertEqual(layer.opacity, 0.5)

 

if __name__ == "__main__":
    unittest.main()