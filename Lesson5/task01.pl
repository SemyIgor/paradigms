% Rules
sum([], 0).
sum([H|T], Sum) :-
    sum(T,Sum1), Sum is Sum1 + H.

% Query
% sum([1,2,3,4,5,6,7,8,9,10], Sum).  #55