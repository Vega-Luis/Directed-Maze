"""
*This class is used to display player statistics.
"""
class Stat:
    def __init__(self, nickname, movements, suggestions, solution, time):
        self.nickname = nickname
        self.movements = movements 
        self.suggestions = suggestions
        self.solution = solution
        self.time = time
    
    def toString(self):
        tr = "\n\nNickName: " + self.nickname 
        tr += "\nMovements: " + str(self.movements)
        tr += "\nSuggestions: " + str(self.suggestions)
        tr += "\nSolution: " + self.solution
        tr += "\nTime: " + self.time
        return tr
