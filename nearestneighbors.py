from annoy import AnnoyIndex
from scipy import spatial
from nltk import ngrams
import random, json, glob, os, codecs, random
import numpy as np
def getNearestNeighbor(filename):
    # data structures
    file_index_to_file_name = {}
    file_index_to_file_vector = {}
    chart_image_positions = {}

    # config
    dims = 2048
    n_nearest_neighbors = 2
    trees = 10000
    infiles = glob.glob('tile_vectors/*.npz')


    # build ann index
    t = AnnoyIndex(dims)
    for file_index, i in enumerate(infiles):
        saved_index = file_index
        file_vector = np.loadtxt(i)
        file_name = os.path.basename(i).split('.')[0]
        file_index_to_file_name[file_index] = file_name
        file_index_to_file_vector[file_index] = file_vector
        t.add_item(file_index, file_vector)

    saved_index += 1
    file_vector = np.loadtxt(filename)
    file_name = os.path.basename(filename).split('.')[0]
    file_index_to_file_name[saved_index] = file_name
    file_index_to_file_vector[saved_index] = file_vector
    t.add_item(saved_index, file_vector)
    t.build(trees)

    nearest_neighbors = t.get_nns_by_item(saved_index, n_nearest_neighbors)
    #return file index for nearest neighbor
    return nearest_neighbors[1]
