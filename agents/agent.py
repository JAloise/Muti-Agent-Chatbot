from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from templates import general_template,ai_template,concordia_template

class Agent:
  def __init__(self, model_type, prompt_type):
      self.model = OllamaLLM(model=model_type)
      self.prompt = ChatPromptTemplate.from_template(prompt_type)
      self.chain = self.prompt | self.model

  def get_response(self,question):
      return self.chain.invoke({"question": question})



class ControlAgent(Agent):
    def __init__(self, model_type, prompt_type):
        super().__init__(model_type, prompt_type)
        self.general_llm = Agent("llama3.2", general_template)
        self.ai_llm = Agent("llama3.2", ai_template)
        self.concordia_llm = Agent("llama3.2", concordia_template)



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




