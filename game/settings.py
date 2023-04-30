class Settings:
    # Object's ID
    ID_EMPTY = 0
    ID_WALL = 1
    ID_PLAYER = 2
    ID_GOAL = 3
    
    def __init__(self, game):
        self.field_size = 10
        self.fields_y = len(game.board)
        self.fields_x = len(game.board[0])
        self.screen_width = self.field_size * self.fields_x
        self.screen_height = self.field_size * self.fields_y
