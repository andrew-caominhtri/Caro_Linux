import tkinter as tk
from tkinter import messagebox
import random

class CaroGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Caro Master")
        self.root.configure(bg="#1e1e2e") # Màu nền tối hiện đại (Cyberpunk style)
        
        # Cấu hình trò chơi
        self.size = 15
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "X"
        self.game_mode = "PvP"  # PvP hoặc PvE
        self.difficulty = "Medium" # Tùy chọn: Easy, Medium, Hard
        self.game_over = False
        
        # --- Giao diện điều khiển (Menu phía trên) ---
        self.menu_frame = tk.Frame(root, bg="#1e1e2e", pady=10)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X, padx=15)
        
        # Chọn chế độ chơi
        self.mode_label = tk.Label(self.menu_frame, text="Chế độ:", font=("Arial", 11, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        self.mode_label.pack(side=tk.LEFT, padx=5)
        
        self.btn_pvp = tk.Button(self.menu_frame, text="Người vs Người", font=("Arial", 10, "bold"), command=lambda: self.set_mode("PvP"), bg="#89b4fa", fg="#11111b", relief=tk.FLAT, bd=0, padx=10, pady=4)
        self.btn_pvp.pack(side=tk.LEFT, padx=5)
        
        self.btn_pve = tk.Button(self.menu_frame, text="Chơi với Máy", font=("Arial", 10, "bold"), command=lambda: self.set_mode("PvE"), bg="#45475a", fg="#cdd6f4", relief=tk.FLAT, bd=0, padx=10, pady=4)
        self.btn_pve.pack(side=tk.LEFT, padx=5)
        
        # Khung chọn độ khó (Chỉ hiện khi chơi với Máy)
        self.diff_frame = tk.Frame(self.menu_frame, bg="#1e1e2e")
        self.diff_frame.pack(side=tk.LEFT, padx=20)
        
        self.diff_label = tk.Label(self.diff_frame, text="Độ khó:", font=("Arial", 11, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        
        self.diff_var = tk.StringVar(value="Medium")
        self.menu_easy = tk.Radiobutton(self.diff_frame, text="Dễ", variable=self.diff_var, value="Easy", bg="#1e1e2e", fg="#a6e3a1", selectcolor="#1e1e2e", font=("Arial", 10), command=self.change_difficulty)
        self.menu_med = tk.Radiobutton(self.diff_frame, text="Vừa", variable=self.diff_var, value="Medium", bg="#1e1e2e", fg="#f9e2af", selectcolor="#1e1e2e", font=("Arial", 10), command=self.change_difficulty)
        self.menu_hard = tk.Radiobutton(self.diff_frame, text="Khó", variable=self.diff_var, value="Hard", bg="#1e1e2e", fg="#f38ba8", selectcolor="#1e1e2e", font=("Arial", 10), command=self.change_difficulty)
        
        # Nút Chơi lại
        self.btn_reset = tk.Button(self.menu_frame, text="Làm mới ↻", font=("Arial", 10, "bold"), command=self.reset_game, bg="#f5e0dc", fg="#11111b", relief=tk.FLAT, bd=0, padx=12, pady=4)
        self.btn_reset.pack(side=tk.RIGHT, padx=5)
        
        # --- Giao diện bàn cờ ---
        # Đã sửa pading thành padding ở dòng dưới
        self.board_frame = tk.Frame(root, bg="#313244", padx=2, pady=2)
        self.board_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.create_board()

    def create_board(self):
        for r in range(self.size):
            for c in range(self.size):
                btn = tk.Button(self.board_frame, text="", font=("Helvetica", 11, "bold"), width=3, height=1,
                                bg="#181825", fg="#cdd6f4", activebackground="#45475a", activeforeground="#cdd6f4",
                                relief=tk.SOLID, bd=1, command=lambda row=r, col=c: self.player_move(row, col))
                btn.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r][c] = btn

    def set_mode(self, mode):
        self.game_mode = mode
        if mode == "PvP":
            self.btn_pvp.config(bg="#89b4fa", fg="#11111b")
            self.btn_pve.config(bg="#45475a", fg="#cdd6f4")
            # Ẩn chọn độ khó nếu chơi 2 người
            self.diff_label.pack_forget()
            self.menu_easy.pack_forget()
            self.menu_med.pack_forget()
            self.menu_hard.pack_forget()
        else:
            self.btn_pve.config(bg="#89b4fa", fg="#11111b")
            self.btn_pvp.config(bg="#45475a", fg="#cdd6f4")
            # Hiện chọn độ khó khi chơi với máy
            self.diff_label.pack(side=tk.LEFT, padx=5)
            self.menu_easy.pack(side=tk.LEFT, padx=3)
            self.menu_med.pack(side=tk.LEFT, padx=3)
            self.menu_hard.pack(side=tk.LEFT, padx=3)
        self.reset_game()

    def change_difficulty(self):
        self.difficulty = self.diff_var.get()
        self.reset_game()

    def player_move(self, r, c):
        if self.board[r][c] != "" or self.game_over:
            return
        
        self.make_move(r, c, self.current_player)
        
        if self.check_win(r, c, self.current_player):
            messagebox.showinfo("Victory!", f"Người chơi {self.current_player} đã chiến thắng!")
            self.game_over = True
            return
        
        if self.game_mode == "PvP":
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            # Lượt của Máy
            self.root.update()
            self.game_over = self.bot_move()

    def make_move(self, r, c, player):
        self.board[r][c] = player
        color = "#89dceb" if player == "X" else "#f38ba8" # X xanh neon nhạt, O đỏ hồng
        self.buttons[r][c].config(text=player, state=tk.DISABLED, disabledforeground=color, bg="#313244")

    def count_line(self, r, c, dr, dc, player):
        """Đếm số quân liên tiếp từ (r,c) theo hướng (dr,dc) và kiểm tra xem có bị chặn đầu không"""
        count = 1
        open_ends = 0
        
        # Hướng thuận
        nr, nc = r + dr, c + dc
        while 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == player:
            count += 1
            nr += dr
            nc += dc
        if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == "":
            open_ends += 1
            
        # Hướng nghịch
        nr, nc = r - dr, c - dc
        while 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == player:
            count += 1
            nr -= dr
            nc -= dc
        if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == "":
            open_ends += 1
            
        return count, open_ends

    def evaluate_cell(self, r, c, player):
        """Đánh giá điểm nguy hiểm/cơ hội của một ô trống đối với một người chơi cụ thể"""
        max_score = 0
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count, open_ends = self.count_line(r, c, dr, dc, player)
            if count >= 5: return 100000
            if count == 4:
                if open_ends == 2: return 10000  # Thế 4 trống 2 đầu thoáng
                if open_ends == 1: return 2000   # Thế 4 bị chặn 1 đầu
            if count == 3:
                if open_ends == 2: return 3000   # Thế 3 thoáng nguy hiểm
                if open_ends == 1: return 500
            if count == 2:
                if open_ends == 2: return 200
                if open_ends == 1: return 50
        return 0

    def bot_move(self):
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == ""]
        if not empty_cells:
            return False

        # --- CHẾ ĐỘ DỄ (EASY) ---
        if self.difficulty == "Easy":
            if random.random() > 0.2:
                best_moves = self.get_neighbor_cells()
                move = random.choice(best_moves) if best_moves else random.choice(empty_cells)
                self.make_move(move[0], move[1], "O")
                return self.check_win(move[0], move[1], "O")

        # --- CHẾ ĐỘ VỪA & KHÓ (MEDIUM & HARD) ---
        best_score = -1
        best_move = empty_cells[0]

        for r, c in empty_cells:
            attack_score = self.evaluate_cell(r, c, "O")
            defend_score = self.evaluate_cell(r, c, "X")
            
            if self.difficulty == "Hard":
                score = attack_score + (defend_score * 1.3)
            else: # Medium
                score = attack_score + defend_score

            if score > best_score:
                best_score = score
                best_move = (r, c)

        self.make_move(best_move[0], best_move[1], "O")
        
        if self.check_win(best_move[0], best_move[1], "O"):
            messagebox.showinfo("Defeat!", "Máy đã chiến thắng! Hãy thử lại nhé.")
            return True
        return False

    def get_neighbor_cells(self):
        neighbors = []
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] != "":
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == "":
                                if (nr, nc) not in neighbors:
                                    neighbors.append((nr, nc))
        return neighbors

    def check_win(self, r, c, player):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            nr, nc = r + dr, c + dc
            while 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == player:
                count += 1
                nr += dr
                nc += dc
            nr, nc = r - dr, c - dc
            while 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == player:
                count += 1
                nr -= dr
                nc -= dc
            if count >= 5:
                return True
        return False

    def reset_game(self):
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "X"
        self.game_over = False
        for r in range(self.size):
            for c in range(self.size):
                self.buttons[r][c].config(text="", state=tk.NORMAL, bg="#181825")

if __name__ == "__main__":
    root = tk.Tk()
    game = CaroGame(root)
    root.mainloop()
