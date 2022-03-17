from src.ai.core.agent import Agent
from src.ai.games.player import Player


class GameAgent(Agent, Player):

    def make_move(self, game, state):
        return self.program(state)