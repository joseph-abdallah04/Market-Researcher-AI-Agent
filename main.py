import ollama

llm = ollama.chat(model="deepseek-r1:32b")

if __name__ == "__main__":
    # Example usage
    response = llm("What is the capital of France?")
    print(response)