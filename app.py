from flask import Flask, render_template, url_for, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy 
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os
# 
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
thumbFolder = os.path.join('static', 'thumbnails')
app.config['THUMB_FOLDER'] = thumbFolder
fullImageFolder = os.path.join('static', 'fullImage')
app.config['FULL_FOLDER'] = fullImageFolder
patch_request_class(app)
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    content = db.Column(db.String(500), nullable = False)
    picURL = db.Column(db.String(200), nullable = False)
    thumbURL = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<Project %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
    # filePath = os.path.join(app.config['THUMB_FOLDER'], 'pikarmy.png')
    return render_template("homePage.html", url = 'static\\thumbnails\\pikarmy.png')

@app.route('/addProject', methods = ['POST', 'GET'])
def addProj():
    print(request.method)
    if request.method == 'POST':
        f = request.files['thumb']  
        thumbPath = f.filename
        f.save(os.path.join(app.config['THUMB_FOLDER'], f.filename))  
        f = request.files['mainImage']  
        mainPath = f.filename
        f.save(os.path.join(app.config['FULL_FOLDER'], f.filename)) 
        proj = Project(title = request.form['title'], content = request.form['content'], picURL = mainPath, thumbURL = thumbPath)
        try :
            db.session.add(proj)
            db.session.commit()
        except:
            return 'error in upload'
        return render_template('upload.html')
    else:
        return render_template('upload.html')

@app.route('/project/<int:id>')
def singleProject(id):
    project = Project.query.filter_by(id = id).first()
    # print(project.thumbURL)
    # print(os.path.join(app.config['THUMB_FOLDER'], 'pikarmy.png') )
    return render_template('singleProject.html', 
    title = project.title, content = project.content, 
    thumb = url_for('static', filename  = 'thumbnails/' + project.thumbURL) , pic = url_for('static', filename  = 'fullImage/' + project.picURL))

if __name__ == "__main__":
    app.run(debug=True)