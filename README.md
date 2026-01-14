# 🤖 AI-Powered MySQL Assistant

An **AI-driven Natural Language to SQL (NL2SQL) application** that enables users to interact with a **MySQL database using plain English**, eliminating the need to write complex SQL queries.

This project bridges the gap between **non-technical users and structured databases** by leveraging a **Large Language Model (LLM)** to translate natural language questions into SQL, execute them securely, and present meaningful insights through an interactive **Streamlit** interface.

---

## ✨ Features

- 🗣️ Ask database questions in natural language  
- 🧠 LLM-powered Text → SQL query generation  
- 🗄️ Secure MySQL execution using SQLAlchemy  
- 📊 Automatic data retrieval with Pandas  
- 💬 AI-generated, human-readable insights  
- 🌐 Interactive web interface built with Streamlit  

---

## 🔄 Application Workflow

1. **Natural Language → SQL**  
   The user enters a question in plain English.  
   The database schema and question are sent to the LLM to generate a valid MySQL query.

2. **SQL → Data**  
   The generated SQL query is executed on the MySQL database using SQLAlchemy.  
   The results are fetched into a Pandas DataFrame.

3. **Data → Insights**  
   The query results are passed back to the LLM, which summarizes the data in a concise and conversational manner.

4. **Presentation**  
   The Streamlit interface displays:
   - Generated SQL query  
   - Query results in tabular form  
   - AI-generated explanation and insights  

---

## 🛠️ Tech Stack

- Python  
- MySQL  
- SQLAlchemy  
- Pandas  
- Streamlit  
- LangChain  
- Groq LLM  

---

## 🎯 Use Cases

- Business users querying databases without SQL knowledge  
- AI-assisted data analysis and reporting  
- Educational demonstrations of NL2SQL systems  
- Rapid exploration of structured data  

---


## 👩‍💻 Author

**Pooja Dusane**  
B.Tech CSE (AI & ML)  

---

⭐ If you find this project useful, feel free to star the repository!
