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
