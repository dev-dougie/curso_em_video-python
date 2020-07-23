cidade = str(input('Por favor, digite o nome da sua cidade: ')).upper().strip()
if cidade[:5] == 'SANTO':
    print("Sua cidade começa com 'Santo'")
else:
    print("Sua cidade não começa com 'Santo'")
