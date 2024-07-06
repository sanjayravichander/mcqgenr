from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Sanjay",
    author_email="sanjay.1991999@gmail.com",
    install_packages=["openai","langchain","langchain_community","python-dotenv","streamlit","PyPDF2"],
    packages=find_packages()
)