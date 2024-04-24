from typing import Optional

class Connect4:
    table:list[int] # TABLE pieces :  Empty = 0 , User = 1, Machine = 2
    who_moves:int # WHO MOVES -1 = user , 1 = machine    

    def __init__(self,who_starts:int) -> None:
        self.who_moves = who_starts
        self.table = [[0 for _ in range (7)] for _ in range(6)]
    
    def get_who_moves(self)->int:
        return self.who_moves
    
    def print_table(self)->None:
        print([x for x in range(7)])
        for row in self.table:
            print(row)

    def not_won(self,table:list[int]) ->bool:
        won = False
        for i,row in enumerate(table):
            for j,num in enumerate(row):
                print(f"PIECE {(i,j)} \n")
                if num == -1:
                    won = self.evaluate(table,i,j,-1)
                if num == 1:
                    won = self.evaluate(table,i,j,1)
                if won:
                    return won
        return won
    
    def evaluate(self,table:list[int],i:int,j:int,who:int)->bool:
        directions = [(1,-1),(1,0),(1,1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        
        for move in directions:
            print(f"MOVE: {move}\n")
            connected = 0
            posy = i
            posx = j
            piece = table[posy][posx]
            
            while piece == who and connected < 4 and self.valid_move(posy,posx):
                connected += 1 
                piece = table[posy][posx]
                print(f"Piece: {piece} Pos: {(posy,posx)} Connected {connected}")
                posy +=  move[0]
                posx +=  move[1]
                
            if connected == 4:
                return True
        return False
    
    def valid_move(self,posi:int,posj:int) -> bool:
        valid = False
        if 0 <= posi <= 5 and 0 <= posj  <= 6:
            valid = True
        return valid
    
    def start_game(self)->None:
        while self.not_won(self.table):   # Self.not_won has to evaluate if someplayer has won
            if self.who_moves == -1:
                self.user_moves()
            else:
                self.machine_moves()
            self.who_moves = 0 - self.who_moves # This line alternates between user (-1) and machine (1)
            self.print_table()
        print("------------GAME ENDED------------")

    def invalid_col_input(self,col:int)->bool:
        ok = True
        if 0<= col < 7 and self.table[0][col] == 0:
            ok = False
        return ok
    
    def make_move(self,col) -> None: # None: Empty = 0 , User = -1, Machine = 1
        rowi = 0
        not_found = True
        for i,row in enumerate(self.table):
            if (row[col] != 0) and not_found:
                rowi = i-1
                not_found = False
        if not_found:
            rowi = 5
        self.table[rowi][col] = self.who_moves

    def user_moves(self) -> None:
        col = int(input("Introduce the column you want to place the chip: "))
        while self.invalid_col_input(col):
            print("Invalid move")
            col = int(input("Introduce the column you want to place the chip: "))
        self.make_move(col)   
        
    def machine_moves(self)->None:
        pass

def main():
    table = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,-1,0,0],[0,0,0,-1,-1,1,0],[0,0,1,-1,1,1,-1],[0,1,-1,1,1,-1,-1]]
    juego = Connect4(-1)
    # juego.start_game()
    
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
        
    print(juego.not_won(table))
    
if __name__ == "__main__":
    main()