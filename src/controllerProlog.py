from random import gammavariate
from sys import flags
from pyswip import *
import constants as consts

class PrologController:
    """
     * Class constructor
     * Set up a maze game by requesting the path of the maze file
     * @param {String} Path: The path of the maze file
    """
    prolog = Prolog()
    prolog.consult(consts.GAME_RULES_PAHT)

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
        matrix = []
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

    """
     * This function reboot maze game 
    """
    def reboot(self):
        pass

    """
     * This function returns true or false if the current position is part of the path solution
     * @param {Integer} ActualRow: current position row 
     * @param {Integer} ActualColumn: current position column 
     * @returns {Boolean}: Return True or False 
    """
    def check(self,ActualRow, ActualColumn):
        verify = Functor('verify',2)
        q = Query(verify(ActualRow, ActualColumn))
        flag = False
        while q.nextSolution():
            flag = True
        q.closeQuery()
        return flag
    
    """
     * This function gives position suggestions to find a route solution
     * @param {Integer} ActualRow: current position row 
     * @param {Integer} ActualColumn: current position column 
     * @returns {Array}: Return array with position suggestions
    """
    def suggestion(self,ActualRow, ActualColumn):
        suggestion = Functor('suggestion',3)
        Suggestion  = Variable()
        q = Query(suggestion(ActualRow, ActualColumn,Suggestion))
        array = []
        while q.nextSolution():
            array += [Suggestion.value]
        q.closeQuery()
        return array

    """
     * This function returns the solution to the maze
     * @returns {Array}: Return array with solution path
    """
    def seeSolution(self):
        findSolution = Functor('findSolution',1)
        Maze  = Variable()
        q = Query(findSolution(Maze))
        matrix = []
        while q.nextSolution():
            matrix = Maze.value
        q.closeQuery()
        return matrix