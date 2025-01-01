import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

import pandas as pd
import numpy as np

st.subheader("A simple chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)
