
Django- Proway<br/>
+++++++++<br/>
COMANDOS<br/>
+++++++++<br/>

-Instalar:
pip install Django

-Iniciar um novo projeto
djando-admin startproject (nome do projeto) ------------* sem os ( )

-Entrando dentro da pasta destino
cd (nome do projeto)

-Rodando o projeto
python manage.py runserver

-Parar o Servidor
crtl + C

-No terminal irá aparecer o link abaixo, só abrir ou digitar no navegador
http://127.0.0.1:8000/

-Atualizar coisas que foram modificadas no projeto
python manage.py migrate

Avisar para o python para migrar modificações
python manage.py makemigrations
-Criar superusuario - permissão total
python manage.py createsuperuser

-Entrar no painel administrador no navegador(USAR LOGIN E SENHA CRIADOS NO TERMINAL DO VSCODE)
http://127.0.0.1:8000/admin

NESSA SEÇÃO VOCÊ CONSEGUE:
-- ADICIONAR USUARIOS E SUAS PERMISSÕES
-- CRIE GRUPOS E PERMISSÕES
LEMBRANDO QUE PARA USAR NOVOS USARIOS CRIADOS , FAZER LOGOFF DA SESSÃO E ABRIR NOVAMENTE
-- ENCERRAR A SESSÃO
-- ACESSE NOVAMENTE COM UM DOS USUÁRIOS CRIADOS

Criar um app ou COMPONENTE <nesse caso nome do compenente foi 'Produto'>
python manage.py startapp Produto
=======





