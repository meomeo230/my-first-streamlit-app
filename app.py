import streamlit as st

a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')

if st.button('Giải'):
    if (a==0 and b==0): st.success('Phương trình có vô số nghiệm)
    if (a==0 and b!=0): st.success('Phương trình vô nghiệm')                              
    if (a!=0): st.success('Phương trình có 1 nghiệm', -b/a)
