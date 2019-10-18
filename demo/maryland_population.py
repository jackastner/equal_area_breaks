import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize, ListedColormap
import geopandas
import equal_area_breaks
import mapclassify


# Color map from ColorBrewer
raw_cmap = [
        [255, 255, 178],
        [254, 204, 92],
        [253, 141, 60],
        [240, 59, 32],
        [189, 0, 38]]
raw_cmap = [[e/255.0 for e in c] for c in raw_cmap] 
cmap = ListedColormap(raw_cmap)

md = geopandas.read_file('data/Maryland_Census_Data__Census_Tracts.shp')
data_col = 'PSQM'

fig, axes = plt.subplots(nrows = 2, ncols = 2)

classes = mapclassify.NaturalBreaks(md[data_col])
labels = ["{:0.2f} -\n{:0.2f}".format(l,h) for (l,h) in zip([0]+list(classes.bins), classes.bins)]
md['classed'] = classes.yb
md.plot(ax=axes[0,0], cmap=cmap, column='classed')
axes[0,0].set_title('Natural Breaks')
axes[0,1].bar(range(len(classes.bins)), classes.counts, color=raw_cmap, tick_label=labels, width=1)

classes = equal_area_breaks.Equal_Area_DP(md[data_col], area=md.geometry.area)
labels = ["{:0.2f} -\n{:0.2f}".format(l,h) for (l,h) in zip([0]+list(classes.bins), classes.bins)]
md['classed'] = classes.yb
md.plot(ax=axes[1,0], cmap=cmap, column='classed')
axes[1,0].set_title('Equal Area')
axes[1,1].bar(range(len(classes.bins)), classes.counts, color=raw_cmap, tick_label=labels, width=1)

plt.show()
