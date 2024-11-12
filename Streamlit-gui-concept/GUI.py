import streamlit as st

title_container = st.container(border=True)
border = st.container(border=True)


with title_container:
    st.title('Streamlit GUI')
with border:

    col1, col2, col3 = st.columns(3)
    with col1:
        st.title('Function list')
    with col2:
        st.title('Input')
        output_container = st.container(border=True)
        with output_container:
            st.title("Ouput")
    with col3:
        st.title('Graph?')



