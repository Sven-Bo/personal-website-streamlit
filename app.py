import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Mohsin :wave:")
    st.title("A BI Developer from Australia")
    st.write(
        "I am a BI developer with a passion for data analytics and visualization. I enjoy writing data stories to inform and drive decision-making."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/mohsin-mukhtiar/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            
On my Medium profile, I share insightful articles and tutorials tailored to writers with the following skills:

Python programming: I provide guidance on how to unleash the potential of Python in your everyday writing endeavors.
Power BI: If you're interested in data visualization and analysis, I offer resources and tips for leveraging Power BI in your writing.
SQL: I delve into the world of SQL, equipping you with the skills to effectively manage and analyze data for impactful writing.
Machine Learning: For those seeking to explore advanced data analysis techniques, I provide insights and tutorials on machine learning applications in writing.
If these topics align with your skills and interests, I invite you to follow my profile and enable notifications. Stay updated with the latest content as we embark on a journey of enhancing our writing skills and leveraging technology to elevate our craft together
            """
        )
        st.write("[Medium Profile >](https://medium.com/@rao.mohsin.54)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://github.com/raomohsin54/personal-website-streamlit/blob/New/images/Project1.png")
    with text_column:
        st.subheader("Sales Analysis App (Ask questions from your dataset)")
        st.write(
            """
            Learn how to use Streamlit, Pandasai and ChatGPT3API!
            Answers any questions asked about the dataset using advanced natural language processing
            """
        )
        st.markdown("[Read Article...](https://medium.com/@rao.mohsin.54/pandasai-and-streamlit-ask-your-data-anything-with-natural-language-processing-bfa88b9ed6b)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image("https://github.com/raomohsin54/personal-website-streamlit/blob/New/images/Project2.png")
    with text_column:
        st.subheader("Create Your Own AI-Powered Chatbot with Streamlit and OpenAI’s ChatGPT-3 API")
        st.write(
            """
            Want to create your own AI Powered Chatbot?
            In this article, I'm going to tell you how to Create Your Own AI-Powered Chatbot with Streamlit and OpenAI’s ChatGPT-3 API.
            """
        )
        st.markdown("[Read Article...](https://medium.com/@rao.mohsin.54/create-your-own-ai-powered-chatbot-with-streamlit-and-openais-chatgpt-3-api-42b7c4025795)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/rao.mohsin.54@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
