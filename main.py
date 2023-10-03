import numpy as np

def tinh_nghich_dao(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        try:
            nghich_dao = np.linalg.inv(matrix)
            return nghich_dao
        except np.linalg.LinAlgError:
            return None
    else:
        return None

def kiem_tra_tinh_chat_nghich_dao(matrix):
    if matrix.shape[0] == matrix.shape[1]:
        nghich_dao = tinh_nghich_dao(matrix)
        if nghich_dao is not None:
            tich = np.matmul(matrix, nghich_dao)
            don_vi = np.eye(matrix.shape[0])
            if np.allclose(tich, don_vi):
                return True
    return False

# Ví dụ sử dụng các hàm tính toán

# Tạo ma trận ngẫu nhiên có kích thước lớn
kich_thuoc = 1000
ma_tran = np.random.rand(kich_thuoc, kich_thuoc)

# Tính nghịch đảo của ma trận
nghich_dao = tinh_nghich_dao(ma_tran)
if nghich_dao is not None:
    print("Ma trận nghịch đảo:")
    print(nghich_dao)
else:
    print("Ma trận không có nghịch đảo.")

# Kiểm tra tính chất nghịch đảo của ma trận
if kiem_tra_tinh_chat_nghich_dao(ma_tran):
    print("Ma trận thỏa tính chất nghịch đảo.")
else:
    print("Ma trận không thỏa tính chất nghịch đảo.")