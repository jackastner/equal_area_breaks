import matplotlib.pyplot as plt
import geopandas
import equal_area_breaks
import mapclassify

from demo_utils import *

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")]
world['gdp_per_cap'] = 1000000 * (world.gdp_md_est / world.pop_est)
world = world.to_crs({'proj': 'wintri'})
world['area'] = world.geometry.area

data_col='gdp_per_cap'
cmap = cmap_yl_or_rd()

fig, axes = plt.subplots(nrows = 4, ncols = 2)

plot_classes(world, mapclassify.Quantiles(world[data_col]), axes[0,0], axes[0,1], cmap)
plot_classes(world, mapclassify.EqualInterval(world[data_col]), axes[1,0], axes[1,1], cmap)
plot_classes(world, mapclassify.NaturalBreaks(world[data_col]), axes[2,0], axes[2,1], cmap)
plot_classes(world, equal_area_breaks.Equal_Area_DP(world[data_col], area=world['area']), axes[3,0], axes[3,1], cmap)

plt.show()
