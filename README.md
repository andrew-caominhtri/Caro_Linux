# 🎮 Trò Chơi Cờ Caro (Gomoku)

Chào mừng bạn đến với dự án **Trò Chơi Cờ Caro (Gomoku)**! Đây là một ứng dụng cờ Caro 15x15 hiện đại được viết bằng Python, sở hữu giao diện đồ họa đẹp mắt.

---

## 🌟 Tính Năng Nổi Bật

* **Bàn cờ chuẩn $15 \times 15$:** Giao diện tông màu tối (Cyberpunk style) bắt mắt, thao tác mượt mà.
* **Chế độ chơi đa dạng:**
  * 👥 **Người vs Người (PvP):** Thách đấu cùng bạn bè trên cùng một máy tính.
  * 🤖 **Chơi với Máy (PvE):** Rèn luyện tư duy với thuật toán AI.
* **AI 3 Cấp Độ (Rule-based AI):**
  * 🟢 **Dễ (Easy):** Máy đánh ngẫu nhiên lân cận, phù hợp cho người mới bắt đầu.
  * 🟡 **Vừa (Medium):** Áp dụng thuật toán Heuristic tấn công và phòng thủ cơ bản.
  * 🔴 **Khó (Hard):** Máy tính toán trọng số nước đi gắt gao, nhạy bén phát hiện và ngăn chặn các thế cờ nguy hiểm (thế 3 trống 2 đầu, thế 4 thoáng).
* **Tính di động cao:** Đã được đóng gói độc lập bằng PyInstaller, có thể chạy ngay mà không bắt buộc cài đặt môi trường Python.

---

## 🚀 Hướng Dẫn Tải & Chạy Game

Bạn có thể lựa chọn 1 trong 3 cách dưới đây tùy thuộc vào hệ điều hành và nhu cầu của mình:

### 1. Chạy nhanh trên Linux / WSL (Không cần cài Python)
> **Dành cho người dùng Linux muốn trải nghiệm ngay lập tức.**

1. Truy cập vào mục [Releases](https://github.com/andrew-caominhtri/Caro_Linux/releases) trên GitHub Repository này.
2. Tải về file thực thi nhị phân `caro_game`.
3. Mở Terminal tại thư mục chứa file vừa tải về và chạy các lệnh sau:
   ```bash
   chmod +x caro_game
   ./caro_game

### 2. Chạy nhanh trên Windows (Không cần cài Python)
Dành cho người dùng Windows.

Truy cập mục [Releases](https://github.com/andrew-caominhtri/Caro_Linux/releases) trên GitHub Repository này.

Tải về tập tin caro_game.exe.

Nhấp đôi chuột (Double-click) vào file caro_game.exe để bắt đầu chơi ngay!

### 3. Chạy từ Mã Nguồn (Dành cho Lập trình viên / Cài đặt thủ công)
Dành cho ai muốn chỉnh sửa code hoặc chạy trực tiếp bằng Python.

Clone repository về máy:

```bash
git clone https://github.com/andrew-caominhtri/Caro_Linux.git
cd Caro_Linux
```
Khởi tạo và kích hoạt môi trường ảo (Khuyên dùng):

On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```
On Windows (PowerShell):

```PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
Cài đặt các thư viện phụ thuộc (nếu có):

```bash
pip install -r requirements.txt
```
Khởi chạy trò chơi:

```bash
python3 caro_game.py
```
