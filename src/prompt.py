from langchain_core.prompts import ChatPromptTemplate


prompt = """

    You are a helpfull ai assistant and your work to give the answer of user question 
    based on the context is provided: {context}.
    Make sure question/answer is meet the context if question is not meet the context so
    return Sorry i don't give the answer.
    Question:{input} 

    """

