from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import json
from flask_bootstrap import Bootstrap5
from flask import request
app=Flask(__name__)
bootstrap=Bootstrap5(app)
@app.route('/')
def hello_world():
    return "<p>Hello</p>"
DB_URI='mysql+pymysql://root:Sun701231@127.0.0.1:3306/blog'

app.config['SQLALCHEMY_DATABASE_URI']=DB_URI

app.config['SQLALCHEMY_ECHO']=True
app.config['DEBUG'] = True
db=SQLAlchemy(app)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100),nullable=False)
    content =db.Column(db.String(100),nullable=False)
    sectionId= db.Column(db.Integer, nullable=False)
    type= db.Column(db.Integer, nullable=False)
    updateTime =db.Column(db.DateTime(timezone=False),server_default=func.now())
    createTime =db.Column(db.DateTime(timezone=False),server_default=func.now())
    poster= db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Post {self.title}>'
    
@app.route('/index')
def index():
    rows=Post.query.all()
    
   
            
    return render_template("main.html", data=rows)

@app.route('/post',methods=['POST'])
def post():
    if request.method=='POST':
        data = request.get_json()
        title = data['title']
        content =data['content']
        Poster=Post(title=title,content=content,sectionId=1,type=1,poster=1)
        db.session.add(Poster)
        db.session.commit()
    return 'hello'
        

