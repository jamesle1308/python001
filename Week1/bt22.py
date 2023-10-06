# Thu nhập tính thuế (năm)
bac_1 = 60000000
bac_2 = 120000000
bac_3 = 216000000
bac_4 = 384000000
bac_5 = 624000000
bac_6 = 960000000


# Thuế suất
thue_suat_1 = 0.05
thue_suat_2 = 0.1
thue_suat_3 = 0.15
thue_suat_4 = 0.2
thue_suat_5 = 0.25
thue_suat_6 = 0.3
thue_suat_7 = 0.35


# Mức giảm trừ (tháng)
giam_tru_doi_tuong_nop_thue = 11000000
giam_tru_moi_nguoi_phu_thuoc = 4400000


# Nhập liệu
tong_thu_nhap_nam = eval(input('Số tiền thu nhập trong năm: '))
so_nguoi_phu_thuoc = int(input('Số người phụ thuộc: '))


# Tính toán
so_tien_giam_tru = (giam_tru_doi_tuong_nop_thue * 12) + (giam_tru_moi_nguoi_phu_thuoc * 12 * so_nguoi_phu_thuoc)
thu_nhap_tinh_thue = tong_thu_nhap_nam - so_tien_giam_tru

if thu_nhap_tinh_thue <= bac_1:
    so_tien_thue = thu_nhap_tinh_thue * thue_suat_1
elif thu_nhap_tinh_thue <= bac_2:
    so_tien_thue = bac_1 * thue_suat_1 + (thu_nhap_tinh_thue - bac_1) * thue_suat_2
elif thu_nhap_tinh_thue <= bac_3:
    so_tien_thue = bac_1 * thue_suat_1 + (bac_2 - bac_1) * thue_suat_2 + (thu_nhap_tinh_thue - bac_2) * thue_suat_3
elif thu_nhap_tinh_thue <= bac_4:
    so_tien_thue = bac_1 * thue_suat_1 + (bac_2 - bac_1) * thue_suat_2 + (bac_3 - bac_2) * thue_suat_3 + (thu_nhap_tinh_thue - bac_3) * thue_suat_4
elif thu_nhap_tinh_thue <= bac_5:
    so_tien_thue = bac_1 * thue_suat_1 + (bac_2 - bac_1) * thue_suat_2 + (bac_3 - bac_2) * thue_suat_3 + (bac_4 - bac_3) * thue_suat_4 + (thu_nhap_tinh_thue - bac_4) * thue_suat_5
elif thu_nhap_tinh_thue <= bac_6:
    so_tien_thue = bac_1 * thue_suat_1 + (bac_2 - bac_1) * thue_suat_2 + (bac_3 - bac_2) * thue_suat_3 + (bac_4 - bac_3) * thue_suat_4 + (bac_5 - bac_4) * thue_suat_5 + (thu_nhap_tinh_thue - bac_5) * thue_suat_6
else:
    so_tien_thue = bac_1 * thue_suat_1 + (bac_2 - bac_1) * thue_suat_2 + (bac_3 - bac_2) * thue_suat_3 + (bac_4 - bac_3) * thue_suat_4 + (bac_5 - bac_4) * thue_suat_5 + (bac_6 - bac_5) * thue_suat_6 + (thu_nhap_tinh_thue - bac_6) * thue_suat_7


# Xuất kết quả
print('-' * 40)
print('Số tiền giảm trừ:', '{:,}'.format(so_tien_giam_tru))
print('Số tiền chịu thuế:', '{:,}'.format(thu_nhap_tinh_thue))
print('Tiền thuế:', '{:,}'.format(round(so_tien_thue)))
