# Web Site QxEventos com Flask
Web site desenvolvido com Flask e o framework Bootstrap.

## Preparando Ambiente
Foi utilizado uma imagem `Docker` como ambiente para execução do Web site, caso não tenha o Docker instalado, baixe usando os comandos:

Atualizando lista de repositórios:
```
sudo apt-get update
```
Adicionando a chave GPG do repositório oficial do Docker:
```
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
```
Adicionando o repositório do Docker às fontes do APT:
```
sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
```
Atualizando novamente a lista de repositórios:
```
sudo apt-get update
```
Instalando o Docker:
```
sudo apt-get install -y docker-engine
```
Adicionando o seu usuário ao grupo `docker` permitindo você executar comandos docker sem precisar ser superusuário:
```
sudo usermod -aG docker $(whoami)
```
Depois de instalado, baixe a imagem usada no desenvolvimento deste projeto:
```
docker pull jardelgoncalves/flask
```
Ou
```
docker pull jardelgoncalves/flask-qxeventos
```

Baixe esse projeto pelo próprio website da `github` ou clone com o comando:
```
git clone https://github.com/JardelGoncalves/QxEventos-with-flask-python.git
```

## Executando
Acesse o diretório do projeto clonado ou baixado e descompactado.

EX:
```
cd QxEventos-with-flask-python
```
Lance o contêiner da seguinte forma:
```
docker run --name projeto-flask -it -p 5000:5000 -v ~/QxEventos-with-flask-python/Python/Projeto\ Flask:/home/Projeto\ Flask jardelgoncalves/flask
```
Explicando:

- `--name` Para nomearmos o contêiner que foi lançado
- `-p` Para podemos acessar nosso projeto pelo browser na quela porta na maquina hospedeira
- `-v` Estamos criando um volume no contêiner, no caso o volume na maquina hospedeira está em `~/QxEventos-with-flask-python/Projeto\ Flask` que será montado na maquina hospederia em `/home/Projeto\ Flask`

Ao executarmos o comando acima, será exibido um novo shell referente ao contêiner lançado, acesse o diretório `/home/Projeto\ Flask` 

Execute o comando (caso tenha baixado a imagem `jardelgoncalves/flask-qxeventos` não precisa executar esse passo):
```
pip3 install -r requirements.txt
```
Depois de baixar todas as bibliotecas necessarias, execute a aplicação da seguinte forma:
```
python3 run.py runserver -h 0.0.0.0
```
