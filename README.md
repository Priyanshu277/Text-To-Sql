# Text-to-SQL Converter using Google Gemini Pro

## Overview
This project implements a Text-to-SQL converter using Google Gemini Pro's generative AI capabilities. By leveraging Retrieval-Augmented Generation (RAG), the application transforms natural language queries into SQL statements. The solution aims to simplify database interactions by enabling users to query databases using plain English.

## Features

Natural Language Query Parsing: Converts user-inputted text into SQL queries.

Retrieval-Augmented Generation (RAG): Enhances the model's output by integrating external knowledge from relevant documents.

Google Gemini Pro Integration: Utilizes the Gemini Pro model's capabilities for accurate and efficient text generation.

Interactive Web Interface: Provides an easy-to-use interface for users to enter their queries and view the generated SQL.

## Usage

Enter your natural language query in the text input field.

Click on the "Generate SQL" button.

View the generated SQL query below the input field.

## Example

Input: "Show me all employees who joined after 2020."

Output: SELECT * FROM employees WHERE join_date > '2020-01-01';
