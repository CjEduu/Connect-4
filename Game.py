from copy import deepcopy
import random
import alphabeta
from typing import Final

DEPTH:Final = 2

class Game:
    # TABLE pieces :  Empty = 0 , User = 1, Machine = -1
    # WHO MOVES -1 = user , 1 = machine    
    
    def __init__(self,who_starts:int) -> None:
        self.who_moves = who_starts
        self.table = [[0 for _ in range (7)] for _ in range(6)]
        
    def print_table(self,table)->None:
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
          
    def start_game(self)->None:
        print("----------CONNECT4----------")
        self.print_table(self.table)
        
        while not self.is_terminal(self.table,-(self.who_moves)):   # Self.not_won has to evaluate if someplayer has won
            if self.who_moves == -1:
                self.user_moves()
            else:
                self.machine_moves()
            self.who_moves = 0 - self.who_moves # This line alternates between user (-1) and machine (1)
            self.print_table(self.table)
        print(f"------------GAME ENDED------------\n{"MACHINE WINS" if self.who_moves == -1 else "USER WINS"}")
        
    def invalid_col_input(self,col:int)->bool:
        ok = True
        if 0<= col < 7 and self.table[0][col] == 0:
            ok = False
        return ok

    def user_moves(self) -> None: 
        col = input(" USER MOVES : Introduce the column you want to place the chip: ")
        while not col.isdecimal() or self.invalid_col_input(int(col)):
            print("Invalid move")
            col = input("Introduce the column you want to place the chip: ")
        self.make_move_final(int(col))
        
    def machine_moves(self)->None:
        col = alphabeta.alpha_beta_search(self,self.table,DEPTH)
        print(col)
        self.make_move_final(col)
          
    def get_who_moves(self,table)->int:
        user = 0
        mach = 0
        for row in table:
            for col in row:
                if col == -1:
                    mach += 1
                if col == 1:
                    user += 1
        
        return -(user-mach)
    
    def is_terminal(self,table,who_moves)->bool:
        won = False
        for i,row in enumerate(table):
            for j,num in enumerate(row):
                # print(f"PIECE {(i,j)} \n---------------------")
                if num == who_moves:
                    won = self.connected_4(table,i,j,who_moves)
                if won:
                    return won
        return False
    
    def connected_4(self,table:list[int],i:int,j:int,who:int)->bool:
        directions = [(1,-1),(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for move in directions:
            connected = 1
            posy = i + move[0]
            posx = j + move[1] 
            while connected < 4 and self.valid_move(posy,posx):
                piece = table[posy][posx]
                if piece == who:
                    connected += 1
                    posy +=  move[0]
                    posx +=  move[1]
                else:
                    break   
            if connected == 4:
                return True
        return False
    
    def valid_move(self,posi:int,posj:int) -> bool:
        valid = False
        if 0 <= posi  <= 5 and 0 <= posj   <= 6:
            valid = True
        return valid
    
    def utility(self,table:list[list[int]],who_moves:int)-> int:
        # directions = [(1,-1),(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        # value = 0
        # for move in directions:
        #     rowi = i+move[0]
        #     coli = j+move[1]
        #     if self.valid_move(rowi,coli): # +1 si existe un hueco vacío alrededor de la ficha (+1 también si le quitas un hueco vacío alrededor a una ficha enemiga)
        #         if table[rowi][coli] in [0,-who_moves]:
        #             value +=1       
        return random.randint(0,10)
    
    def actions(self,table:list[list[int]],who_moves)->list[list[int]]:
        childs:list[list[list[int]]] = list()
        for col in range(7):
            table_m = self.make_move(col,table,who_moves)
            if table_m is not None:
                childs.append((col,table_m))
        return childs
    
    def make_move(self,col,table,who_moves) -> list[list[int]]|None: # None: Empty = 0 , User = -1, Machine = 1
        """Returns a table with the chosen move made"""
        rowi = None                        
        not_found = True
        table = deepcopy(table)
        for i,row in enumerate(table):
            if (row[col] != 0) and not_found:
                rowi = i-1
                not_found = False
                            
        if not_found:
            rowi = 5
        if rowi == -1:
            table = None
        else:
            table[rowi][col] = who_moves
        
        return table
    
    def make_move_final(self,col) -> None: # None: Empty = 0 , User = -1, Machine = 1
        rowi = 0
        not_found = True
        for i,row in enumerate(self.table):
            if (row[col] != 0) and not_found:
                rowi = i-1
                not_found = False
        if not_found:
            rowi = 5
        self.table[rowi][col] = self.who_moves
    
    
def main()->None:
    juego = Game(-1)
    juego.start_game()
    
    
if __name__ == "__main__":
    main()