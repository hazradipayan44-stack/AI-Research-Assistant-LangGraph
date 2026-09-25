# AI Research Assistant using LangGraph and Tavily

An AI Research Assistant built using **LangGraph** and **Tavily Search**.

This project demonstrates how LangGraph can be used to create a structured workflow where a user submits a research question, Tavily searches the web for relevant information, and the results are processed through a LangGraph workflow.

## Project Overview

The goal of this project is to understand how **LangGraph**, **Tavily**, and **Streamlit** can be combined to build a simple research assistant.

The application allows users to enter a research question and retrieve relevant information from the web using Tavily.

## Workflow

```text
User Question
      ↓
LangGraph
      ↓
Research Node
      ↓
Tavily Web Search
      ↓
Search Results
      ↓
Report Node
      ↓
Final Research Report