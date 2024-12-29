import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
from PIL import Image


st.set_page_config(page_title='Home' ,layout="wide",page_icon='👧🏻')



# -----------------  chatbot  ----------------- #
# Set up the OpenAI key

#openai_api_key = st.sidebar.text_input('Enter your OpenAI API Key and hit Enter', type="password")
#openai.api_key = (openai_api_key)

# load the file
#documents = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()

#pronoun = info["Pronoun"]
#name = info["Name"]
#def ask_bot(input_text):
    # define LLM
 #   llm = ChatOpenAI(
  #      model_name="gpt-3.5-turbo",
   #     temperature=0,
    #    openai_api_key=openai.api_key,
    #)
    #llm_predictor =llm
    #service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    
    # load index
    #index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)    
    
    # query LlamaIndex and GPT-3.5 for the AI's response
    #PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting {name} in her job search by providing recruiters with relevant and concise information. 
    #If you do not know the answer, politely admit it and let recruiters know how to contact {name} to get more information directly from {pronoun}. 
    #Don't put "Buddy" or a breakline in the front of your answer.
    #Human: {input}
    #"""
    
    #output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
    #print(f"output: {output}")
    #return output.response

# get the user's input by calling the get_text function
#def get_text():
 #   input_text = st.text_input("After providing OpenAI API Key on the sidebar, you can send your questions and hit Enter to know more about me from my AI agent, Buddy!", key="input")
  #  return input_text

#st.markdown("Chat With Me Now")
#user_input = get_text()

#if user_input:
  #text = st.text_area('Enter your questions')
 # if not openai_api_key.startswith('sk-'):
  #  st.warning('⚠️Please enter your OpenAI API key on the sidebar.', icon='⚠')
  #if openai_api_key.startswith('sk-'):
   # st.info(ask_bot(user_input))

# -----------------  loading assets  ----------------- #

    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")



# ----------------- info ----------------- #

with st.container():
 

    full_name = info['Full_Name']

    st.title(f"Hi, I'm {full_name}👋", info["Intro"])
    st.write("")
    st.write(info['About'])
    
    

    #st_lottie(lottie_gif, height=380, key="data")
        
st.divider()

# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)

st.divider()
# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    with col4:
        st_lottie(js_lottie,height=50,width=50, key="js", speed=1)

    

# -----------------  contact  ----------------- #


