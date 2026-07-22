# 🎮 Trò Chơi Cờ Caro (Gomoku)

## 🌟 Tính Năng Nổi Bật

- **Bàn cờ chuẩn $15 \times 15$:** Giao diện tông màu tối (Cyberpunk style) bắt mắt, thao tác mượt mà.
- **Chế độ chơi đa dạng:**
  - 👥 **Người vs Người (PvP):** Thách đấu cùng bạn bè trên cùng một máy tính.
  - 🤖 **Chơi với Máy (PvE):** Rèn luyện tư duy với thuật toán AI.
- **AI 3 Cấp Độ (Rule-based AI):**
  - 🟢 **Dễ (Easy):** Máy đánh ngẫu nhiên lân cận, phù hợp cho người mới bắt đầu.
  - 🟡 **Vừa (Medium):** Áp dụng thuật toán Heuristic tấn công và phòng thủ cơ bản.
  - 🔴 **Khó (Hard):** Máy tính toán trọng số nước đi gắt gao, nhạy bén phát hiện và ngăn chặn các thế cờ nguy hiểm (thế 3 trống 2 đầu, thế 4 thoáng).
- **Tính di động cao:** Đã được đóng gói bằng **PyInstaller** thành file thực thi nhị phân độc lập cho hệ điều hành Linux (không cần cài đặt môi trường Python).

---

## 🚀 Hướng Dẫn Chạy Nhanh (Không Cần Cài Đặt Python)

Dành cho người dùng muốn tải về và chơi ngay lập tức:

1. Truy cập mục **[Releases](../../releases)** trên GitHub Repository này.
2. Tải về tập tin thực thi nhị phân `caro_game`.
3. Mở Terminal tại thư mục chứa file vừa tải và chạy lệnh cấp quyền thực thi:
   ```bash
   chmod +x caro_game
   ./caro_game
