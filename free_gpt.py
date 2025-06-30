from flask import Flask, render_template, request
from g4f.client import Client
from g4f.Provider import Yqcloud , OIVSCode , Dynaspark , MetaAI, TeachAnything, DeepInfraChat, PollinationsAI
import markdown
import os
app = Flask(__name__)

def get_result(question,output, selectedProvider, selectedModel):
    client = Client(provider=selectedProvider)
    
    response = client.chat.completions.create(
    model= selectedModel,
    messages=[
              {"role": "user", "content": f"Read this previous chat with an AI assistant. Now Answer the current question keeping in mind the previous chat. \n {output}" + "\n" + f"Th equestion now is : {question}"}],
    
) 
    answer = response.choices[0].message.content
    print (answer)
    return markdown.markdown( answer, extensions=['fenced_code', 'codehilite', 'tables'])
  


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template ("free_gpt.html")

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form['question']
    output = request.form['reoutput']
    selectedProvider = request.form['provider']
    selectedModel = request.form['selectedModel']
    print (selectedProvider)
    print (str(selectedModel))
    return get_result(question,output, selectedProvider, selectedModel)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
