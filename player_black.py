from player import Player

class PlayerBlack(Player):
    def __init__(self, nb_pawns=4):
        super().__init__(nb_pawns=nb_pawns)
        
        self.home_base = tuple(i for i in range(self.nb_tiles - 1, 
                                                self.nb_tiles - 1 - self.nb_pawns, 
                                                -1))
