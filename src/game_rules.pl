%%
%
% The edge/5 predicate works as an graph edge.
% When called with OriginRow and OriginColumn returns in DestineRow and DestineColumn
% all valid moves.
% When called with all arguments determinate if the conection between origin and destine vertex
% exist.
%
% @param OriginRow Row index of the origin vertex.
% @param OriginColumn Column index of the origin vertex.
% @param DestineRow Row index of the destine vertex.
% @param DestineColumn Column index of the destine vertex.

% Posible moves on left-direction vertex.
edge(OriginRow, OriginColumn, OriginRow, DestineColumn, at):-
    DestineColumn is OriginColumn - 1,
    not(isWall(OriginRow, DestineColumn)),!.

% Posilbe moves on right-direction vertex.
edge(OriginRow, OriginColumn, OriginRow, DestineColumn, ad):-
    DestineColumn is OriginColumn + 1,
    not(isWall(OriginRow, DestineColumn)),!.

% Posible moves on up-direction vertex.
edge(OriginRow, OriginColumn, DestineRow, OriginColumn, ar):-
    DestineRow is OriginRow - 1,
    not(isWall(DestineRow, OriginColumn)),!.

%posible moves on down-direction vertex.
edge(OriginRow, OriginColumn, DestineRow, OriginColumn, ab):-
    DestineRow is OriginRow + 1,
    not(isWall(DestineRow, OriginColumn)),!.

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, i):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, ar).

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, i):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, ab).

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, i):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, ad).

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, inter):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, at).

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, inter):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, ad).

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, inter):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, ar).

edge(OriginRow, OriginColumn, DestineRow, DestineColumn, inter):-
    edge(OriginRow, OriginColumn, DestineRow,DestineColumn, ab).

% Checks if there is track between origin and destination x = wall
isWall(Row, Column):-getVertexValue(Row,Column,Value), Value = x.


% Finds the maze origin coordinate.
originPoint([[Point|_]|_], 0, 0):- Point = i.
originPoint([_|Tail], Row, Column):-
    originPoint(Tail, RowDown, Column),
    Row is RowDown + 1.

% Finds the maze desitne coordinate.
destinePoint([Row|_], 0, Column):-
    length(Row, Length),
    nth1(Length, Row, Element),
    Element = f,
    Column is Length - 1,!.
destinePoint([_|Tail], Row, Column):-
    destinePoint(Tail, RowDown, Column),
    Row is RowDown + 1.


% Obtains the value of the (i,j) position in the game matrix.
getVertexValue(RowIndex, ColumnIndex, Value):-
    maze(M), nth0(RowIndex, M, Row), nth0(ColumnIndex, Row, Value),!.

% Checks if a exist a path between two vertex, return the path if it exists.
findPath(Row, Column, Row, Column,_,[]):-!.

findPath(Row, Column, DestineRow, DestineColumn, Visited,[[CanditateRow,CandidateColumn]|Tail]):-
    getVertexValue(Row, Column, Value),
    edge(Row, Column, CanditateRow, CandidateColumn, Value),
    notVisited([CanditateRow, CandidateColumn], Visited),
    findPath(CanditateRow, CandidateColumn, DestineRow, DestineColumn, [[CanditateRow,CandidateColumn]|Visited],Tail).
% Check if a vertex have not been visited yet.
notVisited(Target, List):-
    not(visited(Target, List)).

% Checks if a vertex were visited.
visited(Value, [Value|_]):-!.
visited(Value, [_|Tail]):-
    visited(Value, Tail).

% Finds and returns a list with the coordinates of the solution path.
findSolution([[OriginRow, OriginColumn]| Path]):-
    maze(Maze),
    originPoint(Maze, OriginRow, OriginColumn),
    destinePoint(Maze, DestineRow, DestineColumn),
    findPath(OriginRow, OriginColumn, DestineRow, DestineColumn, [], Path).

suggestion(ActualRow, ActualColumn, Suggestion):-
    maze(Maze),
    destinePoint(Maze, DestineRow, DestineColumn),
    findPath(ActualRow, ActualColumn, DestineRow, DestineColumn, [], [Suggestion|_]).

verify(ActualRow, ActualColumn):-
    maze(Maze),
    destinePoint(Maze, DestineRow, DestineColumn),
    findPath(ActualRow, ActualColumn, DestineRow, DestineColumn, [], _),!.