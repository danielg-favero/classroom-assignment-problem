# Problema de alocação de turmas em salas de aula
## Descrição do problema

Dado um número $m$ de horários para um número $n$ salas em uma universidade, é desejado alocar a maior quantidade de turmas nas salas sem que haja conflito de horários.

## Modelagem do problema

Uma solução para esse problema é por uma representação em matriz $S = (s_{ij})_{m\times n}$, onde $m$ representa o número de horários reservados para a realização das aulas e $n$ o número de salas disponíveis. Em cada célula $s_{ij}$ é colocado o número da turma $t$ alocada ao horário $i$ e sala $j$. Uma célula vazia indica que a sala $j$ está desocupada no horário $i$. [*Marcone, et. al, 2002*]