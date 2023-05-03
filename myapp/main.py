from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.layouts import layout, row
from bokeh.plotting import figure
#Setting up the figure
p = figure(name="p")
p2 = figure(name="p2")
earth_orbit=p.circle(x=0, y=0, radius=1, line_color='blue',line_alpha=0.5,fill_color=None, line_width=2)
mars_orbit=p2.circle(x=0, y=0, radius=0.7, line_color='red',line_alpha=0.5,fill_color=None, line_width=2)
curdoc().add_root(p)
curdoc().add_root(p2)
curdoc().title = "test app"


