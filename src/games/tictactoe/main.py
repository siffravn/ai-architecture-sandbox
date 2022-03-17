from src.ai.games.minimax import minmax_decision
from src.games.tictactoe.tictactoe import TicTacToe
from src.ai.core.agent import TraceAgent
from src.ai.core.program import Program
from src.ai.games.gameagent import GameAgent
from src.ai.games.player import QueryPlayer

game = TicTacToe()

program = Program(game, minmax_decision)
agent = GameAgent(program)
agent2 = GameAgent(program)

player = QueryPlayer()

game.play_game(players=(player, TraceAgent(agent)))

# game.play_game(players=(agent2, agent))