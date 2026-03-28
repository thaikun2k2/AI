# 🐍 Python Version Manager Cheatsheet

<p align="center">
  <b>Quản lý nhiều phiên bản Python dễ dàng với <code>py</code></b><br>
  Nhanh • Gọn • Chuẩn Dev
</p>

---

## 🚀 Features

* ✅ Quản lý nhiều version Python song song
* ✅ Cài / gỡ version nhanh chóng
* ✅ Chạy Python theo version cụ thể
* ✅ Tích hợp tốt với `venv`

---

## 📊 Commands Overview

| Action                     | Command                  | Description               |
| -------------------------- | ------------------------ | ------------------------- |
| 📦 List installed versions | `py list`                | Xem các bản Python đã cài |
| 🌐 List available versions | `py list --online`       | Xem các bản có thể cài    |
| ⬇️ Install Python          | `py install <version>`   | Cài version cụ thể        |
| ❌ Uninstall Python         | `py uninstall <version>` | Gỡ version                |
| 🔍 Check current version   | `python --version`       | Xem version hiện tại      |
| ▶️ Run specific version    | `py -<version>`          | Chạy Python theo version  |
| 📄 Run file with version   | `py -<version> file.py`  | Chạy file với version     |

---

## ⚡ Quick Start

```bash
# Xem version có thể cài
py list --online

# Cài Python
py install 3.12

# Tạo môi trường ảo
py -3.12 -m venv venv

# Kích hoạt (Windows)
venv\Scripts\activate

# Kiểm tra
python --version
```

---

## 🧪 Examples

### Install Python

```bash
py install 3.14
py install 3.14.3
```

### Uninstall Python

```bash
py uninstall 3.14.3
```

### Run Python

```bash
py -3.14
py -3.14 main.py
```

---

## 🧠 Best Practices

* 🔒 Luôn dùng version cố định cho từng project
* 📁 Không dùng Python global cho production
* 🧪 Luôn dùng `venv` để cách ly môi trường
* 🏷️ Đặt tên môi trường rõ ràng (`venv`, `env_project`)

---

## 📁 Recommended Project Structure

```
project/
│── venv/
│── src/
│── requirements.txt
│── README.md
```

---

## 🔥 Pro Tips

* Dùng `py` thay vì `python` khi làm multi-version
* Kết hợp với Docker nếu deploy production
* Version mismatch = bug tiềm ẩn ⚠️

---

## 📌 Notes

> Nếu chưa cài Python, lệnh `python --version` có thể trigger cài đặt bản mặc định.

---

## ❤️ Contribute

Feel free to fork & improve this cheatsheet 🚀

---

## 📄 License

MIT License
