from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = Ollama(model="llama3")

template = """
You are a resume screening assistant.
Compare the following resume with the job description.
Give a score out of 100 and explain the result in detail.

Resume:
{resume}

Job Description:
{job}

Respond only in the format:
Score: <score>
Explanation: <your detailed explanation>
"""

prompt = PromptTemplate(input_variables=["resume", "job"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

def analyze_resume(resume, job):
    result = chain.run({"resume": resume, "job": job})
    
    try:
        score_match = re.search(r"Score:\s*(\d+)", result)
        explanation_match = re.search(r"Explanation:\s*(.*)", result, re.DOTALL)
        
        score = score_match.group(1) if score_match else "N/A"
        explanation = explanation_match.group(1).strip() if explanation_match else "No explanation found"
    except Exception as e:
        return "N/A", f"⚠️ Couldn't extract score. Response: {result}"
    
    return score, explanation
