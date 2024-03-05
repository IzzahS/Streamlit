
# Streamlit hello world app
import streamlit as st
import pandas as pd
import numpy as np
import datetime

def main():
    st.title('IZZAH  World!')
    st.write('This is a simple hello world app in Streamlit.')
    st.write('To run this app, use the following command:')
    st.code('streamlit run hello_world.py')
    st.sidebar.title ("This is the sidebar")
    st.sidebar.write("my sidebar")
    st.header ("data elements")

    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df)
    st.header("chart elements")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

    st.header("input widgets")
    option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
    st.write('You selected:', option)

    d = st.sidebar.date_input("When's your birthday", datetime.date(2019, 7, 6))
    st.sidebar.write('Your birthday is:', d)

if __name__ == '__main__':
    main()



