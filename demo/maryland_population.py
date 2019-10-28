import matplotlib.pyplot as plt
import geopandas
import equal_area_breaks
import mapclassify

from demo_utils import *

md = geopandas.read_file('data/Maryland_Census_Data__Census_Tracts.shp')
data_col = 'PSQM'
cmap = cmap_yl_or_rd()

fig, axes = plt.subplots(nrows = 2, ncols = 2)

plot_classes(md, mapclassify.Quantiles(md[data_col]), fig, axes[0,0], cmap)
plot_classes(md, mapclassify.EqualInterval(md[data_col]), fig, axes[0,1], cmap)
plot_classes(md, mapclassify.NaturalBreaks(md[data_col]), fig, axes[1,0], cmap)
plot_classes(md, equal_area_breaks.Equal_Area_DP(md[data_col], area=md.geometry.area), fig, axes[1,1], cmap)

plt.show()
