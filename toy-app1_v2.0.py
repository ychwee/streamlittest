# Author: Prakash Sukhwal
# version: 3.0
# Nov 2022

import streamlit as st
# other libs
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# -- Set page config
apptitle = 'Solution Implementation'

st.set_page_config(page_title=apptitle, page_icon='random', layout= 'wide', initial_sidebar_state="expanded") 
# layout: "centered" or "wide"
# random icons in the browser tab
# sidebar: "expanded" or "collapsed"
st.title('Toy App-1 on the go..')
st.balloons() 

######################## section-1 ##################
# Let's add a sub-title
# refer: https://docs.streamlit.io/library/cheatsheet

st.write("A **_cool_** toy application")


# Let's load and display a data set
st.subheader('**1. A random dataset**')

df1 = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))

st.dataframe(df1.style.highlight_max(axis=0))
st.write('source: https://docs.streamlit.io/en/stable/api.html#display-data')

########################## section-2 #####################

st.subheader('**2. Boston Housing Data**')
boston = datasets.load_boston()
df2 = pd.DataFrame(boston.data, columns=boston.feature_names)
# st.dataframe(df2)

# let us try some plotting
fig, ax = plt.subplots(figsize=(6, 3))
# sns.boxplot(data=df2)
# st.pyplot(fig)

col1, col2 = st.columns((1,1))
with col2:
	df2
with col1:
	sns.boxplot(data=df2)
	st.pyplot(fig)

########################## section-3 ##########################
# try to load diabetes dataset and plot histogram for age of patients
st.subheader('**3. Diabetes Data**')







