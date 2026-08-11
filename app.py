import streamlit as st
import math

# ==========================================
# 0. 図解描画モジュール (SVG)
# ==========================================
def get_schematic_svg(mode):
    style = "<style>.shape{stroke:#2c3e50;stroke-width:3;fill:none;}.assist{stroke:#e74c3c;stroke-width:1.5;stroke-dasharray:4,4;}.point{fill:#e74c3c;}.text{font-family:sans-serif;font-size:14px;fill:#333;}.text-red{font-family:sans-serif;font-size:14px;fill:#e74c3c;font-weight:bold;}.centerline{stroke:#7f8c8d;stroke-width:1;stroke-dasharray:10,5,2,5;}.refline{stroke:#27ae60;stroke-width:1;stroke-dasharray:4,4;}</style>"
    
    if "【外径-1】" in mode:
        return f"""<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6; width: 100%;">
{style}
<line x1="20" y1="180" x2="430" y2="180" class="centerline" />
<text x="360" y="195" class="text" fill="#7f8c8d">中心線 (X=0)</text>
<path d="M 400 140 L 280 60 Q 250 40 190 40 L 40 40" class="shape" />
<line x1="280" y1="60" x2="250" y2="40" class="assist" />
<line x1="190" y1="40" x2="250" y2="40" class="assist" />
<circle cx="250" cy="40" r="5" class="point" />
<text x="260" y="35" class="text-red">仮想交点 (Xv, Zv)</text>
<path d="M 255 70 A 35 35 0 0 0 215 45" stroke="#2980b9" stroke-width="2" fill="none" />
<text x="240" y="85" class="text" fill="#2980b9" font-weight="bold">R (アール)</text>
<line x1="280" y1="60" x2="190" y2="60" class="assist" stroke="#27ae60" />
<path d="M 230 60 A 50 50 0 0 1 250 40" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="195" y="55" class="text" fill="#27ae60" font-weight="bold">θ°</text>
<text x="20" y="25" class="text" fill="#95a5a6">← +Z (奥へ)</text>
<text x="340" y="25" class="text" fill="#95a5a6">-Z (手前へ) →</text>
</svg>"""

    elif "【外径-2】" in mode:
        return f"""<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6; width: 100%;">
{style}
<line x1="20" y1="180" x2="430" y2="180" class="centerline" />
<text x="360" y="195" class="text" fill="#7f8c8d">中心線 (X=0)</text>
<path d="M 350 180 L 350 90 Q 350 50 310 44 L 100 12" class="shape" />
<line x1="350" y1="90" x2="350" y2="50" class="assist" />
<line x1="310" y1="44" x2="350" y2="50" class="assist" />
<circle cx="350" cy="50" r="5" class="point" />
<text x="240" y="45" class="text-red">仮想交点 (Xv, Zv)</text>
<path d="M 345 100 A 40 40 0 0 0 310 65" stroke="#2980b9" stroke-width="2" fill="none" />
<text x="355" y="80" class="text" fill="#2980b9" font-weight="bold">R</text>
<line x1="350" y1="50" x2="150" y2="50" class="refline" />
<path d="M 230 50 A 120 120 0 0 1 245 34" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="210" y="40" class="text" fill="#27ae60" font-weight="bold">θ°</text>
<text x="20" y="25" class="text" fill="#95a5a6">← +Z (奥へ)</text>
<text x="340" y="25" class="text" fill="#95a5a6">-Z (手前へ) →</text>
</svg>"""

    elif "【外径-3】" in mode:
        return f"""<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6; width: 100%;">
{style}
<line x1="20" y1="180" x2="430" y2="180" class="centerline" />
<text x="360" y="195" class="text" fill="#7f8c8d">中心線 (X=0)</text>
<path d="M 400 120 L 290 120 Q 250 120 230 95 L 120 20" class="shape" />
<line x1="290" y1="120" x2="250" y2="120" class="assist" />
<line x1="230" y1="95" x2="250" y2="120" class="assist" />
<circle cx="250" cy="120" r="5" class="point" />
<text x="260" y="135" class="text-red">仮想交点 (Xv, Zv)</text>
<path d="M 270 120 A 25 25 0 0 1 242 103" stroke="#2980b9" stroke-width="2" fill="none" />
<text x="265" y="100" class="text" fill="#2980b9" font-weight="bold">R (谷)</text>
<line x1="250" y1="120" x2="100" y2="120" class="refline" />
<path d="M 170 120 A 80 80 0 0 1 185 75" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="145" y="100" class="text" fill="#27ae60" font-weight="bold">θ°</text>
<text x="20" y="25" class="text" fill="#95a5a6">← +Z (奥へ)</text>
<text x="340" y="25" class="text" fill="#95a5a6">-Z (手前へ) →</text>
</svg>"""

    elif "【外径-4】" in mode:
        return f"""<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6; width: 100%;">
{style}
<line x1="20" y1="180" x2="430" y2="180" class="centerline" />
<text x="360" y="195" class="text" fill="#7f8c8d">中心線 (X=0)</text>
<path d="M 380 40 L 290 105 Q 250 135 210 105 L 120 40" class="shape" />
<line x1="290" y1="105" x2="250" y2="135" class="assist" />
<line x1="210" y1="105" x2="250" y2="135" class="assist" />
<circle cx="250" cy="135" r="5" class="point" />
<text x="180" y="155" class="text-red">交点 (Xv, Zv)</text>
<path d="M 270 120 A 25 25 0 0 1 230 120" stroke="#2980b9" stroke-width="2" fill="none" />
<text x="245" y="105" class="text" fill="#2980b9" font-weight="bold">R</text>
<line x1="150" y1="135" x2="350" y2="135" class="refline" />
<path d="M 300 135 A 50 50 0 0 0 290 105" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="310" y="125" class="text" fill="#27ae60" font-weight="bold">θ1</text>
<path d="M 200 135 A 50 50 0 0 1 210 105" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="175" y="125" class="text" fill="#27ae60" font-weight="bold">θ2</text>
<text x="20" y="25" class="text" fill="#95a5a6">← +Z (奥へ)</text>
<text x="340" y="25" class="text" fill="#95a5a6">-Z (手前へ) →</text>
</svg>"""

    elif "【外径-5】" in mode:
        return f"""<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6; width: 100%;">
{style}
<line x1="20" y1="180" x2="430" y2="180" class="centerline" />
<text x="360" y="195" class="text" fill="#7f8c8d">中心線 (X=0)</text>
<path d="M 400 130 L 290 105 Q 250 95 230 75 L 120 20" class="shape" />
<line x1="290" y1="105" x2="250" y2="95" class="assist" />
<line x1="230" y1="75" x2="250" y2="95" class="assist" />
<circle cx="250" cy="95" r="5" class="point" />
<text x="260" y="110" class="text-red">交点 (Xv, Zv)</text>
<path d="M 270 100 A 30 30 0 0 1 240 85" stroke="#2980b9" stroke-width="2" fill="none" />
<text x="245" y="75" class="text" fill="#2980b9" font-weight="bold">R(谷)</text>
<line x1="100" y1="95" x2="350" y2="95" class="refline" />
<path d="M 310 95 A 60 60 0 0 0 295 103" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="320" y="90" class="text" fill="#27ae60" font-weight="bold">θ1</text>
<path d="M 180 95 A 70 70 0 0 1 190 60" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="155" y="80" class="text" fill="#27ae60" font-weight="bold">θ2</text>
<text x="20" y="25" class="text" fill="#95a5a6">← +Z (奥へ)</text>
<text x="340" y="25" class="text" fill="#95a5a6">-Z (手前へ) →</text>
</svg>"""

    elif "【内径-1】" in mode:
        return f"""<svg viewBox="0 0 450 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px solid #dee2e6; width: 100%;">
{style}
<line x1="20" y1="180" x2="430" y2="180" class="centerline" />
<text x="360" y="195" class="text" fill="#7f8c8d">中心線 (X=0)</text>
<path d="M 400 30 L 300 30 L 190 110 Q 160 132 110 132 L 40 132" class="shape" />
<line x1="300" y1="30" x2="160" y2="132" class="assist" />
<line x1="110" y1="132" x2="160" y2="132" class="assist" />
<circle cx="160" cy="132" r="5" class="point" />
<text x="140" y="152" class="text-red">仮想交点 (Xv, Zv)</text>
<path d="M 145 115 A 35 35 0 0 0 180 100" stroke="#2980b9" stroke-width="2" fill="none" />
<text x="160" y="95" class="text" fill="#2980b9" font-weight="bold">R (アール)</text>
<line x1="190" y1="110" x2="270" y2="110" class="assist" stroke="#27ae60" />
<path d="M 250 110 A 50 50 0 0 0 230 80" stroke="#27ae60" stroke-width="2" fill="none" />
<text x="255" y="95" class="text" fill="#27ae60" font-weight="bold">θ°</text>
<text x="20" y="25" class="text" fill="#95a5a6">← +Z (奥へ)</text>
<text x="340" y="25" class="text" fill="#95a5a6">-Z (手前へ) →</text>
</svg>"""
        
    else:
        return f"""<svg viewBox="0 0 450 80" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8f9fa; border-radius: 8px; border: 1px dashed #ced4da; width: 100%;">
<text x="225" y="45" font-family="sans-serif" font-size="14px" fill="#6c757d" text-anchor="middle">この形状パターンの図解は準備中です</text>
</svg>"""

# ==========================================
# 1. 計算ロジック用モジュール（外径・内径統合）
# ==========================================
def calc_taper_to_arc(x_v_dia, z_v, theta_deg, R, r, z_offset_mode):
    theta_rad = math.radians(theta_deg)
    d = R * math.tan(math.radians(theta_deg / 2.0))
    z_c = z_v + d
    x_c = (x_v_dia / 2.0) - R
    r_prog = R + r
    x_tc_start = x_c + r_prog * math.cos(theta_rad)
    z_tc_start = z_c - r_prog * math.sin(theta_rad)
    x_tc_end = x_c + r_prog
    z_tc_end = z_c
    z_shift = r if "+Z(奥)側にシフト" in z_offset_mode else (-r if "-Z(手前)側にシフト" in z_offset_mode else 0.0)
    return {"start_x_dia": (x_tc_start - r) * 2, "start_z": z_tc_start + z_shift, "end_x_dia": (x_tc_end - r) * 2, "end_z": z_tc_end + z_shift, "prog_r": r_prog, "g_code": "G02 / G03"}

def calc_face_to_arc_to_taper(x_v_dia, z_v, theta_deg, R, r, z_offset_mode):
    theta_rad = math.radians(theta_deg)
    d = R * math.tan(math.radians((90.0 - theta_deg) / 2.0))
    x_c = (x_v_dia / 2.0) - d
    z_c = z_v + R
    r_prog = R + r
    x_tc_start = x_c
    z_tc_start = z_v - r
    x_tc_end = x_c + r_prog * math.cos(theta_rad)
    z_tc_end = z_c - r_prog * math.sin(theta_rad)
    z_shift = r if "+Z(奥)側にシフト" in z_offset_mode else (-r if "-Z(手前)側にシフト" in z_offset_mode else 0.0)
    return {"start_x_dia": (x_tc_start - r) * 2, "start_z": z_tc_start + z_shift, "end_x_dia": (x_tc_end - r) * 2, "end_z": z_tc_end + z_shift, "prog_r": r_prog, "g_code": "G02 / G03"}

def calc_od_to_arc_to_taper(x_v_dia, z_v, theta_deg, R, r, z_offset_mode):
    theta_rad = math.radians(theta_deg)
    d = R * math.tan(theta_rad / 2.0)
    x_c = (x_v_dia / 2.0) + R
    z_c = z_v - d
    r_prog = R - r 
    x_tc_start = x_c - r_prog
    z_tc_start = z_c
    x_tc_end = x_c - r_prog * math.cos(theta_rad)
    z_tc_end = z_c + r_prog * math.sin(theta_rad)
    z_shift = r if "+Z(奥)側にシフト" in z_offset_mode else (-r if "-Z(手前)側にシフト" in z_offset_mode else 0.0)
    return {"start_x_dia": (x_tc_start - r) * 2, "start_z": z_tc_start + z_shift, "end_x_dia": (x_tc_end - r) * 2, "end_z": z_tc_end + z_shift, "prog_r": r_prog, "g_code": "G02 / G03"}

def calc_taper_to_arc_to_taper_v(x_v_dia, z_v, theta1_deg, theta2_deg, R, r, z_offset_mode):
    theta1_rad = math.radians(theta1_deg)
    theta2_rad = math.radians(theta2_deg)
    sum_angles = theta1_rad + theta2_rad
    z_c_relative = R * (math.cos(theta2_rad) - math.cos(theta1_rad)) / math.sin(sum_angles)
    x_c_relative = R * (math.sin(theta1_rad) + math.sin(theta2_rad)) / math.sin(sum_angles)
    z_c = z_v + z_c_relative
    x_c = (x_v_dia / 2.0) + x_c_relative
    r_prog = R - r
    x_tc_start = x_c - r_prog * math.cos(theta1_rad)
    z_tc_start = z_c - r_prog * math.sin(theta1_rad)
    x_tc_end = x_c - r_prog * math.cos(theta2_rad)
    z_tc_end = z_c + r_prog * math.sin(theta2_rad)
    z_shift = r if "+Z(奥)側にシフト" in z_offset_mode else (-r if "-Z(手前)側にシフト" in z_offset_mode else 0.0)
    return {"start_x_dia": (x_tc_start - r) * 2, "start_z": z_tc_start + z_shift, "end_x_dia": (x_tc_end - r) * 2, "end_z": z_tc_end + z_shift, "prog_r": r_prog, "g_code": "G02 / G03"}

def calc_up_to_arc_to_up(x_v_dia, z_v, theta1_deg, theta2_deg, R, r, z_offset_mode):
    theta1_rad = math.radians(theta1_deg)
    theta2_rad = math.radians(theta2_deg)
    alpha = (theta2_rad - theta1_rad) / 2.0
    d = R * math.tan(alpha)
    z_c = z_v - d * math.cos(theta1_rad) - R * math.sin(theta1_rad)
    x_c = (x_v_dia / 2.0) - d * math.sin(theta1_rad) + R * math.cos(theta1_rad)
    r_prog = R - r
    z_tc_start = z_c + r_prog * math.sin(theta1_rad)
    x_tc_start = x_c - r_prog * math.cos(theta1_rad)
    z_tc_end = z_c + r_prog * math.sin(theta2_rad)
    x_tc_end = x_c - r_prog * math.cos(theta2_rad)
    z_shift = r if "+Z(奥)側にシフト" in z_offset_mode else (-r if "-Z(手前)側にシフト" in z_offset_mode else 0.0)
    return {"start_x_dia": (x_tc_start - r) * 2, "start_z": z_tc_start + z_shift, "end_x_dia": (x_tc_end - r) * 2, "end_z": z_tc_end + z_shift, "prog_r": r_prog, "g_code": "G02"}

def calc_id_taper_to_arc(x_v_dia, z_v, theta_deg, R, r, z_offset_mode):
    theta_rad = math.radians(theta_deg)
    d = R * math.tan(math.radians(theta_deg / 2.0))
    z_c = z_v + d
    x_c = (x_v_dia / 2.0) + R
    r_prog = R + r
    x_tc_start = x_c - r_prog * math.cos(theta_rad)
    z_tc_start = z_c - r_prog * math.sin(theta_rad)
    x_tc_end = x_c - r_prog
    z_tc_end = z_c
    z_shift = r if "+Z(奥)側にシフト" in z_offset_mode else (-r if "-Z(手前)側にシフト" in z_offset_mode else 0.0)
    return {"start_x_dia": (x_tc_start + r) * 2, "start_z": z_tc_start + z_shift, "end_x_dia": (x_tc_end + r) * 2, "end_z": z_tc_end + z_shift, "prog_r": r_prog, "g_code": "G03"}


# ==========================================
# 2. 画面表示・UI部分
# ==========================================

st.title("CNC自動旋盤 座標計算アプリ")
st.sidebar.title("機能メニュー")

process_type = st.sidebar.radio("1. 加工種類を選択", ["外径加工", "内径加工"])

if process_type == "外径加工":
    mode = st.sidebar.selectbox(
        "2. 形状パターンを選択", 
        [
            "【外径-1】外径テーパー ⇒ 凸アール", 
            "【外径-2】端面 ⇒ 凸アール ⇒ テーパー",
            "【外径-3】外径ストレート ⇒ 凹アール(谷R) ⇒ テーパー",
            "【外径-4】下りテーパー ⇒ 凹アール ⇒ 上りテーパー (V溝)",
            "【外径-5】上りテーパー ⇒ 凹アール ⇒ 上りテーパー (段差R)"
        ]
    )
else:
    mode = st.sidebar.selectbox(
        "2. 形状パターンを選択", 
        [
            "【内径-1】テーパー(X-方向) ⇒ 凸アール(角R) ⇒ ストレート",
            "【内径-2】（今後追加予定のパターン）"
        ]
    )

st.header(f"{process_type} ➔ {mode}")

# SVG図解の表示 (HTMLのdivタグで囲むことで安全性を強化)
st.markdown(f"<div>{get_schematic_svg(mode)}</div>", unsafe_allow_html=True)
st.write("") 

col1, col2 = st.columns(2)
with col1:
    st.subheader("図面の寸法")
    if "【外径-4】" in mode or "【外径-5】" in mode:
        st.write("※2つの斜面の仮想交点を入力します")
        x_v = st.number_input("仮想交点 X座標 (直径 φ)", value=4.0000, format="%.4f", step=0.01)
        z_v = st.number_input("仮想交点 Z座標", value=3.7300, format="%.4f", step=0.01)
        c_col1, c_col2 = st.columns(2)
        with c_col1:
            theta1 = st.number_input("手前角度 θ1 (°)", value=15.0000, format="%.4f")
        with c_col2:
            theta2 = st.number_input("奥角度 θ2 (°)", value=30.0000, format="%.4f")
        R = st.number_input("谷アール寸法 R", value=1.5000, format="%.4f", step=0.01)
        theta = None
    else:
        x_v = st.number_input("仮想交点 X座標 (直径 φ)", value=15.0000 if "内径" in mode else 6.0000, format="%.4f", step=0.01)
        z_v = st.number_input("仮想交点 Z座標", value=5.0000 if "内径" in mode else 0.0000, format="%.4f", step=0.01)
        theta = st.number_input("テーパー角度 θ (°)", value=15.0000, format="%.4f", step=0.01)
        R = st.number_input("図面アール寸法 R", value=2.0000 if "内径" in mode else 1.2000, format="%.4f", step=0.01)
        theta1 = theta2 = None
    
with col2:
    st.subheader("工具の条件")
    r = st.number_input("使用する工具のノーズR", value=0.4000 if "内径" in mode else 0.2000, format="%.4f", step=0.01)
    st.write("---")
    z_offset_mode = st.radio(
        "プログラム座標のZ位置（仮想刃先）",
        ["① +Z(奥)側にシフト (前挽きなど)", "② ズレなし (刃先R中心)", "③ -Z(手前)側にシフト (裏挽きなど)"],
        index=0
    )

if st.button("座標を計算"):
    if "【外径-1】" in mode:
        res = calc_taper_to_arc(x_v, z_v, theta, R, r, z_offset_mode)
    elif "【外径-2】" in mode:
        res = calc_face_to_arc_to_taper(x_v, z_v, theta, R, r, z_offset_mode)
    elif "【外径-3】" in mode:
        res = calc_od_to_arc_to_taper(x_v, z_v, theta, R, r, z_offset_mode)
    elif "【外径-4】" in mode:
        res = calc_taper_to_arc_to_taper_v(x_v, z_v, theta1, theta2, R, r, z_offset_mode)
    elif "【外径-5】" in mode:
        res = calc_up_to_arc_to_up(x_v, z_v, theta1, theta2, R, r, z_offset_mode)
    elif "【内径-1】" in mode:
        res = calc_id_taper_to_arc(x_v, z_v, theta, R, r, z_offset_mode)
    
    st.success("計算完了！ NCプログラム用座標（直径指令・仮想刃先）")
    st.markdown("##### 1. 円弧の開始点（G01で向かう先）")
    st.code(f"X {res['start_x_dia']:.4f}\nZ {res['start_z']:.4f}")
    st.markdown("##### 2. 円弧の終了点（円弧指令の終点）")
    st.code(f"{res['g_code']} X {res['end_x_dia']:.4f} Z {res['end_z']:.4f} R {res['prog_r']:.4f}")