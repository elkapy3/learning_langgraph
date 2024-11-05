
from langgraph.graph import Graph
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create a simple prompt template
prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Question: {question}"
)

# Define a basic function for the graph
def generate_response(state):
    question = state["question"]
    response = llm.invoke(prompt.format_messages(question=question))
    return {"response": response.content}

# Create the graph
workflow = Graph()

# Add the node
workflow.add_node("generate", generate_response)

# Define the edges
workflow.set_entry_point("generate")
workflow.set_finish_point("generate")

# Compile the graph
chain = workflow.compile()

# Example usage
if __name__ == "__main__":
    result = chain.invoke({"question": "What is LangGraph?"})
    print(result["response"])