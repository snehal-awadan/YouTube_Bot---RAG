import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable, RunnablePassthrough, RunnableLambda, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from urllib.parse import urlparse, parse_qs



st.set_page_config(
    page_title= 'YouTube chatbot',
    page_icon='🎥'
)
st.title('Chat with YouTube videos')


# extract the id from given video:

def extract_video_id(url):
    return parse_qs(urlparse(url).query)["v"][0]


# get the transcript:

def get_trnascript(video_id):
    api=YouTubeTranscriptApi()

    transcript = api.fetch(
        video_id,
        languages=['hi']
    )
# create chunks from the transcript:
    text = " ".join(
        chunk.text
        for chunk in transcript
    )
    return text   # return chunks

# session state:
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

# URL input:
youtube_url = st.text_input(
    'Enter YouTube URL'
)

# process video:

if st.button('Process video'):
    try:
        video_id = extract_video_id(youtube_url)
        with st.spinner('Fetching transcript...'):
            text = get_trnascript(video_id)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 200
        )

        docs = splitter.create_documents([text])

        # Embeddings:
        embeddings = HuggingFaceEmbeddings(model_name = 'all-miniLM-L6-v2')

        # Store in faiss vectorestore:
        vector_store = FAISS.from_documents(
            docs,
            embeddings
        )

        # Save in session state:
        st.session_state.vector_store = vector_store

        st.success('Video indexed successfully!')
   
    except Exception as e:
        st.error(
            f'error: {e}'
        )
# Display:
for message in st.session_state.messages:
    with st.chat_message(
        message['role']
    ):
        st.markdown(
            message['content']
        )

# Chat section:
if st.session_state.vector_store is not None:
    question = st.chat_input("Ask about the video...")

    if question:
        st.session_state.messages.append(
            {
            'role':'user',
            'content': question
            }
        )
       
        with st.chat_message('user'):
            st.markdown(question)

        # create retriever:
        if st.session_state.vector_store is not None:
            retriever = st.session_state.vector_store.as_retriever(
                search_type = 'mmr',
                search_kwargs = {'k':4}
        )
        
        retrived_docs = retriever.invoke(question)

        context = '\n'.join(
            doc.page_content
            for doc in retrived_docs
        )

        prompt = PromptTemplate( 

        template =

        '''
            You are a helpful assistant.
            First understand the question clearly, search for the answer from the provided link's transcript's embeddings
            and make it simple to understand the things for the user, if possible give the example to make things easy to understand.
            If the context is insufficient, just say, 'The topic you asked, is not mentioned in the video.
            Do Not hallucinate in amy way.
            if possible give 1/2 related  questions to the user as a recommendation to give the clear idea about topic. 

            {context}
            Question: {question}
            ''',
            input_variables= ['context', 'question']
        )

        # load llama3
        llm = ChatOllama(model = 'llama3')

        final_prompt = prompt.invoke(
            {
                'context':context,
                'question':question
            }
        )

        response = llm.invoke(final_prompt)
        answer = response.content

        with st.chat_message('assistant'):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                'role':'assistant',
                'content':answer                
            }
        )



