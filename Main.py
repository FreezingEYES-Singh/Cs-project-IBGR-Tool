import rembg
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from pathlib import Path
import requests

print("Hello user. If you want to use this project then save this project in a file and open command prompt .Make sure you have installed modules which are imported in this project.then in cmd write cd <location of file where you have saved this project(Main.py)> then press enter. Then type streamlit run Main.py   ")
print("By the way this website is already deployed on internet ask the host if you don't have url")

st.set_page_config(page_title="School Project: IBGR Tool",page_icon="👑",layout="wide")

def load_lottieurl(url):
        r=requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

delete = st.empty()
local_css("style/style.css")

lottie_welcome=load_lottieurl("https://lottie.host/cd4c54da-7578-41a9-9e67-acc6736dae34/4PWV1mbti1.json")
Thank_You=load_lottieurl("https://lottie.host/97efd3ef-4618-41eb-90dd-116e843d888d/23kU4TV98R.json")
lottie4 = load_lottieurl("https://lottie.host/592c3d29-6205-48de-b316-0c15ae3562b0/PCtnM9bTk4.json")

page_by_img = """
<style>
[data-testid="stAppViewContainer"] {    
background-image: url("https://media.tenor.com/EVQVRTOZwaUAAAAd/wallpaper.gif");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stSidebarContent"] {
background-image: url("https://i.pinimg.com/originals/9e/e5/00/9ee500a1c89c9f0b3bc38aa7ac4971c0.gif");
background-size: cover;
background-repeat: no-repeat;
}
</style>
"""

st.markdown(page_by_img, unsafe_allow_html = True)
    
SUPPORTED_FILE_TYPES = ['.png','.jpg','.jpeg']

def main():
    st.markdown("",unsafe_allow_html = True)
    upload_file = st.file_uploader(":orange[Choose the file from below or drop it in this page]",type=SUPPORTED_FILE_TYPES)

    if upload_file is not None:
        remove_button = st.button("Remove Background")
        if remove_button:
            with st.spinner('Removing Background...'):
                image = upload_file.read()
                out_img = rembg.remove(image)

                col1,col2 = st.columns(2)
                with col1:
                    st.image(image,caption="Original Image",use_column_width=True)
                with col2:
                    st.image(out_img,caption="Image with Background Removed",use_column_width=True)
                    st.download_button(label="Download",data=out_img,file_name = "output.png")


selected = option_menu(
    menu_title=None,
    options=["Home","BG Remover","Contact"],
    icons=["house","book","envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "#000000"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "green"},
        }
    )
with st.sidebar:
    st.info('⚜ Here is the info about website.', icon="ℹ️")
    st.title("⏩ :blue[***Creators***]")
    "⭕ :green[**Alok Kumar**]"
    "⭕ :green[**Arnav Padhi**]"
    "⭕ :green[**Harshit Chauhan**]"
    "⭕ :green[**Manthan Singh Rauthan**]"
    "###"
    st.title("⏩ :blue[***About this website***]")
    "⭕ :orange[**It is a project created by a group of students of XI-C of Mayur Public School in Delhi.**]"
    "⭕ :orange[**It is the project of subject CS**]"
    "⭕ :orange[**Here we have created a website which removes the background of the images**]"
    "⭕ :orange[**Click on the BG Remover section in the navigator bar to go to the tool**]"
    "⭕ :orange[**Click on the Contact section in the navigator bar to contact us. We will reply as soon as we can**]"
    "###"
    st.title("⏩ :blue[***How to use the tool***]")
    "⭕ :red[**Firstly, Click on the 'BG Remover' in the navigation bar.**]"
    "⭕ :red[**Then click on the Browse files button and then select your respective file or you can also drag and drop your file in that page.**]"
    "⭕ :red[**Then a button with name 'Remove Background' will appear. Click on the button**]"
    "⭕ :red[**Then after some time the original image and the image with background removed will appear with a button named as 'Download'.**]"
    "⭕ :red[**Click on that button to download the image**]"
    "###"
    st.title("⏩ :blue[***Important***]")
    "⭕ **You can only drop one file at a time**"
    "⭕ **If you are in the middle of the process in removing the photo then if the website is refreshed by the user then the website will be reset to normal and the process will be breaked.**"
    "⭕ **Now enjoy with no more annoying backgrounds** 😎"
    "---"
    "###"
    "###"
    "###"
    


    st_lottie(Thank_You,key="Thanks")

st.info('***How to use?? Go check sidebar.***', icon="ℹ️")
if selected == "Home":
    with st.container():
        st.title(":red[Image Background Remover Tool ( IBGR Tool )] 👋")
        "###"
        "---"
        left_column,right_column = st.columns((2,1))
        with left_column:
            
            st.header(":green[Welcome to Image Background Remover Tool] 🔰")
            "###"
            "🟡:red[***Welcome to our Image background Remover Tool, where we transform your images effortlessly.***]"
            "🟡:red[***Say goodbye to distracting backgrounds and hello to BG remover.***]"
            "🟡:red[***Simplify your creative process.***]"
            "🟡:red[***Let us take care of your content.***]"
            "🟡:red[***Try it now !!***]"
        with right_column:
            st_lottie(lottie_welcome,height=300,key="welcome")
            
            
    
if selected == "BG Remover":
    main()

if selected == "Contact":
    lottie4 = load_lottieurl("https://lottie.host/592c3d29-6205-48de-b316-0c15ae3562b0/PCtnM9bTk4.json")
    with st.container():
            st.write("---")
            st.header(":red[Get in touch with me!!]")
            st.write("##")

            contact_form = """
            <form action="https://formsubmit.co/manthanrauthan1@email.com" method="POST">
                 <input type="hidden" name="_recaptcha" value="false">
                 <input type="text" name="name" placeholder = "Your name" required>
                 <input type="email" name="email" placeholder = "Your email address" required>
                 <textarea name ="message" placeholder = "Your message here" required></textarea>
                 <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st_lottie(lottie4,key="L4")


                
    
    






