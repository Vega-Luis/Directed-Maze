class Stat:
    def __init__(self, nickname, movements, suggestions, solution):
        self.nickname = nickname
        self.movements = movements 
        self.suggestions = suggestions
        self.solution = solution
    
    def toString(self):
        tr = "\n\nNickName: " + self.nickname 
        tr += "\nMovements: " + str(self.movements)
        tr += "\nSuggestions: " + str(self.suggestions)
        tr += "\nSolution: " + self.solution
        return tr