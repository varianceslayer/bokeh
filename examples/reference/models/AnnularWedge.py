import numpy as np

from bokeh.io import curdoc, show
from bokeh.models import AnnularWedge, ColumnDataSource, Grid, LinearAxis, Plot

N = 9
x = np.linspace(-2, 2, N)
y = x**2
r = x/12.0+0.4

source = ColumnDataSource(dict(x=x, y=y, r=r))

plot = Plot(
    title=None, width=300, height=300,
    min_border=0, toolbar_location=None)

glyph = AnnularWedge(x="x", y="y", inner_radius=.2, outer_radius="r", start_angle=0.6, end_angle=4.1, fill_color="#8888ee")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)
