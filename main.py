
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

    def playing(self,table:list[int]) -> None:
        pass

    def start_game(self)->None:
        while True: #(self.playing(self.table)):   # Self.playing has to evaluate if someplayer has won
            if self.who_moves == -1:
                self.user_moves()
            else:
                self.machine_moves()
            self.who_moves = 0 - self.who_moves # This line alternates between user (0) and machine (1)
            self.print_table()
        print("------------GAME ENDED------------")

    def invalid_col(self,col:int)->bool:
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
        while self.invalid_col(col):
            print("Invalid move")
            col = int(input("Introduce the column you want to place the chip: "))
        self.make_move(col)   

def main():
    juego = Connect4(-1)
    juego.start_game()

if __name__ == "__main__":
    main()