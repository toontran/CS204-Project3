from ipyleaflet import *
from main import *

poly = Polygon(
    locations = [(42, -49), (43, -49), (43, -48)],
    color = "red",
    fill_color = "red"
)

m = Map(center=[42.5531, -48.6914], zoom=6)

m.add_layer(poly)

m
