def tinh_bmi(can_nang, chieu_cao):
    return can_nang / (chieu_cao**2)


def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    else:
        return "Béo phì"


def main():
    print("=== Chương trình tính BMI ===")
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))

    bmi = tinh_bmi(can_nang, chieu_cao)
    phan_loai = phan_loai_bmi(bmi)

    print(f"\nBMI của bạn: {bmi:.2f}")
    print(f"Phân loại: {phan_loai}")
    print("\nCảm ơn bạn đã sử dụng chương trình!")


if __name__ == "__main__":
    main()
