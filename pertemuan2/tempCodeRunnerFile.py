import streamlit as st
import base64

st.set_page_config(page_title="CV Digital Mahasiswa", page_icon="🎓", layout="centered")

# --- SIDEBAR INPUT ---
st.sidebar.title("⚙️ Pengaturan Profil")
nama = st.sidebar.text_input("Nama Lengkap", "Muhammad Toro Haikal")
nim = st.sidebar.text_input("NIM", "2530801086")
jurusan = st.sidebar.selectbox("Jurusan", ["Informatika"])
deskripsi = st.sidebar.text_area("Deskripsi Singkat", "Mahasiswa Informatika yang memiliki ketertarikan tinggi pada logika pemrograman, analisis teknologi, serta pengelolaan data.")
organisasi = st.sidebar.text_area("Pengalaman Organisasi", "Tidak Ada")

punya_pengalaman = st.sidebar.checkbox("Punya Magang/Sertifikasi?")
detail_exp = st.sidebar.text_area("Detail Magang/Sertifikasi", "Sertifikat Python Basics") if punya_pengalaman else ""

foto = st.sidebar.file_uploader("Foto Profil", type=["jpg", "jpeg", "png"])
foto_b64 = f"data:image/png;base64,{base64.b64encode(foto.read()).decode()}" if foto else ""

st.sidebar.subheader("Kemahiran Skill")
s_py = st.sidebar.slider("Python", 0, 100, 80)
s_web = st.sidebar.slider("Web Dev", 0, 100, 60)
s_db = st.sidebar.slider("Database", 0, 100, 70)

# --- DASHBOARD UTAMA ---
st.title("🎓 Curriculum Vitae Digital")
k_kiri, k_kanan = st.columns([2, 1])

with k_kiri:
    st.header(nama)
    st.subheader(f"{jurusan} | NIM: {nim}")
    st.write(deskripsi)

with k_kanan:
    if foto: st.image(foto, width=180)

st.markdown("---")
st.subheader("👥 Pengalaman Organisasi")
st.write(organisasi)

st.subheader("💼 Sertifikasi / Magang")
st.write(detail_exp if punya_pengalaman and detail_exp else "Tidak ada riwayat magang/sertifikasi.")

st.subheader("🔧 Keahlian Teknis")
st.write("Python"); st.progress(s_py)
st.write("Web Development"); st.progress(s_web)
st.write("Database"); st.progress(s_db)

with st.expander("📬 Hubungi Saya"):
    st.write("📧 Email: sumartoro10@gmail.com | 📞 WA: 089516846503")

# --- FITUR SIMPAN PDF (MURNI BROWSER / STREAMLIT) ---
img_html = f'<img src="{foto_b64}" style="width:90px; height:110px; border-radius:6px;" />' if foto_b64 else ''
exp_text = detail_exp if punya_pengalaman else 'Tidak ada'

html_cv = f"""
<!DOCTYPE html><html><head><style>
    @media print {{ .no-print {{ display: none; }} }}
    body {{ font-family: Arial, sans-serif; font-size: 11pt; color: #1e293b; }}
    .title {{ font-size: 18pt; font-weight: bold; color: #1e3a8a; }}
    .section {{ font-size: 12pt; font-weight: bold; color: #1e3a8a; border-bottom: 2px solid #2563eb; margin-top: 15px; margin-bottom: 6px; text-transform: uppercase; }}
</style></head><body>
    <table width="100%"><tr>
        <td>
            <div class="title">{nama}</div>
            <p><b>{jurusan}</b> | NIM: {nim}<br>Email: sumartoro10@gmail.com | WA: 089516846503</p>
        </td>
        <td align="right" width="100">{img_html}</td>
    </tr></table>
    <div class="section">Deskripsi</div><p>{deskripsi}</p>
    <div class="section">Pengalaman Organisasi</div><p style="white-space: pre-line;">{organisasi}</p>
    <div class="section">Sertifikasi / Magang</div><p>{exp_text}</p>
    <div class="section">Keahlian</div><p>Python: {s_py}% | Web Dev: {s_web}% | Database: {s_db}%</p>
    <button class="no-print" onclick="window.print()" style="margin-top:10px; padding:8px 16px; background:#2563eb; color:white; border:none; border-radius:4px; cursor:pointer;">🖨️ Cetak / Simpan PDF</button>
</body></html>
"""

st.markdown("---")
st.subheader("📄 Simpan CV ke PDF")
st.components.v1.html(html_cv, height=450, scrolling=True)