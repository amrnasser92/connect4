Creating a game of connect 4
Class to initialize and set the board with dimensions for rows and columns
function to add a piece to the lowest empy spot of each column
fuction to print the board in 2D
fuction to check if the selected column is full / out of range

function to check if the game is won:
horizontal
vertical 
diagonal:
# if row < 3 and column <5 check + 1 col + 1 row up to (0,0) -> (2,3)
# if row < 3 and column >5 check -1 col + 1 row (2,3) -> (2,6)
# if row > 3 and column <5 check + 1 col - 1 row (3,0) -> (3,3)
# if row > 3 and column >5 check -1 col - 1 row (3,4) ->
