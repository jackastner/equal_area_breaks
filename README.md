# Equal Area Breaks

Equal area breaks, occasionally known as geographic quantiles, is a data
classification method for choropleth maps that ensures the total area of each
class is approximately equal. This package provides algorithms to compute this
classification and integrates the algorithms with [mapclassify][1] so that it
can be used with the full [pysal][2] package suit.

The algorithms implemented in this package are from not yet published paper
[Equal-area Breaks: A Classification Scheme for Data to Obtain an Evenly-colored Choropleth Map][3]

## Package Usage

Example usage of this package is show in the `demo` directory. The demos require,
in addition to this package, geopandas, descartes, and matplotlib. Execute the
following to install these packages.

```
pip install . geopandas matplotlib descartes
```

You should then be able to execute the demo python scripts.

```
python demos/world_population.py
```

[1]: https://pysal.org/mapclassify/
[2]: https://pysal.org/pysal/
[3]: https://www.cs.umd.edu/sites/default/files/scholarly_papers/Abboud.pdf
