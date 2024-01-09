from transformers import TrainingArguments

class Model:
    def __init__(self,model = "LLama2-SA" ,tokenizer = "LLama2-SA"):
        self._model = model
        self._tokenizer = tokenizer
        # self._args = TrainingArguments()
    
    def getModel(self):
        return self.model
        
    def getTokenizer(self):
        return self.tokenizer

    def getEmbeddings(self):
        return self.model.embeddings
