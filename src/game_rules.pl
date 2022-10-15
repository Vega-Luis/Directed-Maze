%%
%
% The edge/5 predicate works as an graph edge.
% When called with OriginRow and OriginColumn returns in DestineRow adn DestineColumn
% all valid moves.
% When called with all arguments determinate if the conection between origin and destine vertex
% exist.
%
% @param OriginRow Row index of the origin vertex.
% @param OriginColumn Column index of the origin vertex.
% @param DestineRow Row index of the destine vertex.
% @param DestineColumn Column index of the destine vertex.

% Posible moves on intersection vertex
edge(OriginRow, OriginColumn, DestineRow, OriginColumn, inter):-
    DestineRow is OriginRow - 1,
    not(isWall(DestineRow, OriginColumn));
    DestineRow is OriginRow + 1,
    not(isWall(DestineRow, OriginColumn)).
edge(OriginRow, OriginColumn, OriginRow, DestineColumn, inter):-
    DestineColumn is OriginColumn - 1,
    not(isWall(OriginRow, DestineColumn));
    DestineColumn is OriginColumn + 1,
    not(isWall(OriginRow, DestineColumn)),!.

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

% Checks if there is track between origin and destination x = wall
isWall(Row, Column):-getVertexValue(Row,Column,Value), Value = x.

% Calcualte the maze start row.
getStart([[Point|_]|_], 0):- Point = i.
getStart([[_|_]|Tail], Row):-
    getStart(Tail, RowDown),
    Row is RowDown + 1.

% Returns the maze start point.
startPoint(Row, 0):-
    maze(M), getStart(M, Row),!.

% Obtains the value of the (i,j) position in the game matrix.
getVertexValue(RowIndex, ColumnIndex, Value):-
    maze(M), nth0(RowIndex, M, Row), nth0(ColumnIndex, Row, Value).