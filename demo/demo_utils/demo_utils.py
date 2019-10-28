from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

# Plot choropleth map data from a given classification
# classes: Instance of mapclassify.MapClassifier. Contains already classified
#          data.
# map_ax: matplotlib axis used to plot map
# legend_ax: matplotlib axis used to plot legend
# colors: a list of colors to be used for each class in the choropleth map
def plot_classes(df, classes, fig, map_ax, colors):
    pos = map_ax.get_position()
    legend_rect = [pos.x0, pos.y1 - pos.height + (pos.height / 5), pos.width / 5, pos.width / 5]
    legend_ax = fig.add_axes(legend_rect, label=classes.name)

    cmap = ListedColormap(colors)
    df['classed'] = classes.yb
    df.plot(ax=map_ax, cmap=cmap, column='classed')
    map_ax.set_axis_off()
    map_ax.set_title(classes.name)
    labels = ["{:0.2f}".format(h) for h in classes.bins]
    legend_ax.bar(range(len(classes.bins)), classes.counts, color=colors, align='edge', tick_label=labels, width=-1)
    legend_ax.set_xticklabels(labels, fontdict=None, minor=False, rotation='vertical')

# Define a color map from ColorBrewer that is suitable for passing to plot_classes.
def cmap_yl_or_rd():
    raw_cmap = [
            [255, 255, 178],
            [254, 204, 92],
            [253, 141, 60],
            [240, 59, 32],
            [189, 0, 38]]
    return [[e/255.0 for e in c] for c in raw_cmap] 
