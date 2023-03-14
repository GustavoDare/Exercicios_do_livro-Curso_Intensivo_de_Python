# Autor: Gustavo Daré
# Data: 24/04/2022

'''
Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário. Crie um dicionário com informações 
    sobre cada cidade e inclua o país em que a cidade está localizada, a população aproximada e um fato sobre essa cidade. As 
    chaves do dicionário de cada cidade devem ser algo como country, population e fact. Apresente o nome de cada cidade e todas 
    as informações que você armazenou sobre ela.
'''

cities = {
    'londres': {'contry': 'inglaterra', 'population': 8.982, 
                'fact': ('Seu centro abriga as sedes imponentes do Parlamento, a famosa torre do relógio do Big Ben e a Abadia de Westminster, '
                    'local de coroação dos monarcas britânicos.')}, 
    'paris': {'contry': 'frança', 'population': 2.161, 
                'fact': ('A cidade é conhecida por monumentos como a Torre Eiffel e a Catedral de Notre-Dame, uma construção gótica do século XII, '
                    'sendo famosa também pela cultura dos cafés e por lojas de estilistas famosos na Rue du Faubourg Saint-Honoré.')}, 
    'são paulo': {'contry': 'brasil', 'population': 12.330, 
                'fact': ('São Paulo, centro financeiro do Brasil, está entre as cidades mais populosas do mundo, com diversas instituições culturais '
                    'e uma rica tradição arquitetônica')}
    }

for nome, infos in cities.items():
    print(f"\n{nome.title()} é uma cidade situada no(a) {infos['contry']} e possui uma população de {infos['population']} milhões. Um  fato "
        f"interessante sobre a cidade é:")
    print(f"    {infos['fact']}")
