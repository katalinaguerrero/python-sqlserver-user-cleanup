# 🧹 User Cleanup Script (SQL Server)

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Database](https://img.shields.io/badge/SQL%20Server-pyodbc-blue)
![Status](https://img.shields.io/badge/status-active-success)

A Python-based utility that **cleans up users and profiles** in a SQL Server database.
It compares existing users in the database against a reference CSV file and generates a **SQL cleanup script**.
Optionally, you can execute those SQL statements directly from Python.

---

## ⚙️ Features

- Connects to SQL Server using `pyodbc`
- Reads a list of valid users from a CSV file
- Generates an output SQL script with `DELETE` statements
- Optional `--execute` flag to run the cleanup automatically
- Fully parameterized using environment variables
- Clean and modular folder structure

---
