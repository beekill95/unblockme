from SearchAlgorithm import SearchAlgorithm
from StateCounter import StateCounter


class BreadthFirstSearch(SearchAlgorithm):
    def __init__(self):
        self.solver = 0

    def setProblem(self, problem):
        self.solver = NewBFSSolver(problem)

    def solve(self):
        return self.solver.solve()

    def description(self):
        print "\nBreadth-First Search Algorithm"


class NewBFSSolver:
    def __init__(self, problem):
        self.problem = problem
        self.visited = set()
        self.stateQueue = []

    def getSolution(self, state):
        states = []
        s = state
        while not(s.parent is None):
            states.append(s)
            s = s.parent

        states.reverse()
        return states

    def solve(self):
        stateCounter = StateCounter()
        self.stateQueue.append(self.problem.startState)
        found = False

        while self.stateQueue:
            state = self.stateQueue.pop(0)

            # prevent some states which were visited
            if state in self.visited:
                continue

            # if current state is goal state
            if self.problem.isGoalState(state):
                found = state
                break

            # otherwise
            stateCounter.record(self.stateQueue)
            self.visited.add(state)
            states = self.problem.generateNextStates(state)
            for s in states:
                if not (s in self.visited):
                    s.setParent(state)
                    self.stateQueue.append(s) # we don't check whether next state is already in visited

        solution = []
        print stateCounter.report()
        if found:
            # we found a solution
            solution = self.getSolution(state)
            print "States visited: %d" %len(self.visited)
            print "Solution found"
        else:
            print "Solution not found"

        return solution