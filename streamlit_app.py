import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('Streamlit Slider and Altair Chart Example')

# create a slider in the sidebar
num_points = st.sidebar.slider('Number of points in random walk', 10, 1000, 100)

# generate a random walk
def random_walk(n):
    return np.cumsum(np.random.randn(n))

# create a dataframe to hold the random walk
df = pd.DataFrame({
    'step': range(num_points),
    'position': random_walk(num_points)
})

# create an Altair chart
chart = alt.Chart(df).mark_line().encode(
    x='step',
    y='position'
)

st.altair_chart(chart, use_container_width=True)
