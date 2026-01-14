import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()
groq_api_key = os.getenv("API_GROQ_KEY")

llm = ChatGroq(model ="openai/gpt-oss-120b" , api_key = groq_api_key)

# Database Configuration 
DB_USER = "root"
DB_PASSWORD = "your database password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "your database name"

# create connection engine
engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")


#
schema = """

customer(
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    join_date TEXT
)

sales(
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product TEXT,
    amount REAL,
    sale_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)

"""

# Generate SQL
def create_query(question:str)-> str:
    output_parser = JsonOutputParser()
    format_inst = output_parser.get_format_instructions()

    prompt = ChatPromptTemplate.from_template(
        """
        Given the following schema, create a MySQL query that will answer the question.
        Output the query in JSON with key 'query' .

        Schema: {schema}

        Question: {question}

        {format_instructions}
        """
    )

    chain = prompt | llm | output_parser

    try:
        response = chain.invoke({
            "schema": schema,
            "question": question,
            "format_instructions": format_inst
        })

        return response.get("query")
    except Exception as e:
        st.error(f"create_query Error: {e}")
        return None


# Execute SQL
def run_query(query: str):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
            return df
    except Exception as e:
        return pd.DataFrame([[str(e)]], columns=["Database Error"])

# 6. AI Logic: Interpret Results
def interpret_results(question: str, results_df: pd.DataFrame) -> str:
    prompt = ChatPromptTemplate.from_template(
        """Given the following data from a database, provide a concise natural language answer to the user's question.

        Data:
        {results}

        Question:
        {question}"""
    )
    chain = prompt | llm
    
    results_str = results_df.to_dict(orient="records")
    response = chain.invoke({"results": results_str, "question": question})
    
    return response.content if hasattr(response, 'content') else str(response)

# Streamlit UI 
st.set_page_config(page_title="AI SQL Assistant", layout="wide")
st.title("AI-Powered MySQL Assistant")

question = st.text_input("Ask a question about your Sales or Customers:")

if st.button("Run Analysis"):
    if question.strip():
        with st.spinner("Generating SQL..."):
            generated_sql = create_query(question)
        
        if generated_sql:
            st.markdown("Generated SQL")
            st.code(generated_sql, language="sql")

            with st.spinner("Executing Query..."):
                results = run_query(generated_sql)

            st.markdown("Data Results")
            st.dataframe(results, use_container_width=True)

            if "Database Error" not in results.columns:
                with st.spinner("Summarizing..."):
                    answer = interpret_results(question, results)
                st.markdown("AI Insights")
                st.success(answer)
    else:
        st.warning("Please enter a question first.")

