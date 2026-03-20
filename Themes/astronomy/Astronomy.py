import openai
from ttkthemes import ThemedTk
from tkinter import ttk

window = ThemedTk(theme="kroc")
window.configure(themebg="kroc")
window.geometry("500x500")
window.resizable(False,False)
lbl=ttk.Label(window,text="",)
lbl.pack(pady=50)
pb = ttk.Progressbar(window,length=400)
pb.pack()
a = True



def check(uanswer):
    global score
    global total
    if answer==uanswer:

        score  += 1
        total  += 1
        lblscore.configure(text="bravo, you are the best, you did your luck! Score:" +str(score)+str("/")+str(total))
        pb["value"]+=10
    else:
        total  +=1
        lblscore.configure(text="noooooo you are wrong!Score:"+str(score)+str("/")+str(total))
    if total ==11:
        global btnreset,framebuttons
        framebuttons.destroy()
        pb.destroy()
        lbl.destroy()
        btnreset = ttk.Button(window,command=restart_quiz)
        btnreset.pack()
        btnreset.configure(text="reset")
    generate_question()
def restart_quiz():
    global score, total
    score = 0
    total = 0
    generate_question()





framebuttons = ttk.Frame()
framebuttons.pack()
total = 0
score = 0
yesbtn = ttk.Button(framebuttons, text="YES",command=lambda:check("yes"))
yesbtn.pack(side="left")

nobtn = ttk.Button(framebuttons, text="NO",command=lambda:check("no"))
nobtn.pack()
client = openai.OpenAI(api_key = "API KEY HERE")
lblscore = ttk.Label(window,text="")
lblscore.pack()
def generate_question():
    global answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"Generate a simple yes/no question in English about astronomy suitable for students up to 18 years old with a clear correct answer. "
             "return the format 'Question: <question> | <yes/no> "},
            {"role":"user","content":"Generate a simple yes/no."}
        ]
    )
   #print(response)
    result = response.choices[0].message.content.strip()
    #print(result)
    question_part, answer_part = result.split(" | ")
    #print(question_part)
    #print(answer_part)
    question = question_part.replace("Question: ","").strip().lower()
    answer = answer_part.replace("Answer: ", "").strip().lower()
    print(question)
    print(answer)
    lbl.configure(text=question)
generate_question()
window.mainloop()
