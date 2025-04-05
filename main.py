from agents.templates import controller_template
from agents.agent import ControlAgent
from constants import CONTROLLER_DATA
import time
# models
# ollama run llama3.2 / gemma3
#response = ollama.list()
#print(response)


def main():
    # create model
    controller_llm = ControlAgent("llama3.2", controller_template,CONTROLLER_DATA)
    print("*" * 100 + "\n" + "*" * 100) # visual line
    print("Chatbot: Ask a question?(use q to quit)\n")
    while True:
        start_time = time.time() # time for testing
        question = input("You: ")
        if question.lower() == "q":
            break
        chatbot_response = controller_llm.answer_question(question)
        print("Chatbot: " + chatbot_response)
        #time segment for testing
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Answer response time = {elapsed_time:.4f}")




if __name__ == "__main__":
    main()