from matplotlib.colors import ListedColormap

# Plot choropleth map data from a given classification
# classes: Instance of mapclassify.MapClassifier. Contains already classified
#          data.
# map_ax: matplotlib axis used to plot map
# legend_ax: matplotlib axis used to plot legend
# colors: a list of colors to be used for each class in the choropleth map
def plot_classes(df, classes, map_ax, legend_ax, colors):
    cmap = ListedColormap(colors)
    labels = ["{:0.2f} -\n{:0.2f}".format(l,h) for (l,h) in zip([0]+list(classes.bins), classes.bins)]
    df['classed'] = classes.yb
    df.plot(ax=map_ax, cmap=cmap, column='classed')
    map_ax.set_axis_off()
    map_ax.set_title(classes.name)
    legend_ax.bar(range(len(classes.bins)), classes.counts, color=colors, tick_label=labels, width=1)

# Define a color map from ColorBrewer that is suitable for passing to plot_classes.
def cmap_yl_or_rd():
    raw_cmap = [
            [255, 255, 178],
            [254, 204, 92],
            [253, 141, 60],
            [240, 59, 32],
            [189, 0, 38]]
    return [[e/255.0 for e in c] for c in raw_cmap] 
