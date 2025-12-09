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
        while True:
            self.display()
            print(f"{self.current} navbati.")

            try:
                r = int(input("Qator (0-2): "))
                c = int(input("Ustun (0-2): "))
            except ValueError:
                print("❗ Faqat raqam kiriting!")
                continue

            if not self.is_valid_move(r, c):
                print("❗ Noto‘g‘ri yoki band joy! Qayta urinib ko‘ring.")
                continue

            self.make_move(r, c)

            if self.is_winner(self.current):
                self.display()
                print(f"🎉 {self.current} g‘olib bo‘ldi!")
                break

            if self.is_draw():
                self.display()
                print("🤝 Durang!")
                break

            self.switch_player()


game = TicTacToe()
game.play()
