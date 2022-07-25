import sys
from pyheat import PyHeat
ph = PyHeat(sys.argv[1])
ph.create_heatmap()
# To view the heatmap.
ph.show_heatmap()
# To output the heatmap as a file.