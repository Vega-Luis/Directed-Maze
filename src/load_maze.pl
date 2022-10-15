% taken from stack overflow
getLines(Path, Lines):-
  setup_call_cleanup(
    open(Path, read, In),
    readData(In, Lines),
    close(In)
  ).

readData(In, L):-
  read_term(In, H, []),
  (   H == end_of_file
  ->  L = []
  ;   L = [H|T],
      readData(In,T)
  ).

loadMaze(Path):-getLines(Path, Lines), asserta(maze(Lines)).