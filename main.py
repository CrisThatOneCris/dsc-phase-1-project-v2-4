import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import os
import requests
import json

#streamlit home page
st.set_page_config(page_title="streamlit test",
                   page_icon="",
                   layout="wide")

#streamlit first data example
# Read the file
# relative path 
#path = 'Flatiron_Course_Content_ForkedGIT\Phase 1\Phase1_Project\dsc-phase-1-project-v2-4\zippedData'

bom_df = pd.read_csv("zippedData/bom.movie_gross.csv.gz")
st.dataframe(bom_df)

