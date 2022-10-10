import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from gpxcsv import gpxtolist
import numpy as np
import matplotlib.pyplot as plt
import haversine as hs
import matplotlib as mpl
import tilemapbase



#streamlit run pythonfile.py into terminal streamlit run trackstream.py

uploaded_file = st.file_uploader("Upload a file", type=("gpx"))
#df=gpxtolist(file_bytes)

if uploaded_file is not None:
    df=pd.DataFrame(gpxcsv(uploaded_file))
    
    st.dataframe(df.iloc[: , :20])

#pd.DataFrame
#df = pd.DataFrame(gpxtolist("99_MMM_2022.gpx"))

#st.set_page_config(page_title=df["name"][0],page_icon=":bar_chart:", layout="wide")

























