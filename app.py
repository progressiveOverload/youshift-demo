import streamlit as st

pg = st.navigation(
    [
        st.Page("Introduction.py", title="Introduction", default=True),
        st.Page("Data.py", title="Data"),
        st.Page("Business.py", title="Business"),
    ]
)
pg.run()
