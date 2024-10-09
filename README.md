# Documentação do ChatBot da Padaria Primeira Linha

## Introdução
Este ChatBot foi desenvolvido para automatizar o atendimento da **Padaria Primeira Linha** via WhatsApp. Utilizando a API do Twilio, ele interage com os clientes, enviando informações sobre localização, cardápios, atendimento personalizado, entre outros serviços. O bot responde automaticamente às mensagens recebidas, utilizando a similaridade de palavras para fornecer as respostas mais adequadas.

### Tecnologias Utilizadas
- **Flask**: Framework web para lidar com as requisições HTTP.
- **Twilio API**: Utilizada para enviar e receber mensagens via WhatsApp.
- **Levenshtein**: Usado para calcular a similaridade entre as palavras enviadas pelo usuário e os comandos pré-definidos.

---

## Estrutura Geral do Código
### Arquivo principal: `padariaBot.py`

### Imports:
- **twilio.rest.Client**: Para interagir com a API da Twilio.
- **flask.Flask, request**: Para lidar com as rotas e requisições HTTP.
- **twilio.twiml.messaging_response.MessagingResponse**: Para criar respostas a serem enviadas ao WhatsApp.
- **Levenshtein**: Para verificar a similaridade entre palavras.

### Funções Principais:

#### `sendMessage(text: str, to: str, fromwwp: str)`
Essa função envia mensagens para o cliente via WhatsApp utilizando a API da Twilio.
- **Parâmetros**:
  - `text`: Texto da mensagem a ser enviada.
  - `to`: Número do destinatário.
  - `fromwwp`: Número do remetente.
  
#### `reply()`
Esta é a principal função de resposta, chamada toda vez que uma mensagem é recebida. Ela lida com os diferentes comandos do usuário e responde de acordo.
- **Fluxo**:
  1. Obtém a mensagem do usuário e converte para minúsculas.
  2. Verifica a mensagem recebida e executa as ações correspondentes, como envio do cardápio ou informações de localização.
  3. Se a mensagem não corresponder a nenhum comando, a função sugere a palavra mais próxima usando a similaridade de Levenshtein.

#### `secondReply(msgtext)`
Função que fornece respostas detalhadas baseadas na escolha do cliente, como a localização da padaria, cardápios, links de atendimento específico, entre outros.

#### `ajuda()`
Exibe as opções disponíveis no momento para o cliente, como ver o cardápio, atendimento via Ifood, entre outros.

#### `intro()`
Esta função dá boas-vindas ao usuário, apresentando o ChatBot e oferecendo ajuda.

### Comandos e Palavras-Chave

O ChatBot reconhece diversos comandos e palavras-chave que são verificadas nas mensagens recebidas. Alguns exemplos são:

- **Saudações**: "oi", "olá", "bom dia", "boa tarde", "boa noite", etc.
- **Consultas sobre cardápio**: "ver menu", "quero cardápio", "pratos", "preços", etc.
- **Pedidos de atendimento humano**: "quero falar com atendente", "solicito atendimento", etc.
- **Outras palavras**: "sim", "não", "1", "2", "3", "4", "5", "6" para selecionar opções.

### Similaridade de Texto
Se o bot não entende uma mensagem, ele tenta encontrar a palavra mais próxima dentro de um conjunto de palavras válidas. Para isso, a função `find_closest_match` usa o algoritmo de Levenshtein para comparar a palavra enviada com as possíveis respostas.

---

## Exemplos de Interação

### 1. **Consulta de Localização**
- **Usuário**: "Onde fica localizado?"
- **Bot**: "Nossa loja fica localizada na Rua Tavares Coutinho, 1871 - Varjota, Fortaleza - CE, 60160-130, venha nos visitar!!, para mais informações acesse: [Link Google Maps]"

### 2. **Consulta do Cardápio**
- **Usuário**: "Quero ver o cardápio"
- **Bot**: Exibe uma lista completa de pratos e preços disponíveis.

### 3. **Solicitação de Atendimento**
- **Usuário**: "Quero falar com um atendente"
- **Bot**: Fornece o link de atendimento via WhatsApp para um atendente humano.

### 4. **Saudações**
- **Usuário**: "Oi"
- **Bot**: "Olá, tudo bem? Prazer eu sou o assistente virtual da Padaria Primeira linha e estou aqui pra ajudar!"

### 5. **Sugestão de Palavra**
- **Usuário**: "cartario"
- **Bot**: "Desculpa, não entendi sua dúvida. Você quis dizer 'cardápio'? (se a palavra for essa, redigite-a)"

---

## Observações Finais

- **Validação de Mensagens**: O bot verifica o texto enviado e responde apenas a palavras ou frases específicas. Caso contrário, ele tenta sugerir a palavra correta.
- **Flexibilidade nos Comandos**: O bot aceita variações de letras maiúsculas/minúsculas e pequenos erros de digitação.
- **Erro Tratamento**: Quando o comando não é encontrado, o bot educadamente pede que o usuário verifique sua mensagem e tenta sugerir uma alternativa.

---

## Melhorias Futuras

- **Integração com Banco de Dados**: Para fornecer informações atualizadas, como promoções e novos produtos automaticamente.
- **Aprimoramento da IA**: Implementação de um modelo de linguagem mais robusto para entender frases mais complexas.
- **Expansão de Funcionalidades**: Oferecer suporte a mais serviços, como agendamentos e pedidos personalizados.
