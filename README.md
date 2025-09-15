# Bài 3: Kiểm tra tính toàn vẹn dữ liệu bằng MD5

## Giới thiệu
Mục tiêu của bài này là kiểm tra tính toàn vẹn dữ liệu của một file văn bản bằng cách:

1. Tính giá trị **MD5 hash lần 1** cho file gốc.  
2. Chỉnh sửa file (ví dụ thêm 1 ký tự `!` vào cuối).  
3. Tính lại **MD5 hash lần 2**.  
4. So sánh hai kết quả → sẽ thấy khác nhau hoàn toàn, dù chỉ thay đổi rất nhỏ.

---

## Yêu cầu môi trường
- Python **3.8+**  
- Một file văn bản để kiểm tra (ví dụ: `sample_md5_demo.txt`).

---

## Cấu trúc file
```
/project-folder
│── check_md5.py          # Script Python để tính toán và so sánh MD5
│── sample_md5_demo.txt   # File văn bản mẫu để test
│── README.md             # Tài liệu hướng dẫn
```

---

## Hướng dẫn sử dụng

### 1. Chỉnh sửa đường dẫn file trong script
Mở file **`check_md5.py`** và sửa dòng:

```python
FILE_PATH = Path(r"E:\Kiemtratinhtoanvendulieu\sample_md5_demo.txt")
```

Đổi thành đúng đường dẫn nơi bạn lưu file văn bản.

---

### 2. Chạy chương trình
Mở **Command Prompt (Windows)** hoặc **Terminal (Linux/Mac)**, di chuyển đến thư mục chứa `check_md5.py`, sau đó chạy:

```bash
python check_md5.py
```

---

### 3. Quan sát kết quả
Ví dụ output:

```
=== BẮT ĐẦU DEMO MD5 ===
Thời điểm: 2025-09-15 14:20:30
Tệp: E:\Kiemtratinhtoanvendulieu\sample_md5_demo.txt
Kích thước trước khi sửa: 1094 bytes
MD5 lần 1: c8bc0ae36aeba0c26fa8f59b525ee203
Kích thước sau khi sửa: 1095 bytes
MD5 lần 2: 84fa490af418029b8f7e6ffe003f0b40

=== SO SÁNH KẾT QUẢ ===
Hai giá trị MD5 KHÁC NHAU như kỳ vọng. Thay đổi nhỏ đã làm hash thay đổi hoàn toàn.
```

---

## Kết luận
- MD5 có tính chất **avalanche effect**: chỉ cần thay đổi rất nhỏ, kết quả hash đã thay đổi hoàn toàn.  
- Đây là cơ chế phổ biến để **kiểm tra tính toàn vẹn dữ liệu** khi truyền tải hoặc lưu trữ.  
- Tuy nhiên, MD5 không còn an toàn tuyệt đối trước tấn công va chạm, nhưng vẫn thường dùng cho kiểm tra checksum.
