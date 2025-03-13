import streamlit as st
import pandas as pd
import numpy as np

st.title("first cloud")
st.write("simple data frame")
df=pd.DataFrame(np.random.randn(10,2),columns=['col1','col2'])
st.dataframe(df)