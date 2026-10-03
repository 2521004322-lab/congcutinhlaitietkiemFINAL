import streamlit as st
st.image("logo.jpg")
# ============================================================
# CẤU HÌNH TRANG
# ============================================================

st.set_page_config(
    page_title="Smart Savings Calculator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS - TRANG TRÍ GIAO DIỆN
# ============================================================

st.markdown("""
<style>

    /* Nền tổng thể */
    .stApp {
        background: linear-gradient(135deg, #f5f7fb 0%, #eef3ff 100%);
    }

    /* Tiêu đề */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #173B7A;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        font-size: 17px;
        color: #667085;
        margin-bottom: 30px;
    }

    /* Header */
    .header-box {
        background: linear-gradient(135deg, #173B7A, #2864C7);
        padding: 30px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(23, 59, 122, 0.20);
    }

    .header-box h1 {
        color: white;
        margin-bottom: 8px;
    }

    .header-box p {
        color: #E8F0FF;
        font-size: 16px;
    }

    /* Section */
    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #173B7A;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* Card */
    .info-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        border-left: 5px solid #2864C7;
        box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        margin-bottom: 18px;
    }

    .definition-card {
        background: #F8FAFF;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #DCE6F7;
        margin-bottom: 15px;
    }

    .definition-title {
        color: #173B7A;
        font-size: 19px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    /* Công thức */
    .formula-box {
        background: linear-gradient(135deg, #EEF5FF, #F8FBFF);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #BFD5F5;
        margin: 15px 0;
        text-align: center;
    }

    .formula {
        font-size: 22px;
        font-weight: 700;
        color: #173B7A;
        font-family: "Times New Roman", serif;
        padding: 10px;
    }

    .formula-note {
        color: #667085;
        font-size: 14px;
    }

    /* Result cards */
    .result-card {
        background: white;
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        height: 100%;
    }

    .result-label {
        color: #667085;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .result-value {
        color: #173B7A;
        font-size: 25px;
        font-weight: 800;
    }

    .total-card {
        background: linear-gradient(135deg, #173B7A, #2864C7);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-top: 20px;
        box-shadow: 0 8px 25px rgba(23, 59, 122, 0.25);
    }

    .total-label {
        font-size: 17px;
        color: #DCE8FF;
    }

    .total-value {
        font-size: 34px;
        font-weight: 800;
        color: white;
        margin-top: 8px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: #F7F9FD;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        background: linear-gradient(135deg, #173B7A, #2864C7);
        color: white;
        font-size: 17px;
        font-weight: 700;
        padding: 12px;
        border: none;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #2864C7, #173B7A);
        color: white;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #7A8499;
        padding: 25px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HÀM ĐỊNH DẠNG TIỀN
# ============================================================

def format_money(value):
    return f"{value:,.0f} VNĐ".replace(",", ".")


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="header-box">
    <h1>💰 SMART SAVINGS CALCULATOR</h1>
    <p>
        Công cụ tính lãi tiền gửi tiết kiệm với lãi đơn và lãi kép.
        Nhập thông tin khoản tiền gửi để xem ngay tiền lãi và tổng số tiền nhận được.
    </p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR - NHẬP DỮ LIỆU
# ============================================================

with st.sidebar:

    st.markdown("## 💳 Thông tin tiền gửi")
    st.markdown("---")

    tien_gui = st.number_input(
        "💵 Số tiền gửi (VNĐ)",
        min_value=0,
        value=100_000_000,
        step=1_000_000,
        format="%d"
    )

    ky_han = st.number_input(
        "📅 Kỳ hạn (tháng)",
        min_value=1,
        max_value=120,
        value=12,
        step=1
    )

    lai_suat = st.number_input(
        "📈 Lãi suất (%/năm)",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.1
    )

    hinh_thuc = st.selectbox(
        "💳 Hình thức nhận lãi",
        [
            "Cuối kỳ",
            "Hàng tháng",
            "Hàng quý"
        ]
    )

    loai_lai = st.radio(
        "🔢 Phương pháp tính lãi",
        [
            "Lãi đơn",
            "Lãi kép"
        ]
    )

    st.markdown("---")

    tinh_lai = st.button(
        "🧮 TÍNH TIỀN LÃI"
    )


# ============================================================
# GIẢI THÍCH KHÁI NIỆM
# ============================================================

st.markdown(
    '<div class="section-title">📚 Khái niệm cơ bản</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="definition-card">
        <div class="definition-title">💵 Tiền gốc (P)</div>
        <p>
        Là số tiền ban đầu khách hàng gửi vào ngân hàng.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="definition-card">
        <div class="definition-title">📈 Lãi suất (r)</div>
        <p>
        Là tỷ lệ phần trăm tiền lãi mà ngân hàng trả cho khoản tiền gửi trong một năm.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="definition-card">
        <div class="definition-title">📅 Kỳ hạn (t)</div>
        <p>
        Là khoảng thời gian khách hàng gửi tiền tại ngân hàng, được tính theo tháng.
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CÔNG THỨC
# ============================================================

st.markdown(
    '<div class="section-title">🧮 Công thức tính lãi</div>',
    unsafe_allow_html=True
)

if loai_lai == "Lãi đơn":

    st.markdown("""
    <div class="formula-box">
        <div class="formula">
            I = P × r × t
        </div>
        <div class="formula-note">
            Trong đó: I = tiền lãi &nbsp; | &nbsp;
            P = tiền gốc &nbsp; | &nbsp;
            r = lãi suất theo kỳ &nbsp; | &nbsp;
            t = số kỳ gửi
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "💡 Lãi đơn: tiền lãi được tính dựa trên số tiền gốc ban đầu. "
        "Tiền lãi phát sinh không được cộng vào tiền gốc để tiếp tục sinh lãi."
    )

else:

    st.markdown("""
    <div class="formula-box">
        <div class="formula">
            A = P × (1 + r)<sup>n</sup>
        </div>
        <div class="formula-note">
            Trong đó: A = tổng tiền cuối kỳ &nbsp; | &nbsp;
            P = tiền gốc &nbsp; | &nbsp;
            r = lãi suất mỗi kỳ &nbsp; | &nbsp;
            n = số kỳ ghép lãi
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "💡 Lãi kép: tiền lãi sau mỗi kỳ được cộng vào tiền gốc "
        "và tiếp tục tạo ra tiền lãi ở các kỳ tiếp theo."
    )


# ============================================================
# HÀM TÍNH TOÁN
# ============================================================

def calculate_interest(
    principal,
    months,
    annual_rate,
    interest_type,
    payment_method
):

    # Chuyển lãi suất % thành số thập phân
    r_year = annual_rate / 100

    # Lãi suất theo tháng
    r_month = r_year / 12

    # Số tháng
    n = months

    # --------------------------------------------------------
    # LÃI ĐƠN
    # --------------------------------------------------------

    if interest_type == "Lãi đơn":

        total_interest = principal * r_month * n

        total_amount = principal + total_interest

        monthly_interest = principal * r_month

        quarterly_interest = monthly_interest * 3

        if payment_method == "Hàng tháng":
            periodic_interest = monthly_interest

        elif payment_method == "Hàng quý":
            periodic_interest = quarterly_interest

        else:
            periodic_interest = total_interest

    # --------------------------------------------------------
    # LÃI KÉP
    # --------------------------------------------------------

    else:

        total_amount = principal * (1 + r_month) ** n

        total_interest = total_amount - principal

        monthly_interest = principal * (
            (1 + r_month) ** 1 - 1
        )

        quarterly_interest = principal * (
            (1 + r_month) ** 3 - 1
        )

        if payment_method == "Hàng tháng":
            periodic_interest = monthly_interest

        elif payment_method == "Hàng quý":
            periodic_interest = quarterly_interest

        else:
            periodic_interest = total_interest

    return (
        periodic_interest,
        total_interest,
        total_amount
    )


# ============================================================
# TÍNH VÀ HIỂN THỊ KẾT QUẢ
# ============================================================

if tinh_lai:

    if tien_gui <= 0:
        st.error("⚠️ Vui lòng nhập số tiền gửi lớn hơn 0.")

    elif lai_suat < 0:
        st.error("⚠️ Lãi suất không hợp lệ.")

    else:

        (
            tien_lai_dinh_ky,
            tong_tien_lai,
            tong_tien
        ) = calculate_interest(
            tien_gui,
            ky_han,
            lai_suat,
            loai_lai,
            hinh_thuc
        )

        st.markdown("---")

        st.markdown(
            '<div class="section-title">📊 Kết quả tính toán</div>',
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # 3 KẾT QUẢ CHÍNH
        # ----------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">
                    💵 Tiền lãi định kỳ
                </div>
                <div class="result-value">
                    {format_money(tien_lai_dinh_ky)}
                </div>
                <p style="color:#667085;">
                    {hinh_thuc}
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">
                    📈 Tổng tiền lãi
                </div>
                <div class="result-value">
                    {format_money(tong_tien_lai)}
                </div>
                <p style="color:#667085;">
                    Sau {ky_han} tháng
                </p>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">
                    💰 Tổng tiền gốc + lãi
                </div>
                <div class="result-value">
                    {format_money(tong_tien)}
                </div>
                <p style="color:#667085;">
                    Giá trị cuối kỳ
                </p>
            </div>
            """, unsafe_allow_html=True)

        # ----------------------------------------------------
        # TỔNG TIỀN
        # ----------------------------------------------------

        st.markdown(f"""
        <div class="total-card">
            <div class="total-label">
                💰 TỔNG SỐ TIỀN NHẬN ĐƯỢC
            </div>
            <div class="total-value">
                {format_money(tong_tien)}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ----------------------------------------------------
        # CHI TIẾT KHOẢN GỬI
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">📋 Chi tiết khoản tiền gửi</div>',
            unsafe_allow_html=True
        )

        detail_col1, detail_col2 = st.columns(2)

        with detail_col1:

            st.markdown("""
            <div class="info-card">
            """, unsafe_allow_html=True)

            st.write(f"**💵 Tiền gốc:** {format_money(tien_gui)}")
            st.write(f"**📅 Kỳ hạn:** {ky_han} tháng")
            st.write(f"**📈 Lãi suất:** {lai_suat:.2f}%/năm")

            st.markdown("</div>", unsafe_allow_html=True)

        with detail_col2:

            st.markdown("""
            <div class="info-card">
            """, unsafe_allow_html=True)

            st.write(f"**🔢 Loại lãi:** {loai_lai}")
            st.write(f"**💳 Nhận lãi:** {hinh_thuc}")
            st.write(
                f"**💰 Tiền lãi:** {format_money(tong_tien_lai)}"
            )

            st.markdown("</div>", unsafe_allow_html=True)

        # ----------------------------------------------------
        # GIẢI THÍCH KẾT QUẢ
        # ----------------------------------------------------

        st.markdown(
            '<div class="section-title">📝 Giải thích kết quả</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="info-card">

        Bạn gửi <b>{format_money(tien_gui)}</b> với lãi suất
        <b>{lai_suat:.2f}%/năm</b> trong thời hạn
        <b>{ky_han} tháng</b>.

        <br><br>

        Phương pháp tính được lựa chọn là <b>{loai_lai}</b>
        và hình thức nhận lãi là <b>{hinh_thuc}</b>.

        <br><br>

        ➜ Tổng tiền lãi nhận được:
        <b>{format_money(tong_tien_lai)}</b>.

        <br><br>

        ➜ Tổng số tiền bao gồm cả gốc và lãi:
        <b>{format_money(tong_tien)}</b>.

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# HƯỚNG DẪN SỬ DỤNG
# ============================================================

st.markdown("---")

with st.expander("📖 Hướng dẫn sử dụng"):

    st.markdown("""
    ### Bước 1: Nhập số tiền gửi
    Nhập số tiền ban đầu bạn muốn gửi vào ngân hàng.

    ### Bước 2: Nhập kỳ hạn
    Chọn số tháng muốn gửi tiền.

    ### Bước 3: Nhập lãi suất
    Nhập lãi suất ngân hàng theo %/năm.

    ### Bước 4: Chọn hình thức nhận lãi
    - **Cuối kỳ:** nhận toàn bộ tiền lãi khi kết thúc kỳ hạn.
    - **Hàng tháng:** nhận tiền lãi theo từng tháng.
    - **Hàng quý:** nhận tiền lãi sau mỗi 3 tháng.

    ### Bước 5: Chọn phương pháp tính lãi
    - **Lãi đơn:** tiền lãi chỉ được tính trên số tiền gốc ban đầu.
    - **Lãi kép:** tiền lãi được cộng vào gốc và tiếp tục sinh lãi.

    ### Bước 6: Nhấn "TÍNH TIỀN LÃI"
    Hệ thống sẽ tự động tính:
    - Tiền lãi định kỳ
    - Tổng tiền lãi
    - Tổng tiền gốc + tiền lãi
    """)


# ============================================================
# SO SÁNH LÃI ĐƠN VÀ LÃI KÉP
# ============================================================

with st.expander("📊 Phân biệt lãi đơn và lãi kép"):

    comparison_data = {
        "Tiêu chí": [
            "Cách tính",
            "Tiền lãi có nhập vào gốc?",
            "Cơ sở tính lãi",
            "Tổng tiền cuối kỳ"
        ],
        "Lãi đơn": [
            "Tính trên gốc ban đầu",
            "Không",
            "Gốc ban đầu",
            "P + I"
        ],
        "Lãi kép": [
            "Tính trên gốc + lãi tích lũy",
            "Có",
            "Số dư sau mỗi kỳ",
            "P × (1+r)ⁿ"
        ]
    }

    st.table(comparison_data)


# ============================================================
# LƯU Ý
# ============================================================

st.markdown("---")

st.warning("""
⚠️ **Lưu ý:** Đây là công cụ tính toán mang tính minh họa.
Kết quả thực tế tại ngân hàng có thể khác do cách tính ngày gửi,
ngày đáo hạn, quy định về lãi suất, phương thức trả lãi,
thuế hoặc các điều khoản cụ thể của từng sản phẩm tiền gửi.
""")


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">
    💰 <b>Smart Savings Calculator</b><br>
    Công cụ mô phỏng tính lãi tiền gửi tiết kiệm
</div>
""", unsafe_allow_html=True)
