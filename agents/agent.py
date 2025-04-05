from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from agents.templates import general_template,ai_template,concordia_template
from constants import EMPTY_DATA,CONCORDIA_DATA
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from agents.helper_function import emmbeded_pdf_data
import os



'''================== Generic Agent =================='''
class Agent:
  def __init__(self, model_type, prompt_type,data):
      self.model = OllamaLLM(model=model_type)
      self.prompt = ChatPromptTemplate.from_template(prompt_type)
      self.chain = self.prompt | self.model
      self.vector_db = None
      self.retriever = None
      # memory
      #print(data)
      if data:
          #print("start")
          self.initialize_data_retrival(data)

  def initialize_data_retrival(self,data):
      emmbedding = OllamaEmbeddings(model="mxbai-embed-large")
      if not os.path.exists(data[2]) or len(os.listdir(data[2])) == 0:
          # start vectorization
          emmbeded_pdf_data(emmbedding,data[0],data[1],data[2],data[3])
      # intializing agent
      self.vector_db = Chroma(
          embedding_function=emmbedding,
          persist_directory=data[2],
          collection_name=data[0],)
      self.retriever = self.vector_db.as_retriever()

  def get_response(self,question):
      if self.retriever:
        info = self.retriever.invoke(question)
        #print(info)
        return self.chain.invoke({"information":info,"question": question})
      else:
          return self.chain.invoke({"information":[], "question": question})



'''================== Control Agent =================='''
class ControlAgent(Agent):
    def __init__(self, model_type, prompt_type,data):
        super().__init__(model_type, prompt_type,data)
        self.general_llm = Agent("llama3.2", general_template,EMPTY_DATA)
        self.ai_llm = Agent("llama3.2", ai_template,EMPTY_DATA)
        self.concordia_llm = Agent("llama3.2", concordia_template,CONCORDIA_DATA)



    def answer_question(self,question):
        return self.get_agent(question).get_response(question)


    def get_agent(self,question):
        model_check = self.get_response(question)
        print(f"Agent key word:{model_check}")
        if "concordia" in model_check.lower():
            return self.concordia_llm
        elif "ai" in model_check.lower():
            return self.ai_llm
        else:
            return self.general_llm




