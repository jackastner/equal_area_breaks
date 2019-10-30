import matplotlib.pyplot as plt
import geopandas
import equal_area_breaks
import mapclassify

from demo_utils import *

md = geopandas.read_file('data/Maryland_Census_Data__Census_Tracts.shp')
data_col = 'PSQM'
cmap = cmap_yl_or_rd()

fig, axes = plt.subplots(nrows = 3, ncols = 2)

plot_classes(md, equal_area_breaks.Equal_Area_Weighted_DP(md[data_col], area=md.geometry.area, w=0.0), fig, axes[0,0], cmap)
plot_classes(md, equal_area_breaks.Equal_Area_Weighted_DP(md[data_col], area=md.geometry.area, w=0.25), fig, axes[0,1], cmap)
plot_classes(md, equal_area_breaks.Equal_Area_Weighted_DP(md[data_col], area=md.geometry.area, w=0.50), fig, axes[1,0], cmap)
plot_classes(md, equal_area_breaks.Equal_Area_Weighted_DP(md[data_col], area=md.geometry.area, w=0.75), fig, axes[1,1], cmap)
plot_classes(md, equal_area_breaks.Equal_Area_Weighted_DP(md[data_col], area=md.geometry.area, w=1.00), fig, axes[2,0], cmap)

plt.show()
