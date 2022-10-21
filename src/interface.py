from pyswip import *

prolog = Prolog()
prolog.consult('game_rules.pl')

def LoadMaze():        
    loadMaze = Functor('loadMaze',1)
    call(loadMaze("C:/Users/admin/Documents/Tec/II Semestre 2022/Leguanjes de programacion/Proyectos/Proyecto 3/Programa/Directed-Maze/data/maze000.txt"))
    

def getMaze():        
    maze = Functor('maze',1)
    Matriz  = Variable()
    q = Query(maze(Matriz))
    while q.nextSolution():
        print(Matriz.value)
    q.closeQuery()

LoadMaze()
getMaze()