class Pawn():
    def __init__(self, starting_position):
        self.position = starting_position
    
    def get_pos(self):
        return self.position

class Player():
    def __init__(self, nb_pawns=4):
        self.nb_pawns = nb_pawns
        
        self.nb_tiles = 1 + 3 * (self.nb_pawns * (self.nb_pawns - 1))
        
        self.home_base = tuple()

class PlayerWhite(Player):
    def __init__(self, nb_pawns=4):
        super().__init__(nb_pawns=nb_pawns)
        
        self.home_base = tuple(i for i in range(0, self.nb_pawns))
        self.pawns = [Pawn(pos) for pos in self.home_base]


class PlayerBlack(Player):
    def __init__(self, nb_pawns=4):
        super().__init__(nb_pawns=nb_pawns)
        
        self.home_base = tuple(i for i in range(self.nb_tiles - 1, 
                                                self.nb_tiles - 1 - self.nb_pawns, 
                                                -1))
        self.pawns = [Pawn(pos) for pos in self.home_base]
        