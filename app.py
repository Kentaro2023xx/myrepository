import streamlit as st
import math

st.title('順運動学テスタ')
st.caption('th1, th2, th3 を指定すると手先位置を計算します. ')
st.caption('クリアしたいときはページをリロードしてください.')
st.text('th1-th3を半角数字で入力')
txth1 = st.text_input('th1')
txth2 = st.text_input('th2')
txth3 = st.text_input('th3')

l1,l2,l3 = 0.5,1.0,0.8
submit_btn= st.button('手先位置計算')

if submit_btn:
    th1 = float(txth1)
    th2 = float(txth2)
    th3 = float(txth3)
    x = math.cos(th1)*(l2*math.sin(th2)+l3*math.sin(th2+th3))
    y = math.sin(th1)*(l2*math.sin(th2)+l3*math.sin(th2+th3))
    z =l1+l2*math.cos(th2)+l3*math.cos(th2+th3);   
    st.text(f'X={x}, Y={y}, Z={z}')
    ee = (x-1)**2+(y-1)**2+(z-1)**2
    e = math.sqrt(ee)
    st.text(f'error norm ={e}')
    if e <= 0.001:
        st.text(f'誤差は指定範囲内です．おめでとう！')
    else:
        st.text(f'誤差は指定範囲を越えています. やり直し！')
