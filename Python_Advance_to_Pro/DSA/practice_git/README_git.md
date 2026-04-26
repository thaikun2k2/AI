Dưới đây là **file `README.md` hoàn chỉnh** (tổng hợp full kiến thức Git từ cơ bản → nâng cao, theo kiểu course Udemy bạn gửi). Bạn chỉ cần **copy → dán vào file README.md là dùng được ngay**.

---


|                        | Public Key             | Private Key   |
| ---------------------- | ---------------------- | ------------- |
| 📌 Mục đích            | Chia sẻ cho người khác | Giữ bí mật    |
| 🔐 Vai trò             | Mã hóa / xác thực      | Giải mã / ký  |
| 📤 Có thể gửi đi?      | ✔ Có                   | ❌ Không       |
| 💥 Lộ ra có sao không? | Không sao              | Nguy hiểm cực |


~/.ssh/id_ed25519        # private key
~/.ssh/id_ed25519.pub    # public key


ADMIN@DESKTOP-1URNQ5U MINGW64 ~
$

ADMIN@DESKTOP-1URNQ5U MINGW64 ~
$ ssh-keygen -t ed25519 -C "thaikun2k2@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/ADMIN/.ssh/id_ed25519):
Enter passphrase for "/c/Users/ADMIN/.ssh/id_ed25519" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/ADMIN/.ssh/id_ed25519
Your public key has been saved in /c/Users/ADMIN/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:cXzrJNiH7voaOvvS4bIHD3OiBgi5ZCA9JNyx2ScalRQ thaikun2k2@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|ooo.oEo          |
|ooo.=.   .       |
|o. = o .. o .    |
|oo  o o  = o .   |
|+o .    S + +    |
|o .   = o. =     |
|   . . X... .    |
|    o +.=o       |
|   .  +O++o      |
+----[SHA256]-----+

ADMIN@DESKTOP-1URNQ5U MINGW64 ~
$

ADMIN@DESKTOP-1URNQ5U MINGW64 ~
$ cat /c/Users/ADMIN/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF8E8a5I/4C63b2bWr/0X/6sbWjcK0rOCdpgYTZ8RL7F thaikun2k2@gmail.com

ADMIN@DESKTOP-1URNQ5U MINGW64 ~
$ ssh -T git@github.com
Hi thaikun2k2! You've successfully authenticated, but GitHub does not provide shell access.


####
git push --set-upstream origin main

==
git push -u origin main
####


````markdown
# 🚀 Git & GitHub Complete Guide (A → Z)

## 📌 1. Git là gì?
Git là hệ thống quản lý version control giúp:
- Theo dõi thay đổi code
- Làm việc nhóm dễ dàng
- Rollback khi có lỗi  

👉 Git lưu lại toàn bộ lịch sử project :contentReference[oaicite:0]{index=0}  

---

## ⚙️ 2. Cài đặt & Config

### Kiểm tra Git
```bash
git --version
````

### Cấu hình user

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

👉 Dùng để gắn thông tin commit ([TutorialsPoint][1])

---

## 📁 3. Khởi tạo Repository

### Tạo repo mới

```bash
git init
```

### Clone repo từ remote

```bash
git clone <repo_url>
```

👉 `git init` tạo repo local, `git clone` copy repo từ server ([Tower][2])

---

## 🔄 4. Git Workflow (Quan trọng nhất)

```
Working Directory → Staging Area → Repository
```

### Step chuẩn:

```bash
git status        # kiểm tra trạng thái
git add .         # đưa code vào staging
git commit -m "message"
git push          # đẩy lên remote
```

👉 Đây là flow dùng 90% thời gian ([GeeksforGeeks][3])

---

## 📌 5. Các lệnh cơ bản

### Kiểm tra trạng thái

```bash
git status
```

### Add file

```bash
git add <file>
git add .
```

### Commit

```bash
git commit -m "message"
```

### Xem lịch sử

```bash
git log
git log --oneline
```

👉 `git add` đưa file vào staging, `commit` lưu snapshot ([Atlassian][4])

---

## 🌿 6. Branch & Merge

### Tạo branch

```bash
git branch <name>
```

### Chuyển branch

```bash
git checkout <name>
```

### Tạo + chuyển luôn

```bash
git checkout -b <name>
```

### Merge

```bash
git merge <branch>
```

👉 Branch giúp dev song song mà không conflict ([Tower][2])

---

## ☁️ 7. Remote (GitHub)

### Thêm remote

```bash
git remote add origin <url>
```

### Push code

```bash
git push -u origin main
```

### Pull code

```bash
git pull
```

👉 `push` gửi code lên server, `pull` lấy code mới ([Simplilearn.com][5])

---

## 🔍 8. Kiểm tra & So sánh

```bash
git diff
git diff --staged
git show <commit>
```

---

## 🔙 9. Undo / Fix lỗi

### Bỏ stage

```bash
git reset HEAD <file>
```

### Undo commit (giữ code)

```bash
git reset --soft HEAD~1
```

### Reset cứng (⚠️ nguy hiểm)

```bash
git reset --hard HEAD~1
```

### Revert (an toàn)

```bash
git revert <commit>
```

👉 `revert` tạo commit ngược lại thay vì xóa history

---

## 📦 10. Stash (tạm lưu code)

```bash
git stash
git stash list
git stash apply
```

👉 Dùng khi đang code dở muốn switch branch ([Simplilearn.com][5])

---

## 🌐 11. Fetch vs Pull

```bash
git fetch   # chỉ tải về
git pull    # tải + merge
```

---

## 🔧 12. Một số lệnh nâng cao

```bash
git rebase
git cherry-pick <commit>
git blame <file>
git reflog
git clean -fd
```

---

## 🧠 13. Best Practice

* Commit nhỏ, rõ ràng
* Luôn pull trước khi push
* Dùng branch cho feature
* Không commit file nhạy cảm (.env)
* Viết commit message rõ nghĩa

---

## 📊 14. Git Flow (Chuẩn thực tế)

```
main/master → production
develop → dev
feature/* → develop
hotfix/* → main
```

---

## ⚡ 15. Cheat Sheet nhanh

```bash
git init
git clone
git status
git add .
git commit -m "msg"
git push
git pull
git branch
git checkout -b new-branch
git merge
```

---

## 🎯 Tổng kết

* Git = quản lý version
* GitHub = lưu trữ remote
* Workflow = add → commit → push
* Branch = làm việc nhóm

---

## 📚 Tài liệu tham khảo

* [https://git-scm.com](https://git-scm.com)
* [https://www.atlassian.com/git](https://www.atlassian.com/git)
* [https://www.geeksforgeeks.org/git](https://www.geeksforgeeks.org/git)

---

🔥 DONE — Bạn đã có full Git từ A → Z

```

---

[1]: https://www.tutorialspoint.com/git/git-basic-commands.htm?utm_source=chatgpt.com "Git - Basic Commands"
[2]: https://www.git-tower.com/learn/git/commands?utm_source=chatgpt.com "Git Commands | Learn Version Control with Git"
[3]: https://www.geeksforgeeks.org/git/useful-github-commands/?utm_source=chatgpt.com "50+ Essential Git Commands for Beginners and Developers - GeeksforGeeks"
[4]: https://www.atlassian.com/git/glossary?utm_source=chatgpt.com "Basic Git Commands | Atlassian Git Tutorial"
[5]: https://www.simplilearn.com/tutorials/git-tutorial/git-commands?utm_source=chatgpt.com "Basic Git Commands You Need to Know | Simplilearn"
