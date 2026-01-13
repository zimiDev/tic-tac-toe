class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current = "X"

    def display(self):
        print("\n")
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < 2:
                print("-" * 9)
        print("\n")

    def switch_player(self):
        self.current = "O" if self.current == "X" else "X"

    def is_valid_move(self, r, c):
        return 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == " "

    def make_move(self, r, c):
        self.board[r][c] = self.current

    def is_winner(self, p):
        rows = any(all(cell == p for cell in row) for row in self.board)
        cols = any(all(self.board[r][c] == p for r in range(3)) for c in range(3))
        diag1 = all(self.board[i][i] == p for i in range(3))
        diag2 = all(self.board[i][2 - i] == p for i in range(3))
        return rows or cols or diag1 or diag2

    def is_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.display()
            print(f"Player {self.current}'s turn.")

            try:
                r = int(input("Enter row (0-2): "))
                c = int(input("Enter column (0-2): "))
            except ValueError:
                print("❗ Invalid input! Please enter numbers only.")
                continue

            if not self.is_valid_move(r, c):
                print("❗ Invalid or occupied position! Try again.")
                continue

            self.make_move(r, c)

            if self.is_winner(self.current):
                self.display()
                print(f"🎉 Player {self.current} wins!")
                break

            if self.is_draw():
                self.display()
                print("🤝 It's a draw!")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()
