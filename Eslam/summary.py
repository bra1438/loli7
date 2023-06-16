import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import find_dotenv, load_dotenv

gen_type = [
    "questions and answers",
    "multiple choice questions",
    "explaination as if you are a teacher",
    "bullet points summary",
]

style = [
    "an educational Presentation slides",
    "a video",
    "a pdf",
    "a user question",
    "a text",
]

text = "Computer science and its part in geology"

def answer(gen_type: str, style:str, text:str)-> str:
    try:
        _ = load_dotenv(find_dotenv())  # read local .env file
        key = os.environ["OPENAI_API_KEY"]
    except:
        return None
    else:    
        chat = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo", openai_api_key=key)

        template_string = """"
        You are given material extracted from {style}, genrate a {gen_type} from the text genrated from this material .
        text:{text} 
        """
        prompt_template = ChatPromptTemplate.from_template(template_string)

        message = prompt_template.format_messages(
            gen_type=gen_type, style=style, text=text
        )

        customer_response = chat(message)
        return customer_response.content
    
    
  
print(answer(gen_type=gen_type[-1],style=style[-1],text=text))