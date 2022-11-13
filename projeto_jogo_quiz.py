# importando bibliotecas
import random as rd
import pandas as pd
cont1=0 # contador
cont2=0 # contador
aux1=int # variavel auxiliar
aux2=int # variavel auxiliar
aux3=str # variavel auxiliar
aux4=str # variavel auxiliar
data = pd.read_csv('/content/drive/MyDrive/portfolio/ciencia_de_dados/trabalho_minigame_futebol/lista-de-times.csv') #importando dados de arquivo .csv
v1=data['Premier League'] # vetor com dados de times
v2=data['La Liga'] # vetor com dados de times
v3=data['Serie A'] # vetor com dados de times
v4=data['Bundesliga'] # vetor com dados de times
v5=data['Ligue 1'] # vetor com dados de times
v6=data['Liga Portugal'] # vetor com dados de times
v0=[v1,v2,v3,v4,v5] # vetor das ligas
va=['inglaterra','espanha','italia','alemanha','frança','portugal'] # vetor com dados dos paises que formam as 6 ligas
vdados_do_jogador=[] # vetor com dados do(a) jogador(a)
vnome=str # variavel com nome do(a) jogador(a)
vpontuacao=0 # varivel com pontuacao do(a) jogador(a)
print('Seja bem vindo(a)!')
print('\n\nJOGO QUIZ\n\n')
print('''Tutorial: \n1) O jogo consiste em acertar o nome do país de origem do time. Nesse caso, cada time pertence a uma das 6 maiores ligas europeias. 
\n2) Em cada questão, você deve digitar o nome do país sem acentuação.
\n3) Você só pode errar 3 vezes.
\n4) Cada acerto somará 1 ponto na pontuação total de jogo\n\n''')
a=str(input('Escreva "sim"  ou "nao" caso queira prosseguir com o jogo: '))
if (a=='sim'):
  vnome=str(input('\nCadastre seu nome de jogador(a): ')) # cadastrando o nome
  vdados_do_jogador.append(vnome)
  print(f'Nome registrado: {vnome}\n')
  print('\n\nAgora, vamos começar o jogo!\n\n') #comeco do jogo
  while (cont1==0):
    aux1=rd.randint(0,(len(v0))-1)
    aux2=rd.randint(0,(len(v0[aux1])-1))
    aux4=v0[aux1][aux2]
    aux3=str(input(f'\nQual é o país de origem de {aux4}? ')).lower()
    if (aux3==va[aux1]):
      vpontuacao=vpontuacao+1
      print(f'\nParabéns!!! Você possui {vpontuacao} ponto(s)!\n')
    elif (aux3!=va[aux1]):
      print('\nInfelizmente, você errou...\n')
      cont2=cont2+1
      if (cont2==4):
        print('Você errou mais de 3 vezes! GAME OVER!')
        cont1=cont1+1
    if (cont2<=3):
      c=str(input('\nDeseja jogar mais uma partida? escreva "sim" ou nao"\n')).lower()
    if (c=='nao'):
      vdados_do_jogador.append(vpontuacao)
      print(f'\n\nResultado:\nJogador(a): {vnome} \nPontuação: {vpontuacao}')
      cont1=cont1+1
else:
  print('\nObrigado pela visita!\n')
