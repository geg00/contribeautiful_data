import gradio as gr
from github import Github

def greet(name):
    g = Github()
    repo = g.get_repo("huggingface/transformers")
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        print ("Title:",issue.title, "Body:", issue.body , "Labels:", issue.labels)
    return "Hello " + name + "!!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()