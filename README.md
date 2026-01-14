# 🤖 AI-Powered MySQL Assistant

An AI-driven **Natural Language to SQL (NL2SQL)** application that allows users to interact with a MySQL database using plain English instead of writing SQL queries.

The system uses a **Large Language Model (LLM)** to generate SQL queries, execute them securely, and summarize the results in a conversational format using **Streamlit**.

---

## 🚀 Features

- Ask database questions in natural language
- Automatic SQL query generation using LLM
- Secure MySQL execution using SQLAlchemy
- Results loaded into Pandas DataFrames
- AI-generated insights from raw query output
- Interactive Streamlit web interface

---

## 🧠 Application Workflow

1. **Text → SQL**  
   User enters a question in English.  
   Database schema + question are sent to the LLM to generate a valid MySQL query.

2. **SQL → Data**  
   Generated SQL is executed on MySQL using SQLAlchemy.  
   Results are fetched into a Pandas DataFrame.

3. **Data → Insights**  
   Query results are sent back to the LLM.  
   The model summarizes the data in natural language.

4. **Presentation**  
   Streamlit displays:
   - Generated SQL
   - Query results table
   - AI-generated explanation

---

## 🛠️ Tech Stack

- Python
- MySQL
- SQLAlchemy
- Pandas
- Streamlit
- LangChain
- Groq LLM

👩‍💻 Author

Pooja Dusane
