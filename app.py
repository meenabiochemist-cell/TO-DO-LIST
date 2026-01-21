from flask import Flask, render_template,request,redirect,url_for
#make an app

app=Flask(__name__)
todolist=[]
todoitem={}
count=1

#specify the route
@app.route("/",methods=["GET","POST"])
def homepage():
 global count
 if request.method=="POST":
    usertask=request.form["Input1"]
    print(usertask) 
    todoitem={"id":count,"task":usertask}
    todolist.append(todoitem)
    count+=1

    print(todolist)
   
 return  render_template("index.html",htmltask=todolist)
@app.route("/delete/<int:taskid>")
def deletepage(taskid):
   print(taskid)
   print(todolist)
   for eachdictionary in todolist:
      if taskid==eachdictionary["id"]:
         ind=todolist.index(eachdictionary)
         todolist.pop(ind)
   return redirect(url_for("homepage"))



if "__main__"==__name__:
    app.run(debug=True)
