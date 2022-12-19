# Problema de alocação de turmas em salas de aula

## Trabalho desenvolvido por:
Daniel Gustavo Favero <br>
RA: 2157128 <br>
Universidade Tecnológica Federal do Paraná - Câmpus Pato Branco

## Descrição do problema

Dado um número $m$ de horários para um número $n$ salas em uma universidade, é desejado alocar a maior quantidade de turmas nas salas sem que haja conflito de horários. <br>

Uma solução para esse problema é por uma representação em matriz $S = (s_{ij})_{m\times n}$, onde $m$ representa o número de horários reservados para a realização das aulas e $n$ o número de salas disponíveis. Em cada célula $s_{ij}$ é colocado o número da turma $t$ alocada ao horário $i$ e sala $j$. Uma célula vazia indica que a sala $j$ está desocupada no horário $i$. [*Marcone, et. al, 2002*] <br>

# Solução para o problema

Uma solução apenas é válida se ela atender os requisitos essenciais, para melhoria da solução, ela também deve atender os requisitos não essenciais

## Representação da solução
Uma solução $s$ é representada por uma matriz com dimensões $|S| \times |D| \times |H|$ onde:
- S: Conjunto de salas no prédio
- D: Conjunto de dias da semana
- H: Conjunto de horários disponíveis

Cada entrada na matriz conterá os dados disciplina alocada

## Requisitos para alocação das salas
- a) Em uma mesma sala e horário, não poderá haver duas turmas alocadas - **ESSENCIAL**
- b) Uma sala não pode receber mais alunos que ela comporta - **ESSENCIAL**
- c) Algumas salas já estão previamente reservadas, é preciso respeitar esse horário - **ESSENCIAL**
- d) Evitar alocar aulas de turmas pequenas em salas de maior capacidade - **NÃO ESSENCIAL**
- e) Sempre que possível, alocar a uma mesma sala alunos de um mesmo período e curso - **NÃO ESSENCIAL**
- f) Se possível, cada uma das salas deve ser deixada vazia em pelo menos um horário ao longo do dia, de forma a possibilitar sua limpeza - **NÃO ESSENCIAL**
- g) Se possível, utilizar o menor número de salas possível - **NÃO ESSENCIAL**

## Função objetivo
Nossa função objetivo deve maximizar a quantidade de vezes que os requisitos não essenciais são atendidos. Ou seja:

$$f(x) = \sum g_i(x)$$

Onde $g_i(x)$ é a quantidade de vezes que o requisito não essencial é encontrado na solução<br>

A solução do problema se dará em duas etapas:
- **Construção inicial gulosa**, para atender os requisitos essenciais
- **Construção de refinamento de busca local**, para melhorar o atendimento dos requisitos não funcionais

## Heurística de construção gulosa    

```
Entrada: E = { conjunto de todas as disciplinas para alocar }
Entrada: R = { conjunto de todas as salas }
Saída: Solução S

inicio
S = {};
C = E; // Ordenar as disciplinas em forma decrescente pela quantidade de alunos matriculados

enquanto |C| > 0 faça
    L = C[0] // Seleciona a primeira turma, ou seja, a que possui o maior número de alunos

    D = Sala em R disponível para turma L
    se (D Existe) então
        Alocar L a sala disponível
        Atualizar a solução S <- S u L
        Remover L de C
    fim
fim

retorna S
```

Os resultados obtidos da construção gulosa se encontram em `results/greedy_results.txt`

## Heurística de refinamento de busca local
```
Entrada: S = { Solução inicial gerada }
Saída: S' = { Solução melhorada }

inicio
    C = S
    custo_final = 0

    custo_inical = calcula_custo(C) // Quantificação das restrições não essenciais para solução inicial
    enquanto custo_final <= custo_inicial
        C' = troca_turmas(C) // Realizar movimentação da solução para melhorar a solução corrente
        custo_final = calcula_custo(C') // Quantificação das restrições não essenciais para solução nova
        C = C'

    retorna C
fim
```


> troca_turmas(C) troca as disciplinas de lugar aleatoriamente para verificar se a quantidade de requisitos não essenciais é atendida

> calcula_custo(C) itera sobre a solução e verifica a quantidade de vezes que os requisitos não essenciais são atendidos


Os resultados obtidos no refinamento se encontram em `results/local_search_results.txt`

## Metaheurística de *Simulated Annealing*
```
Entrada: S0 = { Solução corrente }
Entrada: T0 = { Temperatura inicial }
Entrada: α = { Taxa de resfriamento }
Entrada: SAmax = { Número máximo de iterações }
Saída: S*

inicio
    S = S0
    S' = S
    T = T0
    IterT = 0

    enquanto (T > 0) faça
        enquanto (IterT < SAmax) faça
            IterT += 1
            Gerar novo vizinho S' ∈ N(S)
            ∆ = f(S’) – f(S)

            se (∆ > 0) então
                S = S'

                se (f(S') < f(S*)) então
                    S* = S'
                senão
                    selecione x ∈ [0, 1]

                    se (x < e^(-∆/T)) então
                        S* = S'
            fim se
        fim enquanto
        T = α * T
        IterT = 0
    fim enquanto

    retorne S*  
fim
```

## Referências Bibliográficas

[1] PRADO, Alan Souza. Problema de Alocação de Salas em Cursos Universitários: Um Estudo de Caso. Disponível em: http://www.decom.ufop.br/prof/marcone/projects/ppm497-13/Dissertacao-AlanSouzaPrado.pdf. <br>

[2] RIBEIRO, Paula Ceccon, et. al. HEURÍSTICAS ITERATED LOCAL SEARCH E GUIDED LOCAL SEARCH APLICADAS NA RESOLUÇÃO DO PROBLEMA DE ALOCAÇÃO DE SALAS. Disponível em: https://www.researchgate.net/profile/Paula-Ceccon/publication/261834613_Heuristicas_Iterated_Local_Search_e_Guided_Local_Search_aplicadas_na_resolucao_do_Problema_de_Alocacao_de_Salas/links/00b4953597ebc5b7e6000000/Heuristicas-Iterated-Local-Search-e-Guided-Local-Search-aplicadas-na-resolucao-do-Problema-de-Alocacao-de-Salas.pdf. <br>

[3] SOUZA, Marcone Jamilson Freitas, et. al. EXPERIÊNCIAS COM SIMULATED ANNEALING E BUSCA TABU NA RESOLUÇÃO DO PROBLEMA DE ALOCAÇÃO DE SALAS. Disponpível em: http://www.decom.ufop.br/marcone/Disciplinas/InteligenciaComputacional/SBPO-2002-PAS-TC0106.pdf