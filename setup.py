import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chatgpt",
    version="0.1.0",
    author="prgckwb",
    description="Wrapper for openai package written in python, specialized for ChatGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Prgckwb/chatGPT",
    packages=setuptools.find_packages(),
    install_requires=[
        'openai',
        'tiktoken',
        'rich'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
