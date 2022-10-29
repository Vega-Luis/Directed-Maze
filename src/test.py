from pyswip import *

prolog = Prolog()
prolog.consult('game_rules.pl')

def LoadMaze():        
    assertz = Functor('assertz', 1)
    maze = Functor('maze',1)
    call(assertz(maze("[[x,x,x,x,x,x,x,x,x,x,x],[x,ar,x,x,ad,ad,ad,inter,ad,inter,x],[i,inter,ad,ad,inter,x,x,ab,x,ab,x],[x,ab,x,x,x,inter,at,inter,x,ab,x],[x,ab,x,x,x,ab,x,ab,x,x,x],[x,ab,x,x,inter,inter,x,ab,x,inter,f],[x,ab,x,x,ab,x,x,inter,inter,inter,x],[x,ab,x,x,ab,x,x,x,ar,x,x],[x,ab,x,at,inter,inter,ad,ad,inter,at,x],[x,ab,x,ar,x,ab,x,x,ab,ar,x],[x,inter,ad,inter,x,inter,ad,x,ab,inter,x],[x,x,x,x,x,x,x,x,x,x,x]]")))

def getMaze():        
    maze = Functor('maze',1)
    Matriz  = Variable()
    q = Query(maze(Matriz))
    while q.nextSolution():
        print(Matriz.value)
    q.closeQuery()


LoadMaze()
getMaze()
