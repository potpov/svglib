import json
import sys
import os
from PIL import Image, ImageDraw
from svglib.geom import Point
from svglib.svg import SVG

root_dir = os.path.join(os.path.abspath(os.getcwd()), "svglib")
sample_dir = os.path.join(root_dir, "samples")
coords = json.load(open(os.path.join(sample_dir, "placing.json")))  # a file that tells you where to place a series of SVGs in a canvas 

svg_path = os.path.join(sample_dir, coords["house_body"]["file"])
svg = SVG.load_svg(svg_path)
print("done.")