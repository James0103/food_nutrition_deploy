import streamlit as st
from module.img import get_image_from_uploader
from module.predict import predict

def main():
    st.title("🥣 AI 음식 검사")
    st.badge("음식 사진을 업로드해서 좋은 음식인지 나쁜 음식인지 알아보세요", color="blue")
    st.divider()

    uploaded_file = st.file_uploader("사진 업로드", type=["jpg", "jpeg", "png"], accept_multiple_files=False, label_visibility="visible", width="stretch")
    if uploaded_file is not None:
        # To read file as bytes:
        img_array = get_image_from_uploader(uploaded_file)
        result = predict(img_array)
        print(result)
        st.write(result)

if __name__ == "__main__":
    st.set_page_config(
        page_title="AI 음식 검사", 
        page_icon="🥣",
        layout="wide"
    )
    main()

    