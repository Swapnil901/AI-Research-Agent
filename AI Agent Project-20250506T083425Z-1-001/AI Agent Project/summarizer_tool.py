import os
from langchain.tools import BaseTool
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain.schema import Document

class SummarizerTool(BaseTool):
    name: str = "WebSummarizer"
    description: str = "Summarizes long web text into bullet-point insights using GPT-4."

    def _run(self, text: str) -> str:
        llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.3,
            max_tokens=700,
            api_key=os.environ["OPENAI_API_KEY"]
        )

        chain = load_summarize_chain(llm, chain_type="stuff")

        # 🔧 FIX: Wrap input string into a Document
        doc = Document(page_content=text)

        response = chain.run([doc])

        # Format response as bullet points if needed
        if "\n" not in response:
            bullets = response.split(". ")
            response = "\n".join(f"- {b.strip()}" for b in bullets if b.strip())

        return f"### 📝 Key Summary Points:\n\n{response.strip()}"

    def _arun(self, text: str):
        raise NotImplementedError("Async not supported.")
