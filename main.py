from agents.templates import controller_template
from agents.agent import ControlAgent
from constants import CONTROLLER_DATA
#from testing import model_test
import time


def chatbot_intro():
    #print("*" * 100 + "\n" + "*" * 100)  # visual line
    print("Chatbot: Welcome to Chatty. Your AI friend. I will do my best to answer any question you may have. I am well suited to answer questions about AI and Concordia University.\nHow may I assist you?\n")
    #print("Chatbot: Ask a question?(use 'q' to quit)\n")

def main():
    # create model
    controller_llm = ControlAgent("llama3.2", controller_template,CONTROLLER_DATA)
    #model_test(controller_llm) # ~model testing
    chatbot_intro()
    while True:
        #start_time = time.time() # time for testing
        question = input("You: ")
        if question.lower() == "q":
            break
        chatbot_response = controller_llm.answer_question(question)
        print("Chatbot: " + chatbot_response)
        
        #time segment for testing
        #end_time = time.time()
        #elapsed_time = end_time - start_time
        #print(f"Answer response time = {elapsed_time:.4f}")




if __name__ == "__main__":
    main()