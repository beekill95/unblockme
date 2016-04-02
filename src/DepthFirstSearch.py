from SearchAlgorithm import SearchAlgorithm
from StateCounter import StateCounter


class DepthFirstSearch(SearchAlgorithm):
    def __init__(self):
        self.solver = None

    def setProblem(self, problem):
        self.solver = NewDFSSolver(problem)

    def solve(self):
        return self.solver.solve()

    def description(self):
        print "\nDepth-First Search Algorithm"


class NewDFSSolver:
    def __init__(self, problem):
        self.problem = problem
        self.visited = set()
        self.stateStack = []

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
        self.stateStack.append(self.problem.startState)
        found = False

        while len(self.stateStack) != 0:
            state = self.stateStack.pop()

            # prevent some states which were visited
            if state in self.visited:
                continue

            # if current state is goal state
            if self.problem.isGoalState(state):
                found = state
                break

            # otherwise
            stateCounter.record(self.stateStack)
            self.visited.add(state)
            states = self.problem.generateNextStates(state)
            for s in states:
                if not(s in self.visited):
                    s.setParent(state)
                    self.stateStack.append(s) # we don't check whether next state is already in visited

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