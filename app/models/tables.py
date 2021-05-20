from app import db


#classe abaixo é para os usuarios
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    #nfrom app import db


#classe abaixo é para os usuarios
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    #nome do que será usado(id) e o column, é uma coluna de banco de dados, será do tipo, coluna. db."se for inteiro ou string, segue abaixo"
    #e unique significa "unico", por exemplo aq em baixo, é unico o username
    username = db.Column(db.String, Unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, Unique=True)

    #logo abaixo, será feito uma construtor nesta classe, que funciona basicamente como algo dizendo oq vai receber quando essa classe for inicializada(exemplo: username, email, etc)
    # será seguido uma ordem
    #contrutor sempre recebe "self"
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
 
    #função abaixo "repr" é uma forma abreviada de representation, é uma forma bonita de mostrar os registros
    def __repr__(self):
        return "<User %r" % self.username
    

#classe abaixo, é para os "post" algo como os twite's
class Post(db.Model):
    __tablename__ = "posts"

    #Aq em baixo funciona da mesma forma que o anterior, isso que vai msotrar no "poster" que a pessoa fizer
    #basicamente aq em baixo diz que o ID é uma coluna, inteira que se tem como chave primaria, ou então unica
    id = db.Column(db.Integer, primary_key=True)
    #content seria o conteudo do post
    content = db.Column(db.Text)
    #aq em baixo é o id do usuario que esta fazendo referencia, não pode ser um id qualquer, por isso o "ForeignKey", referencia o id unico de outro usuario 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #o codigo abaixo, será feito para "pegar" o id da pessoa do post e mostrar qual seu "username" ou seja, quem publicou
    #serve para não ficar procurando na barra de pesquisa o tempo todo
    #pode utilizar qualquer nome, e isso serve para ir lá e pegar o tudo relacionada do perfil e mostrar

    user = db.relationship('User', foreign_keys=user_id)

    #estou faznedo para mostrar estes conteudo no post
    def __init__(self, content, user_id):
        self.content = content
        self.user = user_id

    def __repr__(self):
        return "<post %r" %self.id

#classe para os "follows" do twiter
class Follow(db.Model):
    __tablename__ = "follow"

    #mesma forma dos anteriores
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower =db.relationship('User', foreign_keys=follower_id)


