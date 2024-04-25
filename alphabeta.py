from copy import deepcopy

"""Alfa beta pruning algorithm for generating the machine moves"""

class Node:
    def __init__(self,parent,table,who_moves_now) -> None:
        self.who_moves_now = who_moves_now
        self.parent = parent
        self.table  = table
        self.move = None
        self.value = None
    
    def expand(self) -> list['Node']:
        childs:list[Node] = list()
        for col in range(7):
            table = self.make_move(col)
            if table is not None:
                child = Node(self,table,-self.who_moves_now)
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



def alpha_beta_pruning()->int: #Devuelve la columna del movimiento
    pass




def evaluate_node(Node:Node)->None:
    # la intencion es crear un metodo de evaluacion que sume por cada ficha conectada tuya y reste por ficha conectada del rival
    # no si seria optimo tambien sumar por posibilidad de encadenar 4 o imposibilidad, ya que 2 fichas conectadas pero con imposibilidad de encadenar 4 no deberian sumar
    # ej
    # .  .   .   . La ficha "o" de la izquierda jamás podrá sumar 4, la ficha o de la derecha podría en diagonal, pero ya no contaría como ficha conectada
    # .  x   x   .
    # x  o   o   x
    #
    # posiblemente lo mejor sea sumar puntos por conectadas y por direcciones en las que "podría" conectar 4
    pass




def main():
    table = [[0 , 0 , 0 , 0, 0, 0 , -1 ],
             [0 , 0 , 0 , 0, 0, 0 , 1 ],
             [0 , 0 , 0 , 0,-1,-1 ,-1 ],
             [0 , 0 , 0 ,-1,-1, 1 , 1 ],
             [0 , 0 , 1 ,-1, 1, 1 ,-1 ],
             [0 , 1 ,-1 , 1, 1,-1 ,-1 ]]
    
    nodo = Node(None,table,1)
    print("INITIAL TABLE")
    print_table(table)
    print("------------------")
    
    
    childs = nodo.expand()
    for i,child in enumerate(childs):
        print(f"TABLE {i}-------------")
        print_table(child.table)
        for j,child2 in enumerate(child.expand()):
            print(f"TABLE {j} FATHER {i}-------------")
            print_table(child2.table)
            
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




## SABER SI UNA POSICIÓN ES TERMINAL

def not_won(table:list[list[int]],who_moved:int) ->bool:
        won = False
        for i,row in enumerate(table):
            for j,num in enumerate(row):
                # print(f"PIECE {(i,j)} \n---------------------")
                if num == who_moved:
                    won = possible_win(table,i,j,who_moved)
                if won:
                    return won
        return won
    
def possible_win (table:list[list[int]],i:int,j:int,who:int)->bool:
    directions = [(1,-1),(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    
    for move in directions:
        # print(f"MOVE: {move}\n")
        connected = 1
        posy = i
        posx = j
        piece = table[posy][posx]
        
        while piece == who and connected < 4 and valid_move(posy,posx,move):
            posy +=  move[0]
            posx +=  move[1]
            piece = table[posy][posx]
            if piece == who:
                connected += 1
                # print(f"Pos: {(posy,posx)} Connected {connected}") 
            
        if connected == 4:
            return True
    return False

def valid_move(posi:int,posj:int,move:tuple[int,int]) -> bool:
        valid = False
        if 0 <= posi + move[0] <= 5 and 0 <= posj + move[1]  <= 6:
            valid = True
        return valid

# -------------


if __name__ == "__main__":
    main()