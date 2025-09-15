# Bài 3. Kiểm tra tính toàn vẹn dữ liệu bằng MD5.
# - Tính MD5 cho một file văn bản.
# - Chỉnh sửa nội dung file (thêm 1 ký tự), tính lại MD5 và so sánh.
# Yêu cầu: Dùng thư viện chuẩn hashlib (MD5).

import hashlib
from pathlib import Path
from datetime import datetime

CHUNK_SIZE = 1024 * 1024  # 1MB
FILE_PATH = Path(r"E:\Kiemtratinhtoanvendulieu\sample_md5_demo.txt")

def md5_of_file(path: Path) -> str:
    """Tính MD5 của file bằng cách đọc theo khối để hỗ trợ file lớn."""
    md5 = hashlib.md5()
    with path.open("rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            md5.update(chunk)
    return md5.hexdigest()

def append_one_char(path: Path, char: str = "!") -> None:
    """Sửa file bằng cách thêm một ký tự (mặc định '!')."""
    with path.open("ab") as f:
        f.write(char.encode("utf-8"))

def main():
    print("=== BẮT ĐẦU DEMO MD5 ===")
    print(f"Thời điểm: {datetime.now().isoformat(sep=' ', timespec='seconds')}")
    print(f"Tệp: {FILE_PATH.resolve()}")
    print(f"Kích thước trước khi sửa: {FILE_PATH.stat().st_size} bytes")

    # 1) Tính hash lần 1
    md5_1 = md5_of_file(FILE_PATH)
    print(f"MD5 lần 1: {md5_1}")

    # 2) Sửa file rất nhỏ (thêm 1 ký tự)
    append_one_char(FILE_PATH, "!")

    # 3) Tính hash lần 2
    md5_2 = md5_of_file(FILE_PATH)
    print(f"Kích thước sau khi sửa: {FILE_PATH.stat().st_size} bytes")
    print(f"MD5 lần 2: {md5_2}")

    # 4) So sánh
    print("\n=== SO SÁNH KẾT QUẢ ===")
    if md5_1 == md5_2:
        print("Hai giá trị MD5 GIỐNG NHAU (không kỳ vọng). Có thể đã chạy mà không sửa tệp.")
    else:
        print("Hai giá trị MD5 KHÁC NHAU như kỳ vọng. Thay đổi nhỏ đã làm hash thay đổi hoàn toàn.")

if __name__ == "__main__":
    main()
