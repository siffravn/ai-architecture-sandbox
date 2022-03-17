class Player():

    def make_move(self, game, state):
        raise NotImplementedError
    
class QueryPlayer(Player):

    def make_move(self, game, state):
        """Make a move by querying standard input."""
        print("current state:")
        game.display(state)
        print("available moves: {}".format(game.actions(state)))
        print("")
        move = None
        if game.actions(state):
            move_string = input('Your move? ')
            try:
                move = eval(move_string)
            except NameError:
                move = move_string
        else:
            print('no legal moves: passing turn to next player')
        return move