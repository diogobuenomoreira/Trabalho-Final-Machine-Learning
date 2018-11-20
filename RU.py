
import pandas as pd

# Lendo todos os dados de cardápio e clima

df = pd.read_excel('restaurante_vs_com_ferias_feriado.xlsx')
#clima = pd.read_csv('clima.csv',sep = ';', names = ['data','tMin', 'tMed', 'tMax', 'prec','urMin','urMax','check'], header= None)
clima = pd.read_excel('clima.xlsx')

# Separando linhas de Almoço, Jantar e Café da manhã

lunch = df.loc[(df["Tipo"]=="Almoço")]
dinner = df.loc[(df["Tipo"]=="Jantar")]
coffee = df.loc[(df["Tipo"]=="Café da manhã")]

# Arrumando coluna de datas

coffee["Data"] = coffee["Data"].dt.strftime("%d/%m/%Y")

lunch["Data"] = lunch["Data"].dt.strftime("%d/%m/%Y")

dinner["Data"] = dinner["Data"].dt.strftime("%d/%m/%Y")

#coffee['Data'] = pd.to_datetime(coffee['Data'])
#coffee['Data'] = coffee['Data'].dt.date

#lunch['Data'] = pd.to_datetime(lunch['Data'])
#lunch['Data'] = lunch['Data'].dt.date

#dinner['Data'] = pd.to_datetime(dinner['Data'])
#dinner['Data'] = dinner['Data'].dt.date

# Salvando os arquivos separados

lunch.to_excel('lunch.xlsx')
dinner.to_excel('dinner.xlsx')
coffee.to_excel('coffee.xlsx')


# Lendo os dados salvos

lunch = pd.read_excel('lunch.xlsx')
dinner = pd.read_excel('dinner.xlsx')
coffee = pd.read_excel('coffee.xlsx')

# Acrescentando dados climáticos

dataset_cafe = coffee.merge(clima,left_on="Data",right_on="data")
dataset_cafe.to_excel('cafe.xlsx')

dataset_jantar = dinner.merge(clima,left_on="Data",right_on="data")
dataset_jantar.to_excel('jantar.xlsx')            

dataset_almoco = lunch.merge(clima,left_on="Data",right_on="data")
dataset_almoco.to_excel('almoco.xlsx')

