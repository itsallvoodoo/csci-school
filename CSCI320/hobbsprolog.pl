% -----------------------------------------------------
% Program Name:		hwprolog.pl
% Lesson: 			Prolog Programming Exercises
% Author: 			Chad Hobbs
% Collaborators: 	Nobody
% Sources: 			Notes
% Due: 				11:59, Friday, November 22nd, 2013
% -----------------------------------------------------

% -------- EXERCISE 1 --------
% ---- ADD FUNCTION ----
% This very simple function adds an argument to a list including the second argument


add(X,Y,[X|Y]).

% -------- EXERCISE 2 --------
% These two functions return whether or not a given list is even or odd in length

% ---- EVEN LENGTH ----

evenlength([ X,Y | Z ]) :- evenlength(Z).
evenlength([]).

% ---- ODD LENGTH ----
oddlength([ X,Y | Z ]) :- oddlength(Z).
oddlength([X]).


% -------- EXERCISE 3 --------
% This function is a written exercise

member1(X, L) :- concat(L1, [X | L2], L).

member(X, [X|T]).
member(X, [H|T]) :- member(X,T).


% Done on paper that is to be turned in on Monday, the 25th.

% -------- EXERCISE 4 --------
% This function returns the last element in a list, or matches the pattern of last element if given

last1(L, X) :- concat(_, [X], L).

% -------- EXERCISE 5 --------
% This function returns true if a given list is a sublist of the second given list.

% This one works sometimes, and other times it blows the stack. I don't know why
sublist(S,L) :- concat(_,S,P), concat(P,_,L).

% This version works for only singular items in the list. It was my first version and I kept working to get the above version.
sublist2([S],L) :- concat(_,[S|_], L).

% ---- CONCAT FUNCTION ----
% This is a helper function to be used with exercises 4 and 5

concat([], L, L).
concat([H|T], L, [H|M]) :- concat(T, L, M).