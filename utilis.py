import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler as SS
import umap
from matplotlib import pyplot as plt
from kneed import KneeLocator
from sklearn.decomposition import TruncatedSVD
from sklearn.mixture import GaussianMixture
import time
from sklearn.preprocessing import normalize
from scipy import sparse
from collections import Counter


# colormap for ploting
def discrete_cmap(N, base_cmap=None):
    """Create an N-bin discrete colormap from the specified input map"""
    base = plt.cm.get_cmap(base_cmap)
    color_list = base(np.linspace(0, 1, N))
    cmap_name = base.name + str(N)
    return base.from_list(cmap_name, color_list, N)

