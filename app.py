import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="House Price 🏠", layout="centered")

st.markdown("""
<style>
[data-testid="stSidebar"]{display:none;}
header{visibility:hidden;}
.stApp {
  background: linear-gradient(135deg, #FF6A00 0%, #FF9500 50%, #FFB700 100%)!important;
}
.block-container {max-width:480px!important; padding-top:5vh!important;}
div[data-testid="stVerticalBlockBorderWrapper"]{
  background:white!important;
  border-radius:24px!important;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load("house_model.pkl")
cols = list(model.feature_names_in_)
LOCS = [c.replace('Location_','') for c in cols if 'Location_' in c]

with st.container(border=True):
    st.markdown("## 🏠 House Price Predictor")
    st.write("📍 Mysore & Bangalore • ✨ Live Price")

    loc = st.selectbox("📍 Location", LOCS)
    sqft = st.slider("📐 Size (SqFt)", 500, 5000, 1500)
    st.markdown(f"#### 🏡 {sqft} SqFt in {loc}")

    if st.button("💰 Check Price", use_container_width=True, type="primary"):
        d={c:0 for c in cols}; d['Sqft']=sqft; d[f'Location_{loc}']=1
        raw = model.predict(pd.DataFrame([d])[cols])[0]
        total = raw*100000 if raw < 1000 else raw
        per = total/sqft

        st.divider()
        st.markdown(f"### 💸 Price: ₹ {total:,.0f} 🔥")
        st.markdown(f"**🏷️ ₹ {raw:.1f} Lakhs**")
        st.markdown(f"**📊 ₹ {per:,.0f} / SqFt**")
        st.write(f"✅ {sqft} SqFt • 📍 {loc}")