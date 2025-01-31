from praisonaiagents import Agent
import sqlite_fix

config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "praison",
            "path": ".praison"
        }
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "deepseek-r1:latest",
            "temperature": 0,
            "max_tokens": 8000,
            "ollama_base_url": "http://localhost:11434",
        },
    },
    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest",
            "ollama_base_url": "http://localhost:11434",
            "embedding_dims": 1536
        },
    },
}

agent = Agent(
    name="Knowledge Agent",
    instructions="You answer questions based on the provided knowledge.",
    knowledge=["book.pdf"], # Indexing
    knowledge_config=config,
    user_id="user1",
    llm="deepseek-r1"
)

agent.start("Give me the name of a character on the text that i gave u (make a list) ") # Retrieval
