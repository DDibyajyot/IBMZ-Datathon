import streamlit as st
from PIL import Image
import os

title = st.container()
about_info = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
test = st.container()

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


with st.form(key='my_form'):
    st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 150px; border-bottom: solid rgba(98, 185, 198, 0.79);">Upload Images</p>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        uploaded_file = st.file_uploader("Upload Retina Image 1 (Source Image): ", type=['jpg'])
    with col2:
        uploaded_file2 = st.file_uploader("Upload Retina Image 2 (Target Image):", type=['jpg'])

    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    if uploaded_file is not None and uploaded_file2 is not None:
        # Upload images to your Flask API
        files = {'image1': uploaded_file, 'image2': uploaded_file2}
        response = requests.post(
            'http://localhost:5000/api/process_images', files=files)

        # Print the response status code and content for debugging
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")

        if response.status_code == 200:
            # Display the aligned image received from the Flask API
            aligned_image_bytes = response.content
            aligned_image = Image.open(BytesIO(aligned_image_bytes))
            st.image(aligned_image, caption='Aligned Image',
                     use_column_width=True)
        else:
            st.error('Image processing failed. Please try again.')


with about_info:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 150px; border-bottom: solid rgba(98, 185, 198, 0.79);">Motivation</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Early identification is critical to slowing the progression of vision loss and preventing blindness, and images taken using multiple modalities and at different 
    time points can be used to measure the progression of the disease. In order to relate information across multiple images, they need to be registered against one 
    another. We present MedScape, a machine learning model trained to register misaligned retina fundus images.
    </p>""", unsafe_allow_html=True)

with dataset:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid rgba(98, 185, 198, 0.79);">Dataset</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Our model was trained on the Fundus Image Registration Dataset (FIRE), consisting of 129 images grouped into 134 registered pairs. 
    </p>""", unsafe_allow_html=True)

with features:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid rgba(98, 185, 198, 0.79);">Model Structure</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    For our model structure, we used the SuperRetina. Images registered against each other by identifying matching keypoints, which are then used to compute the rigid 
    transformation between the image spaces.
    </p>""", unsafe_allow_html=True)

with model_training:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid rgba(98, 185, 198, 0.79);">Results</p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #FFF; font-size: 16px; font-style: normal; font-weight: 100;">
    Our model offers accuracy of up 78.3% with a 54.7 % percision. It's failure rate is 0% with 0.75% inaccurate and 99.27% acceptable data. Below are our data images 
    </p>""", unsafe_allow_html=True)
    image1 = Image.open(os.path.join(r"/Users/soumyakhanna/Documents/ibm/IBMZ-Datathon/frontend/data/image1.png"))
    st.image(image1, caption='Result of a Match')
    image2 = Image.open(os.path.join(r"/Users/soumyakhanna/Documents/ibm/IBMZ-Datathon/frontend/data/image2.png"))
    st.image(image2, caption='Result after Model input')

with test:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""<p style="color: #FFF; font-size: 20px; font-style: normal; font-weight: 100; margin-top: 20px; border-bottom: solid rgba(98, 185, 198, 0.79);">Try Yourself</p>""", unsafe_allow_html=True)
