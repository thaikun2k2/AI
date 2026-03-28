# Git Cheatsheet & Common Fixes

## 1. Bắt đầu với Git

1. Kiểm tra trạng thái hiện tại:
   - `git status`

2. Thêm thay đổi vào stage:
   - `git add <file>`
   - `git add .` (tất cả thay đổi)

3. Commit:
   - `git commit -m "Your message"`

4. Đẩy lên remote:
   - `git push origin main`

5. Kéo về remote (cập nhật):
   - `git pull origin main`

6. Xem lịch sử commit:
   - `git log --oneline --graph --decorate --all`

---

## 2. Thiết lập Git (thường cần khi mới cài máy)

- `git config --global user.name "Your Name"`
- `git config --global user.email "you@example.com"`

Kiểm tra:
- `git config --global --list`

---

## 3. Cấu hình credential (Windows)

- `git config --global credential.helper wincred`

---

## 4. Phương án xác thực với GitHub

### A. HTTPS + PAT (Recommended)

1. Tạo Personal Access Token trên GitHub (Settings > Developer settings > Personal access tokens > Tokens (classic)).
2. Chọn scope: `repo` (và `workflow` nếu cần), ghi nhớ token.
3. Đẩy code bằng lệnh bình thường; khi hỏi password, dán token.

### B. SSH key

1. Tạo key:
   - `ssh-keygen -t ed25519 -C "you@example.com"`
2. Add key vào SSH agent:
   - `eval $(ssh-agent -s)`
   - `ssh-add ~/.ssh/id_ed25519`
3. Sao chép `~/.ssh/id_ed25519.pub` lên GitHub > Settings > SSH and GPG keys.
4. đổi remote URL:
   - `git remote set-url origin git@github.com:USER/REPO.git`
5. Test:
   - `ssh -T git@github.com`

---

## 5. Lỗi phổ biến và cách fix

### Lỗi 1: `Author identity unknown` / `unable to auto-detect email address`

Dấu hiệu:
- Khi chạy `git commit`, xuất hiện thông báo yêu cầu user.name và user.email.

Cách fix:
- `git config --global user.name "Your Name"`
- `git config --global user.email "you@example.com"`

### Lỗi 2: `remote: Invalid username or token. Password authentication is not supported for Git operations.`

Dấu hiệu:
- `git push` thất bại, thông báo rằng password không hợp lệ.

Cách fix (HTTPS):
- Tạo PAT trên GitHub (scope `repo`).
- Dùng token như password khi push.

Cách fix (SSH):
- Sử dụng SSH key như phần trên, không dùng token/password.

### Lỗi 3: `failed to push some refs` / `non-fast-forward`

Dấu hiệu:
- `git push` báo error, cần `git pull` trước.

Cách fix:
- `git pull --rebase origin main`
- Giải quyết conflict nếu có
- `git push origin main`

### Lỗi 4: `detached HEAD` / không ở nhánh

Dấu hiệu:
- `git status` báo `HEAD detached at ...`.

Cách fix:
- Thoát bằng `git checkout main` (hoặc tên nhánh mà bạn làm việc).
- Nếu muốn giữ commit tạm vào nhánh mới:
  - `git checkout -b my-branch`

---

## 6. Quy trình an toàn khi sửa lỗi

1. `git status`
2. `git pull --rebase origin main`
3. `git add` + `git commit`
4. `git push origin main`

---

## 7. Backup nhanh khi sợ mất dữ liệu

- `git stash` (lưu thay đổi chưa commit tạm thời)
- `git stash pop` (lấy lại)

---

## 8. Kiểm tra remote URL

- `git remote -v`

Nếu remote sai: `git remote set-url origin <url mới>`

---

## 9. Thực thi sau khi sửa README.md và lỗi vừa xong

```powershell
cd C:\Users\ADMIN\Documents\GitHub\AI
git add Python_Advance_to_Pro/Basic/README.md
git commit -m "Update README.md"
git push origin main
```

Nếu vẫn fail, chạy thêm `git pull --rebase origin main` rồi thử lại.
