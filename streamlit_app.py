# -*- coding: utf-8 -*-
import os
import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------------
st.set_page_config(
    page_title="Distributor Sales & Contract Agentic System | Antigravity BI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Streamlit Interface
st.markdown("""
<style>
    /* Dark Theme Global Styling */
    .stApp {
        background-color: #0A0F1D;
        color: #F8FAFC;
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    }
    
    /* Header Bar */
    .top-hero-banner {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.15) 0%, rgba(59, 130, 246, 0.15) 50%, rgba(139, 92, 246, 0.15) 100%);
        border: 1px solid rgba(6, 182, 212, 0.3);
        border-radius: 16px;
        padding: 20px 28px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
    }
    
    .hero-title {
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        background: linear-gradient(135deg, #ffffff 20%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .hero-subtitle {
        font-size: 0.9rem;
        color: #94a3b8;
        margin-top: 4px;
    }
    
    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.4);
        color: #34d399;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
    }
    
    /* Metrics Row */
    .metric-box {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 14px 18px;
        text-align: center;
    }
    .metric-box-val {
        font-size: 1.4rem;
        font-weight: 800;
        color: #38bdf8;
    }
    .metric-box-label {
        font-size: 0.78rem;
        color: #94a3b8;
        margin-top: 2px;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0F172A !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    /* Hide Default Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        max-width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# HELPER FUNCTIONS TO LOAD FILES
# -------------------------------------------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))

def get_file_content(relative_paths):
    for rel_path in relative_paths:
        full_path = os.path.join(current_dir, rel_path)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                return f.read(), full_path
    return None, None

def get_binary_content(relative_paths):
    for rel_path in relative_paths:
        full_path = os.path.join(current_dir, rel_path)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return f.read(), full_path
    return None, None

# Load resources
slide_html, slide_path = get_file_content([
    "Project cuối khóa/Slide_Thuyet_Trinh_Project_Cuoi_Khoa.html",
    "outputs/reports/Slide_Thuyet_Trinh_Project_Cuoi_Khoa.html",
    "Slide_Thuyet_Trinh_Project_Cuoi_Khoa.html"
])

dash_html, dash_path = get_file_content([
    "Project cuối khóa/Dashboard_Tong_Quan_Doanh_So_NPP.html",
    "outputs/reports/NPP_Sales_Coverage_Dashboard.html",
    "Dashboard_Tong_Quan_Doanh_So_NPP.html"
])

spec_md, spec_path = get_file_content([
    "outputs/reports/Distributor_Sales_Contract_Agentic_System_Spec.md",
    "Distributor_Sales_Contract_Agentic_System_Spec.md"
])

# -------------------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
        <div style="background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%); width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; color: white;">
            ⚡
        </div>
        <div>
            <div style="font-weight: 800; font-size: 0.95rem; color: #f8fafc;">ANTIGRAVITY BI</div>
            <div style="font-size: 0.75rem; color: #38bdf8; font-weight: 600;">PROJECT CUỐI KHÓA</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🧭 ĐIỀU HƯỚNG DỰ ÁN")
    menu = st.radio(
        "Chọn nội dung xem:",
        [
            "🖥️ Slide Thuyết Trình (7 Slide Deck)",
            "📊 Executive Live Dashboard",
            "📑 Hồ Sơ Kiến Trúc & 8 Test Cases",
            "📦 Tải Về Trọn Gói (Download)"
        ],
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📈 THÔNG SỐ HỆ THỐNG")
    st.markdown("""
    * **Mô hình:** Multi-Agent 3 Tầng
    * **Quy mô:** 30 NPP Toàn quốc (Á Mỹ & Bernini)
    * **Tốc độ:** &lt; 10 Phút / HĐ *(Nhanh hơn 95%)*
    * **Độ chính xác:** 100% Khớp nối T1–T12
    * **Kiến trúc:** 7 Sheet Master Dynamic SUMIFS
    * **Test Cases:** 8/8 Kịch bản Nghiệm thu Pass
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.75rem; color: #64748b; line-height: 1.4;">
        Khóa học: Agentic AI with Google Antigravity<br>
        Tác giả: Học Viên Antigravity (Sales & BI)
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# MAIN CONTENT AREA
# -------------------------------------------------------------

# Top Header Banner
st.markdown("""
<div class="top-hero-banner">
    <div>
        <div class="badge-pill">● AGENTIC MULTI-AGENT SYSTEM</div>
        <h1 class="hero-title">HỆ THỐNG TỰ ĐỘNG HÓA DOANH SỐ NPP THEO HỢP ĐỒNG</h1>
        <div class="hero-subtitle">Distributor Sales & Contract Agentic System — Tự Động Hóa Đối Soát Cam Kết vs Thực Tế & Quản Trị Độ Phủ NPP</div>
    </div>
    <div style="display: flex; gap: 12px;">
        <div class="metric-box">
            <div class="metric-box-val">&lt; 10m</div>
            <div class="metric-box-label">Xử lý HĐ</div>
        </div>
        <div class="metric-box">
            <div class="metric-box-val">100%</div>
            <div class="metric-box-label">Chính xác</div>
        </div>
        <div class="metric-box">
            <div class="metric-box-val">7 Sheet</div>
            <div class="metric-box-label">Master SUMIFS</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# VIEW 1: SLIDE THUYẾT TRÌNH
if menu == "🖥️ Slide Thuyết Trình (7 Slide Deck)":
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
        <div style="font-size: 0.9rem; color: #94a3b8;">
            💡 <strong>Mẹo trình chiếu:</strong> Nhấp vào khung slide và dùng phím <code>→</code> / <code>Space</code> để chuyển tiếp, <code>←</code> để quay lại, <code>F</code> để toàn màn hình, <code>N</code> để mở Speaker Notes, hoặc <code>D</code> để xem Live Dashboard.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if slide_html:
        components.html(slide_html, height=860, scrolling=False)
    else:
        st.error("Không tìm thấy file Slide HTML. Vui lòng kiểm tra đường dẫn thư mục.")

# VIEW 2: EXECUTIVE LIVE DASHBOARD
elif menu == "📊 Executive Live Dashboard":
    st.markdown("""
    <div style="margin-bottom: 12px; font-size: 0.9rem; color: #94a3b8;">
        📊 <strong>Executive Live Dashboard:</strong> Trực quan hóa độ phủ NPP 3 Miền, tiến độ cam kết vs thực tế, cảnh báo nguy cơ hụt chỉ tiêu và cơ chế duyệt kế hoạch mở mới.
    </div>
    """, unsafe_allow_html=True)
    
    if dash_html:
        components.html(dash_html, height=920, scrolling=True)
    else:
        st.error("Không tìm thấy file Dashboard HTML. Vui lòng kiểm tra đường dẫn thư mục.")

# VIEW 3: HỒ SƠ KIẾN TRÚC & 8 TEST CASES
elif menu == "📑 Hồ Sơ Kiến Trúc & 8 Test Cases":
    if spec_md:
        st.markdown(spec_md)
    else:
        st.info("Hồ sơ đặc tả kỹ thuật chi tiết (`Distributor_Sales_Contract_Agentic_System_Spec.md`).")

# VIEW 4: TẢI VỀ TRỌN GÓI
elif menu == "📦 Tải Về Trọn Gói (Download)":
    st.markdown("### 📥 TẢI VỀ CÁC TÀI NGUYÊN VÀ BẢN ĐÓNG GÓI")
    st.write("Bạn có thể tải trực tiếp các tệp tin để xem ngoại tuyến hoặc chuyển tiếp cho đồng nghiệp:")
    
    col1, col2, col3 = st.columns(3)
    
    # Pack ZIP
    zip_bytes, zip_real_path = get_binary_content([
        "Project cuối khóa/Slide_Thuyet_Trinh_Project_Cuoi_Khoa_Portable.zip",
        "outputs/reports/Slide_Thuyet_Trinh_Project_Cuoi_Khoa_Portable.zip"
    ])
    
    with col1:
        st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(6, 182, 212, 0.4); border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">📦</div>
            <div style="font-weight: 700; font-size: 1rem; color: #fff;">Gói Nén Portable (.zip)</div>
            <div style="font-size: 0.8rem; color: #94a3b8; margin: 8px 0 16px 0;">Bao gồm Slide, Dashboard và Hướng dẫn sử dụng</div>
        </div>
        """, unsafe_allow_html=True)
        if zip_bytes:
            st.download_button(
                label="⬇️ Tải Gói Portable (.zip)",
                data=zip_bytes,
                file_name="Slide_Thuyet_Trinh_Project_Cuoi_Khoa_Portable.zip",
                mime="application/zip",
                use_container_width=True
            )
            
    with col2:
        st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">🖥️</div>
            <div style="font-weight: 700; font-size: 1rem; color: #fff;">File Slide Độc Lập (.html)</div>
            <div style="font-size: 0.8rem; color: #94a3b8; margin: 8px 0 16px 0;">Mở trên mọi trình duyệt bằng 1 cú nhấp đúp</div>
        </div>
        """, unsafe_allow_html=True)
        if slide_html:
            st.download_button(
                label="⬇️ Tải Slide HTML (.html)",
                data=slide_html.encode('utf-8'),
                file_name="Slide_Thuyet_Trinh_Project_Cuoi_Khoa.html",
                mime="text/html",
                use_container_width=True
            )
            
    with col3:
        st.markdown("""
        <div style="background: rgba(30, 41, 59, 0.7); border: 1px solid rgba(16, 185, 129, 0.4); border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 10px;">📊</div>
            <div style="font-weight: 700; font-size: 1rem; color: #fff;">File Live Dashboard (.html)</div>
            <div style="font-size: 0.8rem; color: #94a3b8; margin: 8px 0 16px 0;">Executive BI Dashboard với Chart.js tương tác</div>
        </div>
        """, unsafe_allow_html=True)
        if dash_html:
            st.download_button(
                label="⬇️ Tải Dashboard HTML (.html)",
                data=dash_html.encode('utf-8'),
                file_name="Dashboard_Tong_Quan_Doanh_So_NPP.html",
                mime="text/html",
                use_container_width=True
            )

    st.markdown("---")
    st.markdown("### 📊 Tệp Dữ Liệu Excel Thực Hành:")
    
    excel1_bytes, _ = get_binary_content(["Project cuối khóa/File Excel Master Tracking.xlsx"])
    excel2_bytes, _ = get_binary_content(["Project cuối khóa/Doanh số Thực hiện.xlsx"])
    
    c_ex1, c_ex2 = st.columns(2)
    with c_ex1:
        if excel1_bytes:
            st.download_button(
                label="📑 Tải File Excel Master Tracking (7 Sheet SUMIFS)",
                data=excel1_bytes,
                file_name="File_Excel_Master_Tracking.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
    with c_ex2:
        if excel2_bytes:
            st.download_button(
                label="📑 Tải File Doanh số Thực hiện (Daily Snapshot)",
                data=excel2_bytes,
                file_name="Doanh_so_Thuc_hien.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
