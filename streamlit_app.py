import streamlit as st

@st.cache_data
def initial_page():
    pass

def main():
    # initial 
    initial_page()
    # render
    header = """
    <h1 style="text-align: center; color: pink; font-weight: bold;">CYPAN test</h1>
    """
    st.markdown(header, unsafe_allow_html=True)
    st.image('images/cypan_Arc_Imaginary_Psychic.png')

# run
main()