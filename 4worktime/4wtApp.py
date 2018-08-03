# -*- coding: utf-8 -*-
import sys

if sys.version_info.major < 3:
    reload(sys)
sys.setdefaultencoding('utf8')

from flaskext.mysql import MySQL
from flask import Flask, render_template, request,redirect, session, flash, url_for


app = Flask(__name__, template_folder="templates/layout_1/LTR/default/full")
app.config['MYSQL_DATABASE_USER'] = 'pegue891_develop'
app.config['MYSQL_DATABASE_PASSWORD'] = 'develop'
app.config['MYSQL_DATABASE_DB'] = 'pegue891_4worktime'
app.config['MYSQL_DATABASE_HOST'] = 'www.visiblenet.com.br'
app.config['MYSQL_DATABASE_PORT'] = 3306


mysql = MySQL()
mysql.init_app(app)



class MainMenu:
    'Classe para exibição do menú lateral esquerdo. A príncipio com dados mockados'

    def __init__(self, nome, icone, titulo, rota, submenu, flsub):
        self.nome = nome
        self.icone = icone
        self.titulo = titulo
        self.rota = rota
        self.submenu = submenu
        self.flsub = flsub

    class SubMenu():
        def __init__(self, nome, icone, rota):
            self.nome = nome
            self.icone = icone
            self.rota = rota


#submenu de configurações
itemSub1 = MainMenu.SubMenu("Cadastro de Empresas", "icon-office", "cadastro-empresa")
itemSub2 = MainMenu.SubMenu("Cadastro de Projetos", "icon-stack2", "cadastro-projeto")
itemSub3 = MainMenu.SubMenu("Cadastro de Equipes", "icon-collaboration", "cadastro-equipes")
itemSub4 = MainMenu.SubMenu("Cadastro de Usuários", "icon-users", "cadastro-usuarios")
itemSub5 = MainMenu.SubMenu("Cadastro de Menus", "icon-menu2", "cadastro-menus")

#submenu configuracões
itemSub6 = MainMenu.SubMenu("Suas Integrações", "", "cadastro-menus")
itemSub7 = MainMenu.SubMenu("Projetos e tarefas permanentes", "", "cadastro-menus")
itemSub8 = MainMenu.SubMenu("Configurações dos usuários", "", "cadastro-menus")
itemSub9 = MainMenu.SubMenu("Configurações do Payoneer", "", "cadastro-menus")
itemSub10 = MainMenu.SubMenu("Cronogramas de trabalho", "", "cadastro-menus")



#subDashboard = None
subSupAdm = [itemSub1, itemSub2, itemSub3, itemSub4, itemSub5]
subConfiguracoes=[itemSub7, itemSub8, itemSub9, itemSub10, itemSub6]

#menu de super admin
itemMenu01 = MainMenu("Dashboard", " icon-graph", "Dashboard", "dashboard", "", 0)
itemMenu02 = MainMenu("Configurações", "icon-cog7", "Configurações do Sistema", "configuracao", subConfiguracoes, 1)
itemMenu03 = MainMenu("Super Admin Configurações", "icon-magic-wand", "Configurações do Sistema", "super-configuracao", subSupAdm, 1)
menu = [itemMenu01, itemMenu02, itemMenu03]

@app.route('/dashboard')
def dashboard():
    return render_template('main-menu.html', titulo='Dashboard', menu=menu, url='dashboard')

@app.route('/')
def index():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchone()
    cursor.close()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"
    #return redirect(url_for('dashboard'))


app.run(debug=True,  host='127.0.0.1', port=80)

