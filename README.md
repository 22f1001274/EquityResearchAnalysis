# EquityResearchAnalysis
 
 Real life industry use case of equity research analysis:


 ## Problem:
 * Where should we invest? Hire Bunch of Research analyst
 * Which provide researches on how well any company is doing and should we invest based on research.

 # Possible Solution:
 * Copy-pasting on ChatGPT, issue: tedious 
 * we need an aggregate knowledge base
 * chat gpt word limit
 * amount to text corresponds to cost, no need to supply all chunks 
 * only relevant chunks are to be given to model.

 ## How it works?

 1. View Bunch of news article url's in a single go(use web scrapping to create a knowledge base)
 2. Analyse the each article through prompting.
 3. Generate response within the context of news article.

# Technical architecture
1. Documents | Document loader | (Text loader and UnstructuredUrlloader)
2. Splits | splitting into chunks | (CharacterTextSplitter and Recursive Text Splitter)
3. Vector DB | storing as embedding | (FAISS)
4. Retrieval | retrieve relevant chunks for question | (RetrievalQAWithSourceChain)
5. Prompt | Best chunks given to LLM
6. LLM generates answer

# EquityResearchAnalysis
## Overview
EquityResearchAnalysis is a real-life industry use case project designed to assist in the process of equity research analysis by aggregating relevant financial and market information from various sources. The goal is to streamline the research workflow, enabling users to make informed investment decisions based on the latest available data.

## Problem Statement
1. Investment Decision-Making:

    * Where should we invest?
    * This requires hiring a team of research analysts to gather, process, and analyze vast amounts of data on various companies' financial health.

2. Manual Data Processing:

    * Copy-pasting data into ChatGPT or similar models is tedious and inefficient.
    * ChatGPT has word limits and costs associated with larger inputs.
    * There's no need to provide all data to the model—only relevant chunks should be given for analysis to minimize costs and processing time.

## Solution
The project proposes creating a system that:

* Aggregates a knowledge base using web scraping to gather data from multiple news articles and financial reports.
* Analyzes articles using prompting techniques.
* Generates responses that are concise and within the context of the analyzed data.
## How It Works
1. Web Scraping:
    * The system scrapes a batch of news articles or financial reports in one go, creating a knowledge base of relevant content.
2. Document Processing:
    * Each article is processed and analyzed using prompting techniques to extract key insights.
3. Response Generation:
    * The system generates informed responses by contextualizing the information retrieved from the news articles and presenting it in a summarized format.
## Technical Architecture
1. Document Loading:

    * Document Loader: Loads documents from different sources, including URLs.
    * TextLoader & UnstructuredURLLoader: Handles text extraction and loading from unstructured sources.
2. Document Splitting:

    * CharacterTextSplitter & RecursiveTextSplitter: Split documents into smaller, manageable chunks to ensure efficient processing and limit the input size for the model.
3. Vector Database (VectorDB):

    * FAISS: Stores the vector embeddings of document chunks for efficient search and retrieval.
4. Retrieval:

    * RetrievalQAWithSourceChain: Retrieves the most relevant document chunks based on the query and provides the source of the information.
5. Prompting:

    * Selects the best, most relevant document chunks and feeds them to the Large Language Model (LLM) for generating answers.
6. LLM (Large Language Model):

    * Based on the relevant chunks, the LLM generates context-aware answers to queries, ensuring that the response is informed by the latest data from the knowledge base.

## Future Scope
* Improved Querying: Enhance the question-answering capabilities to handle more complex investment scenarios.
* Automated Monitoring: Set up periodic web scraping to keep the knowledge base up-to-date with the latest market developments.
* Scalability: Implement more advanced techniques for scaling the system for larger datasets and more frequent updates.


