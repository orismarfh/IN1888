# IN1888 - Formatador de Arquivo de Exchange

Script Python para processar e formatar arquivos de cripto-ativos no layout IN1888 (Receita Federal).

## O que faz

- Converte valores monetários de centavos para reais com vírgula decimal
- Converte quantidades de criptoativos para 10 casas decimais
- Valida e padroniza datas
- Grava o arquivo de saída com CRLF (padrão exigido pela Receita)

## Como usar

Sem dependências externas — requer apenas Python 3.

```bash
git clone https://github.com/orismarfh/IN1888.git
cd IN1888
python3 formatar2_csv.py /caminho/para/2026_03_exchange_bin.txt
```

O arquivo de saída é gerado automaticamente no mesmo diretório do input:
`2026_03_exchange_bin.txt` → `2026_03_ajustedezero.txt`

## Registros processados

| Registro | Campos ajustados |
|---|---|
| `0110` | data, valor (÷100), campo5, quantidade cripto (÷10¹⁰) |
| `0510` | valor (÷100), quantidade cripto (÷10¹⁰) |
| `1000` | valor (÷100) |
| `9999` | valor (÷100) |

## Licença

MIT
