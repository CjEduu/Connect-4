
"""Alfa beta pruning algorithm for generating the machine moves"""

# ----------------------------------------
def alpha_beta_search(game,table,depth):
    who_moves = game.get_who_moves(table)
    alpha = float("-inf")
    beta = float("inf")
    _, col = max_valueAB(game, table, alpha, beta,depth,who_moves)
    return col

def max_valueAB(game, table, alpha, beta,depth,who_moves):
    game.print_table(table)
    if depth == 0: #game.is_terminal(table,game.get_who_moves(table)) or 
        n = game.utility(table, game.get_who_moves(table))
        print(f"UTILITY = {n} DEPTH = {depth} WHO MOVES = {who_moves}\nALPHA = {alpha} BETA = {beta}")
        print("---------------------------------------")
        return n, None
    v = float("-inf")
    for col,table in game.actions(table,who_moves):
        v2, _ = min_valueAB(game, table , alpha, beta,depth-1,-who_moves)
        if v2 > v:
            v = v2
            move = col
        if v >= beta:
            return v, move
        alpha = max(alpha, v)
    return v, move

def min_valueAB(game, table, alpha, beta,depth,who_moves):
    game.print_table(table)
    if depth == 0: #game.is_terminal(table,game.get_who_moves(table)) or 
        n = game.utility(table, game.get_who_moves(table))
        print(f"UTILITY = {n} DEPTH = {depth} WHO MOVES = {who_moves}\n ALPHA = {alpha} BETA = {beta}")
        print("---------------------------------------")
        return n, None
    v = float("inf")
    for col,table in game.actions(table,who_moves):
        v2, _ = max_valueAB(game, table, alpha, beta,depth-1,-who_moves)
        if v2 < v:
            v = v2
            move = col
        if v <= alpha:
            return v, move
        beta = min(beta, v)
    return v, move


def print_table(table)->None:
        print([x for x in range(7)])
        for row in table:
            for value in row:
                if value == -1:
                    char = "X"
                if value == 1:
                    char = "O"
                if value == 0:
                    char = "■"
                print(f"{char:>3}",end="")
            print("\n")
