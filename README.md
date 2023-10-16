# Movie Semantic Search Project

Welcome to the Movie Semantic Search project! This project allows you to search for movies based on your queries and preferences. It leverages semantic search to provide accurate and relevant movie recommendations.

## Features

- Search for movies using natural language queries.
- Filter movie listings by genre.
- Set a minimum rating to refine movie matches based on your preferences.
- Retrieve a specified number of relevant movie results.

## Demo


## Getting Started

Follow these steps to set up and run the Movie Semantic Search project on your local machine:

### Prerequisites

- Python 3.8 or later
- Conda (for managing Python environments)
- Pinecone (Vector Database)
- Streamlit (for the user interface)
- Pandas (for data manipulation)
- Sentence-Transformers (for semantic encoding)

### Installation

1. Clone the project repository from GitHub.

```bash
git https://github.com/francomedin/semantic_search.git
```

2. Install project dependencies.
```bash
pip install -r requirements.txt
```


### Configurations

To use this project for movie search, you need to configure the following:

- See the Notebook file to create the vector database from your dataset
- Pinecone API Key: Obtain your Pinecone API Key from the Pinecone platform. You'll need this key to perform semantic search.


### Usage

Launch the Streamlit app by running the following command:
```bash
streamlit run main.py
```


### Acknowledgments

- Pinecone for providing the semantic search infrastructure.
- Hugging Face Transformers for Sentence-Transformers.