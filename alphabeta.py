from copy import deepcopy
from math import inf
from random import randint

"""Alfa beta pruning algorithm for generating the machine moves"""

class Node:
    def __init__(self,table,who_moves_now)->None:
        self.table = table
        self.who_moves_now = who_moves_now
            
    def expand(self) -> list['Node']:
        childs:list[Node] = list()
        for col in range(7):
            table = self.make_move(col)
            if table is not None:
                child = Node(table,self.who_moves_now)
                childs.append(child)
        return childs
        
    def make_move(self,col) -> list[list[int]]|None: # None: Empty = 0 , User = -1, Machine = 1
        """Returns a table with the chosen move made"""
        rowi = None                        
        not_found = True
        table = deepcopy(self.table)
        for i,row in enumerate(table):
            if (row[col] != 0) and not_found:
                rowi = i-1
                not_found = False
        if not_found:
            rowi = 5
        if rowi == -1:
            table = None
        else:
            table[rowi][col] = self.who_moves_now 
        
        return table

    ## SABER SI UNA POSICIÓN ES TERMINAL

    def not_won(self,table:list[list[int]],who_moved:int) ->bool:
            won = False
            for i,row in enumerate(table):
                for j,num in enumerate(row):
                    # print(f"PIECE {(i,j)} \n---------------------")
                    if num == who_moved:
                        won = self.possible_win(table,i,j,who_moved)
                    if won:
                        return won
            return won

    def possible_win (self,table:list[list[int]],i:int,j:int,who:int)->bool:
        directions = [(1,-1),(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]

        for move in directions:
            # print(f"MOVE: {move}\n")
            connected = 1
            posy = i
            posx = j
            piece = table[posy][posx]

            while piece == who and connected < 4 and self.valid_move(posy,posx,move):
                posy +=  move[0]
                posx +=  move[1]
                piece = table[posy][posx]
                if piece == who:
                    connected += 1
                    # print(f"Pos: {(posy,posx)} Connected {connected}") 

            if connected == 4:
                return True
        return False

    def valid_move(self,posi:int,posj:int,move:tuple[int,int]) -> bool:
            valid = False
            if 0 <= posi + move[0] <= 5 and 0 <= posj + move[1]  <= 6:
                valid = True
            return valid

    # -------------

def alphabeta(node:Node,depth)->int:
    value = alphabeta_(node,depth,inf,-inf,True)
    
    #habria que buscar la columna a la que  se refiere el valor devuelto en los hijos del node 
    
    return value

def alphabeta_(node:Node,depth,alpha,beta,maxplayer)->int: #Devuelve la columna del movimiento
    
    if depth == 0 or node.not_won(node.table,-node.who_moves_now):
        return heuristic(node)
    
    if maxplayer:
        value = -inf
        for child in node.expand():
            value = max(value,alphabeta_(child,depth-1,alpha,beta,False))
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return value

    else: 
        value = inf
        for child in node.expand():
            value = min(value,alphabeta_(child,depth-1,alpha,beta,True))
            beta = min(beta,value)
            if alpha >= beta:
                break
        return value

def heuristic(node:Node)->None:
        # la intencion es crear un metodo de evaluacion que sume por cada ficha conectada tuya y reste por ficha conectada del rival
        # no si seria optimo tambien sumar por posibilidad de encadenar 4 o imposibilidad, ya que 2 fichas conectadas pero con imposibilidad de encadenar 4 no deberian sumar
        # ej
        # .  .   .   . La ficha "o" de la izquierda jamás podrá sumar 4, la ficha o de la derecha podría en diagonal, pero ya no contaría como ficha conectada
        # .  x   x   .
        # x  o   o   x
        #
        # posiblemente lo mejor sea sumar puntos por conectadas y por direcciones en las que "podría" conectar 4
        x = randint(1,10)
        return x



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
