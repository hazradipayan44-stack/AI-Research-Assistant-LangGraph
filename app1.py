import streamlit as st

from graph import graph


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔎",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("AI Research Assistant")

st.write(
    "A web research assistant built with "
    "LangGraph and Tavily."
)


# ==========================================
# USER INPUT
# ==========================================

question = st.text_input(
    "Enter your research question:",
    placeholder="Example: What is Generative AI?"
)


# ==========================================
# RESEARCH BUTTON
# ==========================================

if st.button("Research"):

    if not question.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        with st.spinner(
            "Researching the web..."
        ):

            result = graph.invoke(
                {
                    "question": question,
                    "search_results": {},
                    "final_report": []
                }
            )


        # ==================================
        # SUCCESS MESSAGE
        # ==================================

        st.success(
            "Research completed successfully!"
        )


        # ==================================
        # RESEARCH QUESTION
        # ==================================

        st.subheader("Research Question")

        st.write(question)


        st.divider()


        # ==================================
        # SEARCH RESULTS
        # ==================================

        st.subheader("Web Research")


        sources = result["final_report"]


        if not sources:

            st.info(
                "No search results were found."
            )


        else:

            for index, source in enumerate(
                sources,
                start=1
            ):

                st.markdown(
                    f"### {index}. {source['title']}"
                )


                st.write(
                    source["content"]
                )


                if source["url"]:

                    st.markdown(
                        f"[View Source]({source['url']})"
                    )


                st.divider()
