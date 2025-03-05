import json
import sys
import os
from PIL import Image, ImageDraw
from svglib.geom import Point
from svglib.svg import SVG

root_dir = os.path.join(os.path.abspath(os.getcwd()), "svglib")
sample_dir = os.path.join(root_dir, "samples")

coords = {
    "car_body": {
        "file": "square_lines.svg",
        "bounding_box": [20, 60, 108, 100]  # Main car body
    },
    "car_top": {
        "file": "square_lines.svg",
        "bounding_box": [40, 30, 88, 60]  # Smaller top section (like a windshield/cabin)
    },
    "wheel_1": {
        "file": "circle.svg",
        "bounding_box": [30, 90, 50, 110]  # Left wheel
    },
    "wheel_2": {
        "file": "circle.svg",
        "bounding_box": [80, 90, 100, 110]  # Right wheel
    },
    "front_window": {
        "file": "square_lines.svg",
        "bounding_box": [50, 35, 65, 55]  # Front windshield
    },
    "rear_window": {
        "file": "square_lines.svg",
        "bounding_box": [65, 35, 80, 55]  # Rear windshield
    }
}

# let's take the first square, and scale it to fit its bounding box in the canvas
def compute_scale(x1, y1, x2, y2, orig_w=128, orig_h=128):
    new_w, new_h = (x2 - x1, y2 - y1)  # the size of the bounding box
    width_ratio = new_w / orig_w
    height_ratio = new_h / orig_h
    return width_ratio, height_ratio



def composite(coords):
    composite = SVG([], (128, 128), width=128, height=128)
    for shape in coords.values():
        svg_path = os.path.join(sample_dir, shape["file"])
        svg = SVG.load_svg(svg_path)
        
        (x1, y1, x2, y2) = shape["bounding_box"]
        (_x1, _y1), (_x2, _y2) = svg.bbox()
        
        # compute width and height for the box rather than the full image
        _w, _h = _x2 - _x1, _y2 - _y1
        width_ratio, height_ratio = compute_scale(x1, y1, x2, y2, _w, _h)

        target_center = Point((x1 + x2) // 2, (y1 + y2) // 2)
        
        svg.scale((width_ratio, height_ratio))
        svg.translate(-svg.viewbox.center)
        svg.translate(target_center)
        composite = composite + svg 
    return composite

result = composite(coords)





print("done.")