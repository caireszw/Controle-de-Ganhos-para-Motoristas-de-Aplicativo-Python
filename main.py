def lin():
    print('-'*30)

temp = dict()
modelo = dict()
corridas = list()
mediaconsumo = None
valorcombustivel = None

print('SISTEMA CONTROLE DE GANHOS!')
lin()
while True:
    print('1 - Inserir resultados')
    print('2 - Qual o modelo do carro')
    print('3 - Media de consumo')
    print('4 - Mostrar os resultados')
    print('5 - Mostrar todas as corridas')
    print('6 - Encerrar Programa')
    lin()
    resp = int(input('Digite a opção desejada'))
    if resp == 1:
        temp['Data'] = int(input('Data da corrida:'))
        temp ['Valor'] = float(input('Digite o valor da corrida').replace(',','.'))
        temp['Km'] = float(input('Digite a kilometragem de viagem').replace(',','.'))
        corridas.append(temp.copy())
        temp.clear()
    elif resp == 2:
        carro = str(input('Digite o modelo do carro:'))
        
    elif resp == 3:
        mediaconsumo = float(input('Digite a media de consumo do veiculo').replace(',','.'))
        valorcombustivel = float(input('Digite o valor atual do combustivel:').replace(',','.'))
        
    elif resp == 4:
        if mediaconsumo is None:
            print('Preencha a média de consumo (opção 3)')
        elif valorcombustivel is None:
            print('Preencha o valor do combustível (opção 3)')
        else:
            totalganho = 0
            for v in corridas:
                totalganho += v['Valor']
        

            totalkm = 0 
            for v in corridas:
                totalkm += v['Km'] 
        

            totallitros = totalkm / mediaconsumo 
            totalgasto = totallitros * valorcombustivel  

            lin()
            print('RELATORIO')
            print(f'O valor total ganho com corridas foi R${totalganho:.2f}')
            print(f'O valor total rodado foi {totalkm:.2f} quilometros')
            lucro = totalganho - totalgasto
            print(f'O lucro final foi de {lucro:.2f}')
            lin()
    elif resp == 5:
        if len(corridas) == 0:
            print('Nenhuma corrida cadastrada!')
        else:
            for v in corridas:
                print(f'Dia {v["Data"]} | Valor {v["Valor"]} | Km {v["Km"]}')

    elif resp == 6:
        print('FIM DO PROGRAMA OBRIGADO!')
        break


        


