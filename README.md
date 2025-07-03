Padrões utilizados: Factory Method, Bridge, Strategy

O padrão Factory Method foi escolhido para facilitar a montagem dos produtos, tendo uma base abstrata que se encaixa em todas opções de lanche. Esse padrão foi implementado por meio da superclasse abstrata Lanche e suas duas subclasses concretas Hambúrguer e Salsipão no arquivo lanche.py

O padrão Bridge foi escolhido para dividir as classes entre duas hierarquias diferentes. Esse padrão foi implementado através da comunicação das classes Condimento e Carne no implementacao.py com a classe Lanche do lanche.py

O padrão Strategy foi escolhido para criar diferentes famílias de algoritmos. Esse padrão foi implementado através da classe Condimento e suas subclasses, e da classe Carne e suas subclasses no implementacao.py