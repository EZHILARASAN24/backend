from openllm import LLMServer, LlamaV3  # Replace with the latest Llama model class

# Initialize LLM server with the latest Llama model
llm_server = LLMServer(model=LlamaV3())

# Run the server
if __name__ == "__main__":
    llm_server.run()
