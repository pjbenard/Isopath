from player import Player

class PlayerWhite(Player):
    def __init__(self, nb_pawns=4):
        super().__init__(nb_pawns=nb_pawns)
        
        self.home_base = tuple(i for i in range(0, self.nb_pawns))
