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

## � Cách sử dụng Miniconda

### 📍 Vị trí Miniconda
```
C:\Users\ADMIN\miniconda3
```

### 🚀 Tạo Môi trường mới

```bash
# Tạo môi trường với Python 3.11
conda create -n my_env python=3.11

# Tạo môi trường với Python 3.12
conda create -n my_env python=3.12 -y
```

### 🔄 Quản lý Môi trường

```bash
# Liệt kê tất cả các môi trường
conda env list

# Kích hoạt môi trường
conda activate my_env

# Deactivate môi trường
conda deactivate

# Xóa môi trường
conda remove -n my_env --all
```

### 📦 Cài đặt Packages

```bash
# Cài package từ conda
conda install numpy pandas matplotlib

# Cài package từ pip
pip install requests beautifulsoup4

# Cài từ requirements.txt
pip install -r requirements.txt
```

### 💡 Ví dụ Workflow

```bash
# 1. Tạo môi trường
conda create -n ai_project python=3.11 -y

# 2. Kích hoạt
conda activate ai_project

# 3. Cài các package cần thiết
pip install numpy pandas scikit-learn matplotlib

# 4. Chạy code
python main.py

# 5. Deactivate khi xong
conda deactivate
```

### 🎯 Thực hành từ thư mục `src`

```bash
# Di chuyển đến thư mục src
cd C:\Users\ADMIN\Documents\GitHub\Series_AI\AI\Python_Advance_to_Pro\Basic\src

# Tạo môi trường
conda create -n basic_env python=3.11 -y

# Kích hoạt
conda activate basic_env

# Cài pip packages
pip install -r ../requirements.txt

# Chạy file Python
python Comprehension.py
```

---

## 📌 Notes

> Nếu chưa cài Python, lệnh `python --version` có thể trigger cài đặt bản mặc định.
> Miniconda đã sẵn sàng sử dụng từ bất kỳ đường dẫn nào trên hệ thống.

---

## ❤️ Contribute

Feel free to fork & improve this cheatsheet 🚀

---

## 📄 License

MIT License



---

## 📦 Python Built-in Types & Methods

| Type  | Key Methods |
|-------|------------|
| 🔢 int/float | int(), float(), abs(), sqrt() |
| 🔤 str | upper(), len(), isdigit(), center() |
| 📋 list | list(), append(), insert(), len() |
| 📦 tuple | tuple(), len(), max(), min() |
| 🧩 set | add(), remove(), pop(), clear() |
| 🗂️ dict | keys(), items(), copy(), clear() |
| 📄 file | read(), write(), mode, name |