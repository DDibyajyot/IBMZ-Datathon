import streamlit as st


title = st.container()
about_info = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

dark_mode = """<style>[data-testid="stAppViewContainer"] > .main {{background-color: #121111;}}[data-testid="stHeader"] {{background-color: #121111;}}</style>"""

st.markdown(dark_mode, unsafe_allow_html=True)

with title:
    st.markdown("""<h2 style="text-align: center; font-size: 120px; font-weight: lighter;">Med<span style='color:#EC0164'>Scape</span></h2>""", unsafe_allow_html=True)
    st.markdown("""<p style="text-align: center; color: #FFF; font-size: 32px; font-style: normal; font-weight: lighter;">The solution to medical image registration</p>""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col3:
        pass
    with col2 :
        def redirect_button(url: str, text: str= None, color="#FD504D"):
            st.markdown(
            f"""
            <a href="{url}" target="_self">
                <div style="
                    display: inline-block;
                    font-size: 26px;
                    color: #FFFFFF;
                    background-color: {color};
                    background: rgba(98, 185, 198, 0.79);
                    border-radius: 9px;
                    height: 65px;
                    width: 300px;
                    margin-left: -50px;
                    margin-top: 50px;
                    padding: 0.5em 1em;
                    text-decoration: none;
                    justify-content: center;">
                    {text}
                </div>
            </a>
            """,
            unsafe_allow_html=True
            )
        redirect_button("http://stackoverflow.com","Devpost Submission >")

with about_info:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 150px; border-bottom: solid #EC0164;">About</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Medical image registration refers to the process of aligning two image datasets into one coordinate system for analysis. For our research, we have chosen to focus 
    on images of eye retinas because its avalible datasets made it a good starting point. //Tech about tech-stack a bit
    </p>""", unsafe_allow_html=True)

with dataset:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid #EC0164;">Dataset</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Medical image registration refers to the process of aligning two image datasets into one coordinate system for analysis. For our research, we have chosen to focus 
    on images of eye retinas because its avalible datasets made it a good starting point. //Tech about tech-stack a bit
    </p>""", unsafe_allow_html=True)

with features:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid #EC0164;">Features</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Medical image registration refers to the process of aligning two image datasets into one coordinate system for analysis. For our research, we have chosen to focus 
    on images of eye retinas because its avalible datasets made it a good starting point. //Tech about tech-stack a bit
    </p>""", unsafe_allow_html=True)

with model_training:
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid #EC0164;">Model Training</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Medical image registration refers to the process of aligning two image datasets into one coordinate system for analysis. For our research, we have chosen to focus 
    on images of eye retinas because its avalible datasets made it a good starting point. //Tech about tech-stack a bit
    </p>""", unsafe_allow_html=True)
