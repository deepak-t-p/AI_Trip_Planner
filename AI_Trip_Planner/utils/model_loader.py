




class ConfigLoader:
    def __init__(self):
        pass



class ModelLoader:
    model_provider:Literal["groq","openai"]="groq"
    config: Optional[ConfigLoader] =Field(default=None, exclude=True)


    def model_post_init(self, __context: Any)-> None:
        self.config = ConfigLoader()

    
    class Config:
        arbitrary_types_allowed =True

    def load_llm(self):
        """
        Load and return the LLM model.
         
        """

        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")

        if self.model_provider =="groq":
            print("Loading LLM from Groq ...............")
            groq_api_key= os.getenv("GROQ_API_KEY")
