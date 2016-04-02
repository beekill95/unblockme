# abstract class


class SearchAlgorithm:
    def __init__(self):
        self.problem = 0
        return

    def solve(self):
        raise NotImplementedError

    def setProblem(self, problem):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError
