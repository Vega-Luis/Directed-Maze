from pyswip import *

class controllerProlog:
    """
     * Class constructor
     * Set up a maze game by requesting the path of the maze file
     * @param {String} Path: The path of the maze file
    """
    prolog = Prolog()
    prolog.consult('game_rules.pl')

    def __init__(self,Path):
        self.maze=[]
        self.load_Maze(Path)

    """
     * This function calls prolog to read the file path and load the maze.
     * @param {String} Path: The path of the maze file
    """
    def load_Maze(self,Path):        
        loadMaze = Functor('loadMaze',1)
        call(loadMaze(Path))
        
    """
     * This function get maze.
    """
    def getMaze(self):
        maze = Functor('maze',1)
        Matriz  = Variable()
        q = Query(maze(Matriz))
        while q.nextSolution():
            matrix = Matriz.value
        q.closeQuery()
        self.getMazeAux(matrix)

    """
     * This function converts the prolog array to a readable array
     * @param {Array} matrix: Prolog array.
    """
    def getMazeAux(self,matrix): 
        maze =[]
        for rows in matrix:
            array =[]
            for element in rows:
                array+=[element.value]
            maze+=[array]
        self.maze = maze

    def reboot(self):
        pass

    def check(self):
        pass
    
    def suggestion(self):
        pass

    def seeSolution(self):
        pass
    
c = controllerProlog('C:/Users/admin/Documents/Tec/II Semestre 2022/Leguanjes de programacion/Proyectos/Proyecto 3/Programa/Directed-Maze/data/maze000.txt')
c.getMaze()
print(c.maze)