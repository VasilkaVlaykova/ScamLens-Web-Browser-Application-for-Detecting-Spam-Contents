# ScamLens Introduction

## Project Overview

ScamLens is a machine learning web application developed to help users identify potentially suspicious emails, messages and URLs. The system provides an immediate prediction and probability score, helping users make a more informed decision before interacting with suspicious content. It was designed to be simple, accessible and suitable for users without technical knowledge.

The application does not require registration or payment, and the submitted content is not stored. ScamLens is intended to support users but does not replace official cybersecurity services or professional advice.

## Research Background

The development of ScamLens was supported by research into online scams, social engineering, scammer behaviour and existing machine learning detection techniques. The research investigated how algorithms are used to detect spam emails, malicious URLs and fraudulent messages.

Both the literature-based research and the practical research helped to outline the entire interface and system design. The identified user concerns, research gaps and existing detection methods influenced the system requirements, navigation, safety information, prediction results and probability indicators.

## Development Methodology

An Agile methodology was used during the development of ScamLens. The project was completed through several stages, including research, requirements analysis, system design, data preparation, model training, model evaluation, prototype creation, implementation and testing.

This approach allowed the application and machine learning models to be developed gradually. Testing and feedback were used throughout the process to identify problems and improve the system.

## Technologies and Programming Language

ScamLens was developed using **Python 3.12**. Python was selected because it provides a wide range of libraries for data preparation, machine learning, natural language processing and web application development.

The user interface was created with **Streamlit**, which allowed the trained machine learning models and the visual interface to be integrated into one web application.

## Python Libraries

The main Python libraries used in the project include:

* **Streamlit** – used to develop the web application and its interface.
* **Pandas** – used to load, organise and prepare the datasets.
* **NumPy** – used to support numerical and data-processing operations.
* **Scikit-learn** – used for text vectorisation, model training, data splitting and model evaluation.
* **NLTK** – used for natural language processing tasks, including stop-word removal and lemmatisation.
* **Joblib** – used to save and load the trained models and TF-IDF vectorisers.
* **Plotly** – used to present the prediction probability through visual indicators.
* **Regular Expressions (`re`)** – used to clean text and identify patterns such as URLs, numbers and special characters.
* **Pathlib** – used to manage file and model paths within the project.

## Development Tools

The following tools supported the creation and management of ScamLens:

* **Visual Studio Code** – used to write, organise and test the application code.
* **Jupyter Notebook** – used for dataset exploration, preprocessing, model training and evaluation.
* **Git** – used for version control and tracking project changes.
* **GitHub** – used to store, manage and present the project repository.
* **Figma** – used to prepare and explore the initial interface designs.
* **Streamlit** – used to run and test the final web application.

## Documentation Structure

The remaining documentation presents the functional and non-functional requirements, system design and architecture, and prototype design. These sections explain how the research findings were transformed into the final structure, features and visual interface of ScamLens.


[← Back to the main README](../README.md) | [Next: Functional and Non-functional Requirements →](02_Functional_and_Non_Functional_Requirements.md)