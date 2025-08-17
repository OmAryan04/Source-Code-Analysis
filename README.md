# Source-Code-Analysis
A source code analyzer using Generative AI

# End-to-end-Source-Code-Analysis-Generative-AI

# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n llmapp python=3.10 -y
```

```bash
conda activate llmapp
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Vertex AI project credentials as follows:

```ini
project_id = "xxxxxxxxxxx"
region = "xxxxx"
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- Vertex AI
- gemini-2.5-pro
- ChoromaDB

