jogadores = list()  # lista principal

# ===== Cadastro dos jogadores =====
while True:
    jogador = dict()
    total_gols = list()

    nome = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {nome} jogou? "))

    for c in range(partidas):
        gols = int(input(f"Quantos gols na partida {c+1}? "))
        total_gols.append(gols)

    jogador["nome"] = nome
    jogador["gols"] = total_gols
    jogador["total"] = sum(total_gols)

    jogadores.append(jogador)

    continuar = input("Quer cadastrar outro jogador? [S/N] ").strip().upper()
    if continuar == "N":
        break

# ===== Mostrar resumo =====
print("-=" * 30)
print(f"{'ID':<5}{'Nome':<15}{'Gols':<20}{'Total':<5}")
print("-" * 50)

for i, jogador in enumerate(jogadores):
    print(f"{i:<5}{jogador['nome']:<15}{str(jogador['gols']):<20}{jogador['total']:<5}")

# ===== Sistema de consulta =====
while True:
    print("-=" * 30)
    escolha = int(input("Mostrar detalhes de qual jogador? (999 para sair): "))

    if escolha == 999:
        print("Encerrando sistema de consulta...")
        break

    if escolha >= len(jogadores) or escolha < 0:
        print(f"ERRO! Não existe jogador com ID {escolha}.")
    else:
        jogador = jogadores[escolha]
        print(f"-- DETALHES DO JOGADOR {jogador['nome']}:")
        for i, g in enumerate(jogador["gols"]):
            print(f"   Na partida {i+1} fez {g} gols.")
        print(f"   Total de gols: {jogador['total']}")

#Programa no qual aprimoramos o exercicio 93 a um novo nivel, dessa vez permitindo ao usuario, adicionar novos jogadores, e no final o permitindo visualizar detalhadamente o aproveitamentdo de cada jogador separadamente se assim desejar!
