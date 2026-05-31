import streamlit as st
import random
import os

# =========================
# DATA
# =========================

performers = [
    "Aidra Fox","Adriana Chechik","Mac","Lust",
    "Emma Hix","Molly","Mia Malkova","Cali",
    "Eva Lovia","Madison Ivy","Angela White","Phoenix Marie",
    "Lana Rhoades","Kendra Sunderland","Jessa Rhodes","Nikki Benz",
    "Brandi Love","Luna Star","Nicole Aniston","Peta Jensen",
    "Blake Blossom","Lexi Luna","Lena Paul","Azul hermosa",
    "Savannah Bond","Jennifer White","Kayley Gunner","Rachel Starr"
]

# =========================
# IMAGE PATH (FIXED FOR STREAMLIT CLOUD)
# =========================

BASE_DIR = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(BASE_DIR, "images")

def get_image_path(name):
    filename = name.split()[0].lower() + ".jpg"
    path = os.path.join(IMAGE_FOLDER, filename)
    return path if os.path.exists(path) else None

# =========================
# SESSION STATE
# =========================

if "selected" not in st.session_state:
    st.session_state.selected = random.sample(performers, 5)

# =========================
# UI
# =========================

st.set_page_config(page_title="Performers App", layout="centered")

st.title("🎲 Performer Swipe App")
st.caption("Random picks + shuffle anytime")

# =========================
# SHUFFLE BUTTON (ALWAYS RANDOM)
# =========================

if st.button("🔀 Shuffle 5 new performers"):
    st.session_state.selected = random.sample(performers, 5)

selected = st.session_state.selected

# =========================
# DISPLAY
# =========================

for name in selected:
    st.subheader(name)

    img_path = get_image_path(name)

    if img_path:
        st.image(img_path, use_container_width=True)
    else:
        st.error(f"Image not found for: {name}")

    st.divider()
