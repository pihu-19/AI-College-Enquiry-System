
import streamlit as st
from graph.graph_builder import process_question
import time


# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI College Enquiry System",
    page_icon="🎓",
    layout="wide"
)


# ---------------- Session Memory ---------------- #

if "history" not in st.session_state:
    st.session_state.history = []


# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background-color:#F4F8FB;
}

.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:white;
}

.sub-title{
    text-align:center;
    font-size:20px;
    color:white;
}

.header{
    background:linear-gradient(90deg,#0B3D91,#1E88E5);
    padding:25px;
    border-radius:15px;
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)



# ---------------- College Photo ---------------- #

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        "assets/college.jpg",
        width=450
    )



# ---------------- Header ---------------- #

st.markdown("""
<div class="header">

<h1 class="main-title">
🎓 AI College Enquiry System
</h1>

<p class="sub-title">
Multi-Agent College Enquiry System using LangGraph
</p>

</div>
""", unsafe_allow_html=True)


st.write("")



# ---------------- Sidebar ---------------- #

st.sidebar.title("AI Agents")

st.sidebar.success("Admission Agent")

st.sidebar.success("Fees Agent")

st.sidebar.success("Exam Agent")

st.sidebar.success("Scholarship Agent")


st.sidebar.markdown("---")


st.sidebar.info("""
Project Features

- Intent Classification

- Multi-Agent Architecture

- Knowledge Base

- LangGraph

- Chat History
""")


st.sidebar.markdown("---")


st.sidebar.info("""
Developed By

PIHU

AI Internship Project
""")



# ---------------- College Information ---------------- #

st.markdown("## About Our College")


c1,c2,c3 = st.columns(3)


with c1:
    st.info("""
Departments

• Computer Science

• Electronics

• Mechanical

• Civil
""")


with c2:
    st.success("""
Location

Dumka, Jharkhand

Near Govt. Polytechnic,
Shivpahar Dumka

Established: 2013
""")


with c3:
    st.warning("""
Contact

Email:
coordinatortigjh@gmail.com

Phone:
+91-9007600888
""")



# ---------------- AI Agents ---------------- #

st.markdown("## Available AI Agents")


a1,a2 = st.columns(2)


with a1:
    st.info("Admission Agent")

    st.success("Fees Agent")


with a2:
    st.warning("Exam Agent")

    st.error("Scholarship Agent")



# ---------------- User Question ---------------- #

question = st.text_input(
    "Ask your question",
    placeholder="Example: What is the admission process?"
)



# ---------------- Ask Button ---------------- #

if st.button("Ask AI"):

    if question.strip()=="":
        st.warning("Please enter a question.")

    else:

        with st.spinner("AI is thinking..."):

            start=time.time()

            time.sleep(1)

            answer = process_question(question)

            end=time.time()


        st.session_state.history.append(
            {
                "question": question,
                "answer": answer
            }
        )


        st.markdown("## AI Response")

        st.success(answer)

        st.info(
            f"Response Time: {round(end-start,2)} seconds"
        )



# ---------------- Chat History ---------------- #

if st.session_state.history:

    col1, col2 = st.columns([5,1])

    with col1:
        st.markdown("## Previous Questions")


    with col2:

        if st.button("Clear"):

            st.session_state.history = []

            st.rerun()



    for chat in reversed(st.session_state.history):

        st.write(
            "Question:",
            chat["question"]
        )


        st.write(
            "Answer:",
            chat["answer"]
        )


        st.divider()



# ---------------- System Status ---------------- #

st.markdown("## System Status")


st.success("AI Agents Active")

st.success("LangGraph Connected")

st.success("Knowledge Base Ready")



# ---------------- Footer ---------------- #

st.markdown("---")


st.markdown(
"""
<div class="footer">

Developed for AI Internship Project by PIHU

<br>

Multi-Agent College Enquiry System using LangGraph

</div>
""",
unsafe_allow_html=True
)