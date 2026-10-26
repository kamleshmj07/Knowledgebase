import streamlit as st
import pandas as pd
from langchain_openai import ChatOpenAI
from langchain_classic.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from dotenv import load_dotenv

load_dotenv()


def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("CSV FAQ Agent - HELLO Agent!")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Display the DataFrame
        st.write("Data Preview:")
        st.dataframe(df.head())

        # Ask user for a question about the data
        question = st.text_input("Ask me! What do you want to know?")

        llm = launch_llm_agent()
        csv_data = df.to_csv(index=False)  # Convert DataFrame to CSV string without index

        if question:
            chain = create_chain(llm, csv_data, question)
            response = chain.invoke({})
            st.write("Agent Response: ", response)


def launch_llm_agent():
    """
    Function to launch the language model agent.
    """
    # Initialize the ChatOpenAI agent
    agent = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.4,
        max_tokens=1024,
    )

    return agent

def create_chain(llm, csv_data, question) -> LLMChain:
    """
    Function to create a chain for the language model.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                [
                    "The answer must come from the CSV content",
                    "The model should not answer from general world knowledge",
                    "For numeric questions it should compute totals or averages if needed",
                    "The answer should be in clear English, ready to share with a customer",
                    "If it cannot find a matching answer in the CSV data, it should say something like 'Sorry, I donot have that information in the CSV data.'",
                ]
            ),
            HumanMessagePromptTemplate.from_template(
                f"CSV data:\n{csv_data}\n\nQuestion: {question}\n"
            ),
        ]
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

if __name__ == "__main__":
    main()
