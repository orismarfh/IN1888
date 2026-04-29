import sys
from datetime import datetime


def ajustar_registro_0110(linha):
    campos = linha.split('|')
    campos[1] = datetime.strptime(campos[1], '%d%m%Y').strftime('%d%m%Y')

    try:
        campos[4] = '{:,.2f}'.format(float(campos[4]) / 100).replace(',', '').replace('.', ',')
    except ValueError:
        campos[4] = '0,00'

    try:
        campos[5] = '{:,.2f}'.format(float(campos[5])).replace(',', '').replace('.', ',')
    except ValueError:
        campos[5] = '0,00'

    try:
        campos[7] = '{:.10f}'.format(float(campos[7]) / 10000000000).replace('.', ',')
    except ValueError:
        campos[7] = '0,0000000000'

    return '|'.join(campos)


def ajustar_registro_0510(linha):
    campos = linha.split('|')
    try:
        campos[4] = '{:,.2f}'.format(float(campos[4]) / 100).replace(',', '').replace('.', ',')
    except ValueError:
        campos[4] = '0,00'

    try:
        campos[6] = '{:.10f}'.format(float(campos[6]) / 10000000000).replace('.', ',')
    except ValueError:
        campos[6] = '0,0000000000'

    return '|'.join(campos)


def ajustar_registro_1000(linha):
    campos = linha.split('|')
    try:
        campos[8] = '{:,.2f}'.format(float(campos[8]) / 100).replace(',', '').replace('.', ',')
    except ValueError:
        campos[8] = '0,00'
    return '|'.join(campos)


def ajustar_registro_9999(linha):
    campos = linha.split('|')
    try:
        campos[2] = '{:,.2f}'.format(float(campos[2]) / 100).replace(',', '').replace('.', ',')
    except ValueError:
        campos[2] = '0,00'
    return '|'.join(campos)


def processar_arquivo_cripto(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        for linha in infile:
            if linha.strip().startswith('0110'):
                outfile.write(ajustar_registro_0110(linha.strip()) + '\r\n')
            elif linha.strip().startswith('0510'):
                outfile.write(ajustar_registro_0510(linha.strip()) + '\r\n')
            elif linha.strip().startswith('1000'):
                outfile.write(ajustar_registro_1000(linha.strip()) + '\r\n')
            elif linha.strip().startswith('9999'):
                outfile.write(ajustar_registro_9999(linha.strip()) + '\r\n')
            else:
                outfile.write(linha.strip() + '\r\n')


if len(sys.argv) != 2:
    print(f'Uso: python {sys.argv[0]} <arquivo_entrada>')
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace('exchange_bin', 'ajustedezero')
if output_file == input_file:
    output_file = input_file.rsplit('.', 1)[0] + '_ajustedezero.txt'

processar_arquivo_cripto(input_file, output_file)
print(f'Gerado: {output_file}')
