import asyncio


async def tarefa(nome, duração):
    print(f"\nExecutando tarefa {nome} por {duração} segundos")
    await asyncio.sleep(duração)
    print(f"\nTarefa {nome} concluída")


# corrotina
async def main():
    await asyncio.gather(
        tarefa("Tarefa 1", 3),
        tarefa("Tarefa 2", 6)
    )

    await tarefa("Tarefa 3", 4)

if __name__ == "__main__":
    asyncio.run(main())
