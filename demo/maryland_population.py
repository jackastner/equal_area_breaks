import matplotlib.pyplot as plt
import geopandas
import equal_area_breaks
import mapclassify

from demo_utils import *

md = geopandas.read_file('data/Maryland_Census_Data__Census_Tracts.shp')
data_col = 'PSQM'
cmap = cmap_yl_or_rd()

fig, axes = plt.subplots(nrows = 4, ncols = 2)

plot_classes(md, mapclassify.Quantiles(md[data_col]), axes[0,0], axes[0,1], cmap)
plot_classes(md, mapclassify.EqualInterval(md[data_col]), axes[1,0], axes[1,1], cmap)
plot_classes(md, mapclassify.NaturalBreaks(md[data_col]), axes[2,0], axes[2,1], cmap)
plot_classes(md, equal_area_breaks.Equal_Area_DP(md[data_col], area=md.geometry.area), axes[3,0], axes[3,1], cmap)

plt.show()
