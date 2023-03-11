import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')

if st.button('Giải'):
    if (a==0 and b==0): st.write('Phương trình có vô số nghiệm')
    if (a==0 and b!=0): st.write('Phương trình vô nghiệm')                              
    if (a!=0): st.write('Phương trình có 1 nghiệm', -b/a)
