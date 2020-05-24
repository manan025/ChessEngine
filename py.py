import interactive as it
# import chess.interactive as it

"""
Memory Chess engine
Made by Manan

Description: This app can be used to play special kind of chess, where when you kill one of the pieces of opponent,
You can see the position of all the pieces or else you will have to use your memory or
the chess play history [notation that you used to play the game till then] to see the game progress/ tokens location.
"""
# 8 x 8

p1_pawn_constant = 2    # (x, y) -> x for all pawns for player 1
p1_main_constant = 1    # (x, y) -> x for all the major tokens for player 1
p2_pawn_constant = 7    # (x, y) -> x for all pawns for player 2
p2_main_constant = 8    # (x, y) -> x for all the major tokens for player 2
p1 = {"rook1": [p1_main_constant, 1], "knight1": [p1_main_constant, 2], "bishop1": [p1_main_constant, 3],
      "king": [p1_main_constant, 4], "queen": [p1_main_constant, 5],
      "bishop2": [p1_main_constant, 6], "knight2": [p1_main_constant, 7], "rook2": [p1_main_constant, 8],
      "pawn1": [p1_pawn_constant, 1], "pawn2": [p1_pawn_constant, 2], "pawn3": [p1_pawn_constant, 3],
      "pawn4": [p1_pawn_constant, 4], "pawn5": [p1_pawn_constant, 5], "pawn6": [p1_pawn_constant, 6],
      "pawn7": [p1_pawn_constant, 7], "pawn8": [p1_pawn_constant, 8]}

p2 = {"rook1": [p2_main_constant, 1], "knight1": [p2_main_constant, 2], "bishop1": [p2_main_constant, 3],
      "king": [p2_main_constant, 4], "queen": [p2_main_constant, 5],
      "bishop2": [p2_main_constant, 6], "knight2": [p2_main_constant, 7], "rook2": [p2_main_constant, 8],
      "pawn1": [p2_pawn_constant, 1], "pawn2": [p2_pawn_constant, 2], "pawn3": [p2_pawn_constant, 3],
      "pawn4": [p2_pawn_constant, 4], "pawn5": [p2_pawn_constant, 5], "pawn6": [p2_pawn_constant, 6],
      "pawn7": [p2_pawn_constant, 7], "pawn8": [p2_pawn_constant, 8]}

player1_name = input("Enter Player 1 name: ").strip()
player2_name = input("Enter Player 2 name: ").strip()
result = None or player1_name or player2_name
end = False
it.info(player1_name, player2_name)

while not end:
    exit(ValueError)

# player1 = {"rook1": 1, "knight1": 2, "bishop1": 3, "king": 4, "queen": 5, "bishop2": 6, "knight2": 7, "rook2": 8}
# player2 = {"rook1": 1, "knight1": 2, "bishop1": 3, "king": 4, "queen": 5, "bishop2": 6, "knight2": 7, "rook2": 8}
