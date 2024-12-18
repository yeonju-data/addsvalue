import streamlit as st
st.caption('Welcome to the Capybara World')

def main_page():
    st.title('MainPage')
    st.header("Hi, My name is **Capybara**")
    st.image("https://files.oaiusercontent.com/file-RXgPugPD8VR8hhWqW6oShS?se=2024-12-18T06%3A48%3A47Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D92f6d024-011a-4226-90c3-96acea6c5180.webp&sig=HDwGlEqxa5vo8891UnCjnzx5r9P5ft7gc3nAhc3AW%2BE%3D")

def page2():
    st.title('Page2')
    st.header('Hi, We are **Capybaras**')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text('Capybara')
        st.image("https://i.kym-cdn.com/photos/images/original/001/551/402/80c.jpeg")
    with col2:
        st.text('capybara baby')
        st.image("https://i.kym-cdn.com/photos/images/original/002/194/548/499.jpg")
    with col3:
        st.text('capybara friends')
        st.image("https://i.kym-cdn.com/photos/images/original/001/101/897/df5.jpg")


def page3():
    st.title('Page3')
    st.header('Yes, We are **VERY CUTE**')
    tab1, tab2, tab3 = st.tabs(['Capybara face','capybara baby','swimming capybara'])
    with tab1:
        st.text('Capybara')
        st.image("https://i.kym-cdn.com/photos/images/original/001/551/402/80c.jpeg")
    with tab2:
        st.text('capybara baby')
        st.image("https://i.kym-cdn.com/photos/images/original/002/194/548/499.jpg")
    with tab3:
        st.text('capybara friends')
        st.image("https://i.kym-cdn.com/photos/images/original/001/101/897/df5.jpg")

#딕셔너리 선언 {'selectbox 항목' : '페이지명'...}
page_names_to_funcs = {'MainPage': main_page, 'Page2':page2, 'Page3' : page3}

#사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())

#해당 페이지 부르기
page_names_to_funcs[selected_page]()


