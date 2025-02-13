import streamlit as st


def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Select an option',
        ['Home', 'Movies', 'Genres', 'Actors/Actresses', 'Ratings']
    )

    if menu_option == 'Home':
        st.write('Home')

    if menu_option == 'Movies':
        st.write('Movies List')

    if menu_option == 'Genres':
        st.write('Genres List')

    if menu_option == 'Actors/Actresses':
        st.write('Actors and Actresses List')

    if menu_option == 'Ratings':
        st.write('Ratings List')


if __name__ == '__main__':
    main()
