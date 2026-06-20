## Q3
```
Câu hỏi: Khôi phục file về trạng thái trước khi chỉnh sửa (chưa commit)?
Tình huống: bạn sửa main.py nhưng chưa git add, muốn bỏ hết thay đổi về như ban đầu.


git restore main.py
→ File trở về đúng như lần commit cuối cùng. Thay đổi bị xóa vĩnh viễn.

Tại sao 3 đáp án kia sai?
git reset --hard (vàng)

→ Reset toàn bộ repo về commit cũ, không phải từng file riêng lẻ. Đây là lệnh "nặng" hơn và nguy hiểm hơn.

git rebase --abort (đỏ)

→ Chỉ dùng khi đang bị kẹt giữa chừng một lần git rebase. Không liên quan đến khôi phục file.

git rebase <branch> (xanh lá)

→ Dùng để di chuyển nhánh lên trên một nhánh khác. Hoàn toàn không liên quan.

Bảng tóm tắt các lệnh undo

Tình huống                          Lệnh
────────────────────────────────────────────────────
Sửa file, chưa add, muốn bỏ        git restore <file>
Add rồi, muốn bỏ khỏi staging      git restore --staged <file>
Commit rồi, muốn undo (an toàn)    git revert HEAD
Commit rồi, muốn xóa (nguy hiểm)  git reset --hard HEAD~1
```

## Q4

```
Phân tích câu hỏi
Các bước cần sắp xếp:

1/ git add .
2/ git init
3/ git remote add origin <url>
4/ git commit -m "message"
5/ git push origin main

Đáp án đúng: Tam giác đỏ — 2, 1, 4, 3, 5

git init → git add . → git commit → git remote add → git push
Lý do từng bước:

Thứ tự	Lệnh	Lý do bắt buộc
1st	git init	Phải tạo repo trước, chưa có repo thì không làm gì được
2nd	git add .	Stage files trước khi commit
3rd	git commit	Phải có commit mới push được
4th	git remote add	Kết nối remote trước khi push
5th	git push	Cuối cùng mới push lên

Tại sao các đáp án khác sai?

Xanh dương (2, 3, 1, 4, 5) — git remote add trước git add .
→ Về mặt kỹ thuật không lỗi, nhưng không đúng thứ tự logic tự nhiên và không phải workflow chuẩn.

Vàng (3, 2, 1, 4, 5) — bắt đầu bằng git remote add
→ Sai, vì chưa git init thì không thể add remote (chưa có .git folder).

Xanh lá (1, 2, 3, 4, 5) — bắt đầu bằng git add .
→ Sai, git add trước git init sẽ báo lỗi ngay: "not a git repository".

Lưu ý: Quiz đánh dấu đáp án xanh dương nhưng đó là nhầm — thứ tự chuẩn nhất và được dạy rộng rãi nhất là đỏ (2, 1, 4, 3, 5).
```

## Q6

```
Đáp án: "File có trên branch mới nhưng chưa được theo dõi" ✓
Lý do
File chưa git add = file untracked — Git hoàn toàn không biết file này tồn tại, không gắn nó với bất kỳ branch nào.

Vì vậy khi bạn git checkout other-branch:


Branch main:    README.md (tracked) + new_file.py (UNTRACKED)
                                              ↓
git checkout other-branch                     ↓ (Git không đụng vào)
                                              ↓
Branch other:   README.md (tracked) + new_file.py (vẫn còn đó, vẫn untracked)
File theo bạn sang branch mới vì Git chỉ quản lý những gì đã được track.

Tại sao 3 đáp án kia sai?
"File sẽ biến mất ở branch mới" (đỏ)
→ Sai. Git không xóa untracked files khi đổi branch.

"File được tự động thêm vào stage ở branch mới" (xanh dương)
→ Sai. Git không tự động stage bất cứ thứ gì.

"Git sẽ báo lỗi khi chuyển branch" (xanh lá)
→ Sai với untracked file. Git chỉ báo lỗi nếu file đã được tracked và có thay đổi chưa commit mà bị conflict với branch đích.

Thực tế cần nhớ

Trạng thái file     Khi đổi branch
──────────────────────────────────────────────
Untracked           Theo bạn sang branch mới (không mất)
Staged (git add)    Theo bạn sang branch mới (vẫn staged)
Committed           Ở lại branch cũ — branch mới không có
Kết luận: Chỉ những gì đã commit mới thực sự "thuộc về" một branch.
```
