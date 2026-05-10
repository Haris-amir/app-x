import streamlit as st
import random
import os

# =========================
# DATA
# =========================

performers = [
    "Riley Reid","Adriana Chechik","Anikka Albrite","Abella Danger",
    "Dani Daniels","August Ames","Mia Malkova","Elsa Jean",
    "Eva Lovia","Madison Ivy","Angela White","Phoenix Marie",
    "Lana Rhoades","Kendra Sunderland","Jessa Rhodes","Emily Willis",
    "Brandi Love","Gianna Dior","Nicole aniston","Peta Jensen",
    "Blake Blossom","Lexi Luna","Lena Paul","Anna Claire Clouds",
    "Savannah Bond","Jennifer White","Kayley Gunner"
]

# =========================
# IMAGE LOADER (LOCAL FILES)
# =========================

IMAGE_FOLDER = "images"

def get_image_path(name):
    filename = name.split()[0].lower() + ".jpg"
    path = os.path.join(IMAGE_FOLDER, filename)

    if os.path.exists(path):
        return path
    return None

# =========================
# SESSION STATE (TRUE RANDOM ON FIRST LOAD)
# =========================

if "selected" not in st.session_state:
    st.session_state.selected = random.sample(performers, 3)

# =========================
# UI
# =========================

st.set_page_config(page_title="Performer App", layout="centered")

st.title("🎲 Performer App")
st.caption("Random picks + shuffle anytime")

# =========================
# SHUFFLE BUTTON (ALWAYS RANDOM)
# =========================

if st.button("🔀 Shuffle 3 new performers"):
    st.session_state.selected = random.sample(performers, 3)

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
        st.warning(f"No image found for {name}")

    st.divider()