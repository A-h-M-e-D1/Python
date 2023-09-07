from flask import Flask,render_template

skills_app=Flask(__name__)

My_skills=[("html",80),("Css",50),("python",70)]

@skills_app.route("/")

def homepage():
       return render_template("homepage.html",
                               title="page 1",
                               css_file='css/homepage.css')

@skills_app.route("/about")

def aboutpage():
       return render_template("page2.html",
                               title="page 2")

@skills_app.route("/add")
def addpage():
        return render_template("add.html",
                               title="page 3",
                               css_file='css/add.css')
       
@skills_app.route("/skills")
def Myskills():
       return render_template("skills.html",
                              title="skills",
                              skills=My_skills,
                              css_file='css/skill.css')

if __name__=="__main__":
       skills_app.run()
