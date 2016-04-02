from SearchAlgorithm import SearchAlgorithm
from StateCounter import StateCounter


class BestFirstSearch(SearchAlgorithm):
    def __init__(self):
        self.solver = 0

    def setProblem(self, problem):
        self.solver = SolverBestFirstSearch(problem, HeuristicFunction())

    def solve(self):
        return self.solver.solve()

    def description(self):
        print "\nBest-First Search"


class SolverBestFirstSearch:
    def __init__(self, problem, heuristicFunction):
        self.problem = problem
        self.minHeap = MinHeap()
        self.visited = set()
        self.heuristicFunction = heuristicFunction

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
        self.minHeap.insert((0, self.problem.startState)) # the first state's score doesn't matter
        found = False

        while not self.minHeap.isEmpty():
            value = self.minHeap.remove()

            if value[1] in self.visited:
                continue

            # check for goal state
            if self.problem.isGoalState(value[1]):
                found = value[1]
                break

            stateCounter.record(self.minHeap.priQueue)

            self.visited.add(value[1])
            states = self.problem.generateNextStates(value[1])
            for s in states:
                if not (s in self.visited):
                    s.setParent(value[1])

                    score = self.heuristicFunction.evaluate(s)
                    self.minHeap.insert((score,s))

        solution = []
        print stateCounter.report()
        if found:
            solution = self.getSolution(found)
            print "States visited: %d" %len(self.visited)
            print "Solution found"
        else:
            print "Solution not found"
        return solution


class HeuristicFunction:
    def __init__(self):
        return

    def evaluate(self, state):
        return self.__g(state) + self.__h(state)

    def __g(self, state):
        return state.height

    def __h(self, state):
        map = state.mapp
        row = 2  # the row in which the red block is in
        for col in range(0,6):
            # search which column is the red block in
            if map[row][col] == '8':
                break

        obstacleCnt = 0  # number of blocks which are blocking the red block
        for i in range(col + 2, 6):
            if map[row][i] != '0':
                obstacleCnt += 1
        return obstacleCnt * 10  # give the obstacleCnt move important


class MinHeap:
    def __init__(self):
        self.priQueue = []

    def insert(self, (score, state)):
        self.priQueue.append((score, state))

        self.__upHeap(len(self.priQueue) - 1)

    def remove(self):
        if len(self.priQueue) == 0:
            raise Exception("Remove empty queue")
        else:
            value = self.priQueue[0]
            self.priQueue[0] = self.priQueue[len(self.priQueue) - 1]
            self.priQueue.pop() # pop the last element out

            self.__downHeap(0)
            return value

    def isEmpty(self):
        return len(self.priQueue) == 0

    def __upHeap(self, position):
        if position != 0:
            parent = (position - 1) // 2

            if self.priQueue[parent][0] > self.priQueue[position][0]:
                self.__swap(parent, position)
                self.__upHeap(parent)

    def __downHeap(self, position):
        leftChild = 2 * position + 1
        rightChild = 2 * position + 2

        if leftChild < len(self.priQueue) and rightChild < len(self.priQueue):
            smallerChild = leftChild if self.priQueue[leftChild][0] < self.priQueue[rightChild][0] else rightChild
            if self.priQueue[position][0] > self.priQueue[smallerChild][0]:
                self.__swap(position, smallerChild)
                self.__downHeap(smallerChild)
        elif leftChild < len(self.priQueue):
            if self.priQueue[position][0] > self.priQueue[leftChild][0]:
                self.__swap(position, leftChild)

    def __swap(self, i, j):
        self.priQueue[i], self.priQueue[j] = self.priQueue[j], self.priQueue[i]