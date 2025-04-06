import time


'''================== Testing functions =================='''
questions = ["what is SOEN 423","can you give me a description of the material covered in the course","then what is SOEN 422"
            ,"Compare soen 423 and soen 422","Can you give me more differences between the 2 programs"
            "what are the prerequisites of computer science",
            "How many credits are in the program","how long does it take to finish the program",
            "which classes in the computer science program cover embedded systems","which courses cover programing",
            "what is soen 390","what are its prerequisites","do I need to take the class to finish my computer science degree",
            "how many credits do i need to complete computer science","What is an LLM",
            "Do i need math to use artificial intelligence","does concordia cover ai","why is the sky blue","I want to study in concordia, but I don't know how much a semester costs?"
            ,"Are cars or trains faster?","WHO ARE YOU?","How can I reach a Concordia advisor","Can you compare MCgill and concordia","How much does a semester in Mcgill cost",
             "What are some examples of high paying jobs?","What is the longest bridge?","What happens if i combine bleach and ammonia?",
             "What will happen if i add water to the answer of the previous question","What is the definition of the word 'circle'?",
             "What is the purpose of nitroglycerin?","When was the fall of Czecoslovakia?","what is 1 + 1?","What happens if i divide the answer of the previous question by 2",
             "Name 5 different objects that are green","Are cats better than dogs?","How many people is there on earth?"]




def model_test(model):
    open("test.txt", "w").close()
    print("*" * 100 + "\n" + "*" * 100)  # visual line
    print("="*40+" Start Test " + "=" * 40 + "\n")
    start_time = time.time()  # time for testing
    for question in questions:
        chatbot_response = model.answer_question(question)
        f = open("test.txt", "a")
        f.write(f"{"%"*50}\n{"Input: "+ question}\n{"Output:" +chatbot_response}\n")
        f.close()
    # time segment for testing
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time taken to answer = {elapsed_time:.4f}")
    print("="*40+" End Test " + "=" * 40 + "\n")
    print("*" * 100 + "\n" + "*" * 100)  # visual line
