# Solução gulosa para o problema de alocação de turmas em salas de aula

## Algoritmo genérico para solução do problema

```
classroom_assign(C = {(Si, Fi) | 0 <= i <= n}):
    ordernar as turmas C em ordem crescente de tempo de início (Si)
    começar com d = 0 salas de aula disponíveis

    para cada turma ci em C:
        se: ci é compatível com uma das d salas abertas, adicione ci a essa sala
        senão: abra a sala d + 1 e adicione ci a essa nova sala
```

Por facilidade na resolução, será considerado apenas a alocação de salas em um dia da semana