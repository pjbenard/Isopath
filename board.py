import numpy as np
from itertools import chain

class Board():
    def __init__(self, size_board=4):
        self.size_board = size_board
        self.nb_tiles = 1 + 3 * (self.size_board * (self.size_board - 1))
        
        V, E = self.__make_graph__()
        self.graph = {'V': V, 'E': E}
        self.neighbours = self.__make_neighbours_dict__()
        
        self.values = self.__make_values__()
        
    
    def __make_graph__(self):
        def create_link(e1, e2):
            E[e1, e2], E[e2, e1] = 1, 1

        # Init
        n = self.size_board
        nb_tiles = self.nb_tiles
        nb_layers = 2 * n - 1
        V = np.arange(0, nb_tiles, dtype=int)
        E = np.zeros((nb_tiles, nb_tiles), dtype=int)

        # Creation of a matrix of placements
        matrix = []
        first_element = 0
        for layer_size in chain(range(n, nb_layers + 1), 
                                range(nb_layers - 1, n - 1, -1)):
            matrix.append([first_element + i for i in range(0, layer_size)])
            first_element += layer_size

        # Horizontal connections 
        for layer in range(0, nb_layers):
            for tile1, tile2 in zip(matrix[layer][:-1], matrix[layer][1:]):
                create_link(tile1, tile2)

        # Vertical connections
        for diff_layers, RANGE in zip((1, -1), 
                                      (range(0, nb_layers // 2), 
                                       range(nb_layers - 1, nb_layers // 2, -1))):
            for layer in RANGE:
                for tile_idx, tile in enumerate(matrix[layer]):
                    create_link(tile, matrix[layer + diff_layers][tile_idx])
                    create_link(tile, matrix[layer + diff_layers][tile_idx + 1])

        # Teleport connections
        first_tile_mid_layer = ((n - 1) * (3 * n - 2)) // 2
        pairs = ((0, n - 1), 
                 (first_tile_mid_layer, first_tile_mid_layer + nb_layers - 1), 
                 (nb_tiles - n, nb_tiles - 1))

        for tile1, tile2 in pairs:
            create_link(tile1, tile2)
        
        return V, E
    
    def __make_neighbours_dict__(self):
        neighbours = {tile: np.nonzero(self.graph['E'][tile]) for tile in self.graph['V']}
        return neighbours

    def __make_values__(self):
        values = np.zeros(self.nb_tiles, dtype=int)
        values[:self.size_board] = 1
        values[-self.size_board:] = -1
        return values
