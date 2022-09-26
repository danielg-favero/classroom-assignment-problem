# Solução gulosa para o problema de alocação de turmas em salas de aula

## Requisitos para alocação das salas
- a) Em uma mesma sala e horário, não poderá haver duas turmas alocadas
- b) Uma sala não pode receber mais alunos que ela comporta
- c) Utilizar o espaço de forma eficiente, ou seja, evitar alocar aulas de turmas pequenas em salas de maior capacidade

## Função objetivo
Queremos minimizar o custo de alocar uma disciplina $i$ em uma sala $j$ em seu horário $H(i)$ com duração $D(i)$ 

## Representação da solução
Uma solução $s$ é representada por uma matriz com dimensões $|S| \times |D| \times |H|$ onde:
- S: Conjunto de salas no prédio
- D: Conjunto de dias da semana
- H: Conjunto de horários disponíveis

Cada entrada na matriz será o código da disciplina

- http://www.decom.ufop.br/prof/marcone/projects/ppm497-13/Dissertacao-AlanSouzaPrado.pdf

## Heurística construtiva gulosa    

```
Entrada: E = { conjunto de todas as disciplinas para alocar }
Entrada: R = { conjunto de todas as salas }
Saída: Solução S

inicio
S <- {};
C <- E; // Ordenar as disciplinas em forma decrescente pela quantidade de alunos matriculados
g <- 0; // Armazena o valor das inserções na solução inicial

enquanto |C| > 0 faça
    L = C[0] // Seleciona a primeira turma, ou seja, a que possui o maior número de alunos

    D = Sala em R disponível para turma L
    se (D Existe) então
        Alocar L a sala disponível
        Atualizar a solução S <- S u L
        Remover L de C
    fim

    g <- g + valor do custo da inserção de L em S
fim

retorna S e g
```

Por facilidade na resolução, será considerado apenas a alocação de salas em um dia da semana