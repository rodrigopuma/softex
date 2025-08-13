Jogo da Forca em Python
Descrição
Este projeto implementa o clássico Jogo da Forca em Python. O jogador deve tentar adivinhar uma palavra secreta, letra por letra, com um número limitado de tentativas. A cada erro, uma parte da forca é desenhada. O jogo termina quando o jogador adivinha a palavra ou quando esgota todas as tentativas.

Funcionalidades
Palavra Secreta: O jogo escolhe uma palavra aleatória de uma lista predefinida.

Tentativas Limitadas: O jogador tem um número limitado de tentativas para adivinhar a palavra.

Entrada do Usuário: O jogador insere uma letra por vez para tentar adivinhar a palavra.

Erros e Acertos: O jogo verifica se a letra inserida está correta e atualiza o estado do jogo.

Desenho da Forca: Cada erro resulta no desenho progressivo da forca, até que o jogador perca.

Vitoria ou Derrota: O jogador vence ao adivinhar todas as letras ou perde se as tentativas se esgotarem.

Requisitos
Python 3.x instalado.

Nenhuma biblioteca externa é necessária. Apenas a biblioteca padrão do Python.

Como Rodar
Baixe ou clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/jogo-da-forca.git
cd jogo-da-forca
Execute o jogo:
Execute o arquivo jogo_forca.py no terminal ou prompt de comando:

bash
Copiar
Editar
python jogo_forca.py
Jogue o jogo! O jogo irá instruí-lo a inserir letras para tentar adivinhar a palavra secreta.

Estrutura de Arquivos
jogo_forca.py: Código principal do jogo.

palavras.txt (opcional): Arquivo contendo uma lista de palavras que o jogo pode usar (caso queira adicionar mais palavras à lista).

Como Funciona o Jogo
O jogo escolhe uma palavra aleatória da lista predefinida.

O jogador deve tentar adivinhar a palavra, inserindo letras uma de cada vez.

A cada tentativa, o estado da palavra é atualizado, mostrando as letras corretas já adivinhadas e os espaços em branco para as letras ainda não descobertas.

Se o jogador errar, uma parte do corpo da forca será desenhada, e o número de tentativas diminui.

O jogo termina quando o jogador adivinha a palavra ou quando as tentativas acabam.

Exemplo de Execução
lua
Copiar
Editar
Bem-vindo ao jogo da forca!

_ _ _ _ _ _

Digite uma letra: a
Boa! A letra 'a' está na palavra.

_ a _ _ _ _

Digite uma letra: p
Boa! A letra 'p' está na palavra.

p a _ _ _ _

Digite uma letra: z
Ops! A letra 'z' não está na palavra.

_ _ _ _ _ _

A forca vai aparecendo com os erros...
Personalização
Você pode adicionar mais palavras à lista de palavras editando o código na função escolher_palavra() ou criando um arquivo palavras.txt com uma palavra por linha.

O desenho da forca é feito de maneira simples. Você pode modificar os estágios da forca no código se quiser personalizar ainda mais.

Contribuição
Se você quiser melhorar o código ou adicionar novos recursos, fique à vontade para abrir uma pull request ou sugerir melhorias.

Licença
Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para mais detalhes.

Esse é um modelo básico de README, mas você pode adaptar e expandir conforme necessário!