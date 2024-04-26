import streamlit as st
import chromadb



######################
st.snow()
st.image("https://th.bing.com/th/id/OIP.jVzH70O__7IbEGeredhIkwHaDY?w=350&h=159&c=7&r=0&o=5&dpr=1.3&pid=1.7")
st.title('📽️Enhancing Search Engine Relevance for Video Subtitles⌨️')
######################


client = chromadb.PersistentClient(path="C:\\Users\\Shashikanth\\OneDrive\\Documents\\Mentoring\\Data Science\\Internship\\weekly Projects\\Search Engine project")
client.heartbeat()
collection = client.get_collection(name="search")


query_text = st.text_area('Enter your query:')
if st.button('Search'):
    st.snow()
    def similar_title(query_text):
        result = collection.query(
            query_texts=[query_text],
            include=["metadatas","distances","documents"],
            n_results=10
        )
        ids = result['ids'][0]
        metadatas = result['metadatas'][0]
        distances = result['distances'][0]
        documents = result['documents'][0]
        sorted_data = sorted(zip(metadatas, ids,distances,documents), key=lambda x: x[2], reverse=True)
        return sorted_data

    result_data = similar_title(query_text)
    
    st.success('Here are the most relevant subtitle names :')
    for metadata,ids,distance,documents in result_data:
        subtitle_name = metadata['Movie/Episode']
        subtitle_id = ids
        documents = documents
        st.markdown(f"[{subtitle_name}]")
        st.markdown(f"[{documents}]")
