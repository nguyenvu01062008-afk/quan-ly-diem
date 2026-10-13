import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu mẫu
data = {
    'Ho_ten': ['An', 'Binh', 'Chi', 'Dung', 'Ha', 'Lan', 'Minh', 'Nam', 'Phuc', 'Trang'],
    'Chuyen_can': [8, 9, 7, 10, 8, 6, 9, 7, 8, 9],
    'Giua_ky': [7, 8, 6, 9, 7, 6, 8, 7, 7, 9],
    'Cuoi_ky': [7.5, 8.5, 6.5, 9.5, 7, 6, 8.5, 7, 7.5, 9]
}
df = pd.DataFrame(data)

df['Tong_ket'] = 0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']

def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm tổng hợp")
st.dataframe(df)

st.subheader("Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
max_sv = df.loc[df['Tong_ket'].idxmax()]
min_sv = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()

st.write(f"- Điểm trung bình lớp: **{dtb_lop:.2f}**")
st.write(f"- Sinh viên cao nhất: **{max_sv['Ho_ten']}** ({max_sv['Tong_ket']:.2f} điểm)")
st.write(f"- Sinh viên thấp nhất: **{min_sv['Ho_ten']}** ({min_sv['Tong_ket']:.2f} điểm)")
st.write(f"- Số sinh viên đạt (>= 5 điểm): **{so_sv_dat}**")

st.subheader("Tra cứu thông tin cá nhân")
ten_chon = st.selectbox("Chọn tên sinh viên cần xem:", df['Ho_ten'])
sv_chon = df[df['Ho_ten'] == ten_chon].iloc[0]

st.write(f"Họ tên: **{sv_chon['Ho_ten']}** | Chuyên cần: **{sv_chon['Chuyen_can']}** | Giữa kỳ: **{sv_chon['Giua_ky']}** | Cuối kỳ: **{sv_chon['Cuoi_ky']}** | Tổng kết: **{sv_chon['Tong_ket']:.2f}** | Xếp loại: **{sv_chon['Xep_loai']}**")

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(df['Ho_ten'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Điểm Tổng Kết')
ax.set_ylabel('Sinh Viên')
st.pyplot(fig)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: small;'>Người thực hiện: Trần Ngọc Nguyên Vũ - MSSV: 066208014402</p>", unsafe_allow_html=True)
