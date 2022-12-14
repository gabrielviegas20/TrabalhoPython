from sys import displayhook
from tkinter.tix import DisplayStyle
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#IMPORTANDO BASE DE DADOS
df = pd.read_csv("C:/Users/gabri/OneDrive/Documentos/6Semestre/labprog/python/Trabalho2/TrabalhoPython/Conceito_Enade_2019.csv")
df["Conceito Enade (Faixa)"] = pd.to_numeric(df["Conceito Enade (Faixa)"], errors="coerce")
#FUNÇOES
def Histrograma():
    area = input("Escolha o curso: ")
    plot1 = df[df["Área de Avaliação"] == area]
    print(plot1[["Área de Avaliação", "Conceito Enade (Contínuo)", "Conceito Enade (Faixa)"]])
    plot1 = plot1.groupby("Sigla da IES").head(1)
    #plot1 = plot1.groupby('Sigla da IES')[['Conceito Enade (Contínuo)', 'Conceito Enade (Faixa)']].agg('mean')
    print(plot1[["Sigla da IES", "Conceito Enade (Contínuo)", "Conceito Enade (Faixa)"]])
    fig1 = px.histogram(plot1, x="Sigla da IES", y="Conceito Enade (Contínuo)")
    fig1.show()
    
def StarPlots():
    instituicao1 = input("Escolha a instituição 1 que deseja comparar(colocar sigla): ")
    instituicao2 = input("Escolha a instituição 2 que deseja comparar(colocar sigla): ")
    plot2 = df[df["Sigla da IES"]== instituicao1]
    print(plot2[["Sigla da IES","Área de Avaliação", "Conceito Enade (Contínuo)"]])
    plot3 = df[df["Sigla da IES"]== instituicao2]
    print(plot3[["Sigla da IES","Área de Avaliação", "Conceito Enade (Contínuo)"]])


    fig2 = make_subplots(rows=1, cols=4, specs=[[{'type': 'polar'}] * 4] * 1)
    fig2.add_trace(
        go.Scatterpolar(
            theta=plot2["Área de Avaliação"],
            r=plot2["Conceito Enade (Contínuo)"],
            fill='toself',
            name = instituicao1
        ),
        row=1,
        col=2,
        
    )
    fig2.add_trace(
        go.Scatterpolar(
            theta=plot3["Área de Avaliação"],
            r=plot3["Conceito Enade (Contínuo)"],
            fill='toself',
            name = instituicao2
        ),
        row=1,
        col=4,
        
    )
    fig2.update_layout(height=800, width = 1400)
    fig2.show()

def Medias():
    fig = go.Figure()
    print("A media do conceito geral eh: ")
    media = df["Conceito Enade (Contínuo)"].mean()
    print(round(media, 2))
    print("A variancia do conceito geral eh: ")
    variancia = df["Conceito Enade (Contínuo)"].var()
    print(round(variancia, 2))
    print("A moda do conceito geral(Faixa) eh: ")
    moda = df["Conceito Enade (Faixa)"].mode()
    print(moda)
    print("A mediana do conceito geral eh: ")
    mediana = df["Conceito Enade (Contínuo)"].median()
    print(round(mediana, 2))
    print("O desvio padrao do conceito geral eh: ")
    desvioPadrao = df["Conceito Enade (Contínuo)"].std()
    print(round(desvioPadrao, 2))
    #######################
    fig.add_trace(
        go.Histogram(
            x=df["Conceito Enade (Contínuo)"]
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[media, media, media],
            y=[0, 400],
            name="media"
        )
    )

    
    fig.show()
    
    
#MAIN
print("Escolha que tipo de estatistica quer comparar: ")
print("1-Comparar qual faculdade tem o melhor conceito em um determinado curso: ")
print("2-Comparar conceitos dos cursos entre 2 faculdades ")
print("3-Calcular a media, variancia, mediana, desvio padrao dos conceitos de todas as instituições: ")
escolha = int(input("Sua escolha: "))
if escolha == 1:
    Histrograma()
else:
    if escolha == 2:
        StarPlots()
    else:
        Medias()

