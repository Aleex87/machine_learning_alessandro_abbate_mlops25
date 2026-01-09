import streamlit as st

st.markdown("# App front page")

pages = [
    st.Page("pages/home.py", title="Home"),
    st.Page("pages/book_finder.py", title="BookFinder"),
    st.Page("pages/dashboard.py", title="Dashboard"),
]
pg = st.navigation(pages)

pg.run()
