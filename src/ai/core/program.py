class Program():
    def __init__(self, problem, search=None):
        self.problem = problem
        self.search = search

    def __call__(self, percept):
        return self.search(percept, self.problem)
