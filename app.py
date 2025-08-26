import streamlit as st

def main():
    cont1 = st.container(border=True, width='stretch', height=350)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit Row 대안들", 
        page_icon="📐",
        layout="wide"
    )
    
    main()

    