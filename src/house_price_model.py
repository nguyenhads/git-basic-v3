import csv
import os


def doc_du_lieu(duong_dan):
    du_lieu = []
    with open(duong_dan, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            du_lieu.append({k: float(v) for k, v in row.items()})
    return du_lieu


def tinh_trung_binh(ds):
    return sum(ds) / len(ds)


def huan_luyen_linear_regression(X, y):
    """Hồi quy tuyến tính nhiều biến dùng phương trình chuẩn: w = (X^T X)^-1 X^T y"""
    n = len(X)
    k = len(X[0])

    # Thêm cột bias (x0 = 1)
    X_bias = [[1.0] + row for row in X]
    m = k + 1

    # Tính X^T X
    XTX = [[0.0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for row in X_bias:
                XTX[i][j] += row[i] * row[j]

    # Tính X^T y
    XTy = [0.0] * m
    for i in range(m):
        for idx, row in enumerate(X_bias):
            XTy[i] += row[i] * y[idx]

    # Giải hệ phương trình bằng khử Gauss
    w = giai_he_phuong_trinh(XTX, XTy)
    return w


def giai_he_phuong_trinh(A, b):
    n = len(b)
    # Tạo ma trận mở rộng
    M = [A[i][:] + [b[i]] for i in range(n)]

    for col in range(n):
        # Tìm pivot
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]

        pivot = M[col][col]
        for row in range(col + 1, n):
            factor = M[row][col] / pivot
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    # Thế ngược
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for j in range(i + 1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]

    return x


def du_doan(w, x):
    ket_qua = w[0]
    for i, xi in enumerate(x):
        ket_qua += w[i + 1] * xi
    return ket_qua


def tinh_r2(y_thuc, y_du_doan):
    tb = tinh_trung_binh(y_thuc)
    ss_tot = sum((y - tb) ** 2 for y in y_thuc)
    ss_res = sum((y - yp) ** 2 for y, yp in zip(y_thuc, y_du_doan))
    return 1 - ss_res / ss_tot


def tinh_rmse(y_thuc, y_du_doan):
    mse = sum((y - yp) ** 2 for y, yp in zip(y_thuc, y_du_doan)) / len(y_thuc)
    return mse ** 0.5


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    duong_dan = os.path.join(base_dir, "data", "house_prices.csv")

    print("=== Mô hình dự báo giá nhà (Linear Regression) ===\n")

    du_lieu = doc_du_lieu(duong_dan)
    print(f"Đã tải {len(du_lieu)} mẫu dữ liệu từ {duong_dan}\n")

    features = ["dien_tich", "so_phong_ngu", "so_toilet", "khoang_cach_trung_tam"]
    X = [[row[f] for f in features] for row in du_lieu]
    y = [row["gia_nha"] for row in du_lieu]

    w = huan_luyen_linear_regression(X, y)

    ten_features = ["bias"] + features
    print("Hệ số hồi quy:")
    for ten, he_so in zip(ten_features, w):
        print(f"  {ten:30s}: {he_so:10.4f}")

    y_du_doan = [du_doan(w, x) for x in X]
    r2 = tinh_r2(y, y_du_doan)
    rmse = tinh_rmse(y, y_du_doan)

    print(f"\nĐánh giá mô hình trên tập huấn luyện:")
    print(f"  R²   : {r2:.4f}  (càng gần 1 càng tốt)")
    print(f"  RMSE : {rmse:.2f} triệu đồng")

    print("\n--- Dự báo thử ---")
    nha_moi = [90, 3, 2, 5]
    gia = du_doan(w, nha_moi)
    print(
        f"Nhà {nha_moi[0]}m², {nha_moi[1]} phòng ngủ, "
        f"{nha_moi[2]} toilet, cách TT {nha_moi[3]}km"
    )
    print(f"Giá dự báo: {gia:.0f} triệu đồng")


if __name__ == "__main__":
    main()
