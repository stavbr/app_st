from random import randint
from pandas import read_csv
import streamlit as st
a = 10
b = 20
print(a + b)
st.write("# abc")
import pandas as pd


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file, sep = ";")
    st.write(dataframe)





title = int(st.text_input('Digite o n de intervalos', '6'))
st.write('Tamanho istograma sera ', title)

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.hist(np.random.normal(20,2,100), bins = title)
fig

plt.show()

