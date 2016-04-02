from Player import Player
from State import State
from Problem import Problem
import time
from DepthFirstSearch import DepthFirstSearch
from BreadthFirstSearch import BreadthFirstSearch
from BestFirstSearch import BestFirstSearch


class AIPlayer(Player):
    def __init__(self, map):
        Player.__init__(self, map)
        self.searchAlgorithm = 0

    def setSearchAlgorithm(self, searchAlgorithm):
        if searchAlgorithm == "dfs":
            self.searchAlgorithm = DepthFirstSearch()
        elif searchAlgorithm == "bfs":
            self.searchAlgorithm = BreadthFirstSearch()
        elif searchAlgorithm == "astar":
            self.searchAlgorithm = BestFirstSearch()

    def play(self):
        mapp = self.map.getMapState()

        # generate problem to solve
        problem = Problem(State(mapp))

        # set problem
        self.searchAlgorithm.setProblem(problem)

        # calculate running time
        start = time.time()

        # solve problem
        self.map.loadInfo("solving")
        moves = self.searchAlgorithm.solve()
        if moves != []: self.map.loadInfo("found")
        else: self.map.loadInfo("notfound")

        # stop time
        stop = time.time()

        # print some statistics
        print "Thoi gian giai quyet : %d giay" %(stop - start)
        print "So luong move la : %d" %len(moves)
        self.map.loadTime(start)

        for move in moves:
            self.map.moveBlock(move.mapp)
            self.map.loadMove()
        self.map.move = 1

        # notify that player have solve the problem
        print "AI player done playing!"
