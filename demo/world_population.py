import matplotlib.pyplot as plt
import geopandas
import equal_area_breaks

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")]
world = world.to_crs({'proj': 'wintri'})
world['area'] = world.geometry.area

fig, axes = plt.subplots(nrows = 2, ncols = 2)

world.plot(ax=axes[0,0], edgecolor='black', cmap='OrRd', column='pop_est', scheme='quantiles')
world.plot(ax=axes[0,1], edgecolor='black', cmap='OrRd', column='pop_est', scheme='equal_area_greedy', classification_kwds={'area': world.area})
world.plot(ax=axes[1,0], edgecolor='black', cmap='OrRd', column='pop_est', scheme='equal_area_greedy2', classification_kwds={'area': world.area})
world.plot(ax=axes[1,1], edgecolor='black', cmap='OrRd', column='pop_est', scheme='equal_area_dp', classification_kwds={'area': world.area})
plt.show()
