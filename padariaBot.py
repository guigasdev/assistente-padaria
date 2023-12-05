import os
from twilio.rest import Client
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import Levenshtein

apbot = Flask(__name__)
def sendMessage(text : str, to: str, fromwwp: str):

    account_sid = "AC9db2603c4e9d8758fc629c78d77c2e92"
    auth_token = "1d39effac65729ebaa495660da527f6f"
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        from_ ='whatsapp:+558586964555',
        body=text,
        to=to
        )
    print(message.sid)


@apbot.route("/sms", methods = ["get","post"])
def reply():
    valid_words = ["oi","ola","olá", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "sim", "não", "bom dia", "boa tarde", "boa noite", "cardárpio", "menu", "quero menu", "ver menu", "como vejo o menu?", "ver o cardápio", "envia o cardápio", "pratos", "ver as entradsa?", "eu quero menu", "eu quero cardápio", "preços", "negociação", "eu quero ver os preços", "quero os preços", "preço dos pratos", "valor dos pratos", "tem como ter desconto?", "valores?", "qual o valor dos pratos?", "atendente", "atendimento", "atendente", "quero falar com um atendente", "eu quero falar com um atendente", "quero falar com o atendente", "quero falar com a atendente", "quero atendimento", "solicito atendimento", "eu preciso falar com um atendente", "eu preciso falar com uma atendente", "eu preciso falar com o gerente", "eu quero falar com um vendedor", "como eu falo com um atendente?", "como eu falo com um vendedor?", "como eu falo com uma atendente?", "como eu falo com o atendente?", "quero ser atendido", "quero falar com alguem", "preciso falar com um atendente","como solicitar o cardárpio", "eu quero ver o cardárpio", "gostaria de ver o menu", "preciso do cardárpio"]
    msgt = request.form.get("Body")
    msgt.lower()
    sen_num= request.form.get("From")
    me_num = request.form.get("To")
    print(msgt)
    print(sen_num)

    if(msgt == "1" or msgt == "2" or msgt == "3" or msgt == "4" or msgt == "5" or msgt == "6"):
            secondReply(msgt)
    elif(msgt == "sim" or msgt == "Sim" or msgt == "s" or msgt == "ss" or msgt == "SIm" or msgt == "SIM" or msgt == "sIM" or msgt == "siM"):
           ajuda()    

    elif(msgt == "não" or msgt == "Não" or msgt == "nao" or msgt == "Nao" or msgt == "n" or msgt == "nn"):
            msg = "Muito obrigado por estar conosco!!"
            sendMessage(msg, sen_num, me_num)
            msg = "Se precisar de algo a mais so mandar um olá!"
            sendMessage(msg, sen_num, me_num)
    
    elif(msgt == "cardápio" or  msgt == "menus" or msgt == "menu" or msgt == "ver menu" or msgt == "Quero ver menu" or msgt == "preciso do menu" or msgt == "quero cardápio" or msgt == "Quero ver o cardápio" or msgt == "ver menu" or msgt == "enviar menu" or msgt == "pratos" or msgt == "ver pratos" or msgt == " Como faço para ver o cardápio" or msgt == "cardápio de comida" or msgt == "Como ver o cardápio?" or msgt == "ver cardápio" or msgt == "cardápio" or msgt == "cardápio" or msgt == "enviar" or msgt == "solicitar menu" or msgt == "eu quero cardápio" or msgt == "eu quero menu" or msgt == "preciso cardápio"or msgt == "eu quero ver  as comidas do menu" or msgt == "preciso cardápio" or msgt == "eu preciso menu" or msgt == "preciso de cardápio"):
          especifico(1)
          loop()
    
    elif(msgt == "Vatapá" or "vatapa" or "vatapá" or "VATAPÁ" or "VATAPA"):
          especifico(2)
          loop()
    elif(msgt == "Arroz" or "ARROZ" or "arroz"):
         especifico(3)
         loop()      
    elif(msgt == "Patê" or "PATE" or "pate" or "PATÊ" or "patê"):
         especifico(4)
         loop()    
    elif(msgt == "Empadão" or "EMPADAO" or "empadao" or "EMPADÃO" or "empadão"):
         especifico(5)
         loop()
    elif(msgt == "Quiche" or "QUICHE" or "quiche"):
         especifico(6)
         loop()
    elif(msgt) == "kit nalino" or "kitnatal" or "Comidas natalista" or "Kit natal 1" or "Kit natal 2" or "opções natalinas":
         especifico(7)
         (loop)
    
    elif(msgt == "OI" or msgt == "Oi" or msgt == "oi" or msgt == "Olá" or msgt == "olá" or msgt == "Ola" or msgt == "ola" or msgt == "fala" or msgt == "opa" or msgt == "Fala" or msgt == "Opa" or msgt == "Bom dia" or msgt == "bom dia" or msgt == "bomdia" or msgt == "Boa tarde" or msgt == "boa tarde" or msgt == "boatarde" or msgt == "Bom tarde" or msgt == "bom tarde" or msgt == "bomtarde" or msgt == "Boa noite" or msgt == "boa noite" or msgt == "boanoite" or msgt == "Bom noite" or msgt == "bom noite" or msgt == "bomnoite" or msgt == "Boa dia" or msgt == "boa dia" or msgt == "boadia" or msgt == "Boadia" or msgt == "Bomtarde" or msgt == "Bomnoite" or msgt == "cuida" or msgt == "chama" or msgt == "agiliza" or msgt == "Pode me ajudar?" or msgt == "Pode me ajudar" or msgt == "pode me ajudar?" or msgt == "pode me ajudar" ):
        intro()
        ajuda()
  
    else:
        sugestion = find_closest_match(msgt, valid_words) 
        msg = 'Desculpa nao entendi a sua duvida, voce quis dizer "'+sugestion+'"?\n(se a palavra for essa, redigite-a)' 
        sendMessage(msg, sen_num, me_num)         

def secondReply(msgtext):
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    if(msgtext == "1"):
        msg = "Nossa loja fica localizada na Rua Tavares Coutinho, 1871 - Varjota, Fortaleza - CE, 60160-130, venha nos visitar!!, para mais informações acesse: \n https://www.google.com.br/maps/place/Padaria+Primeira+Linha/@-3.7324807,-38.4858801,17z/data=!3m1!4b1!4m6!3m5!1s0x7c7487f4c8f21ff:0x3ae78a25e0f755b3!8m2!3d-3.7324807!4d-38.4858801!16s%2Fg%2F1yg4dhnc5?entry=ttu"
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "2"):
        msg = """
            Nosso Cardápio dispões dos seguintes pratos:
                Bandeja de Frios -------- R$ 130,00
                Vatapá de Camarão ------- R$ 90,00
                Vatapá de Frango -------- R$ 60,00
                Salpicão ---------------- R$ 65,00
                Tender ------------------ R$ 120,00
                Arroz Natalino ---------- R$ 45,00
                Arroz Branco ------------ R$ 25,00
                Arroz de Camarão -------- R$ 75,00
                Frango Quatro Queijos --- R$ 70,00
                Lagarto ao Molho Madeira - R$ 109,00
                Strogonoff de Carne ------ R$ 90,00
                Cento de Salgados (Coxinha, bolinha, pastel carne ou queijo) - R$ 69,90
                Mini Árabe Recheado (cento) - R$ 190,00
                Pão Americano - R$ 69,00
                Farofa Natalina - R$ 50,00
                Rabanada - R$ 55,00
                Patê de Frango - R$ 45,00
                Patê de Presunto - R$ 40,00
                Empadão Frango - R$ 90,00
                Empadão Carne do Sol - R$ 120,00
                Empadão Misto - R$ 109,00
                Quiche Camarão - R$ 190,00
                Quiche de Queijo c/ geléia de pimenta - R$ 150,00
                Quiche de Espinafre c/ ricota - R$ 150,00
                Quiche de Álho Poro - R$ 150,00
                Quiche de Tomate Seco c/ provolone - R$ 150,00

                Pavê Taça (p) - R$ 109,00
                Charlotte Taça (p) - R$ 109,00
                Pudim (M) - R$ 90,00 
                Taça Felicidade (g) - R$ 209,00
                Taça Felicidade (p) - R$ 109,00
                Docinho - R$ 2,00
                Bolo Indiano (M) - R$ 99,00
                Bolo da Vovó (M) - R$ 99,00
                Peru  - R$ 350,00 
                Pernil  4kg  - R$ 390,00
                Chester 4kg - R$ 299,00

KIT NATALINO 1 - VALOR: R$999,00  - SERVE 15 PESSOAS
                               
1 Peru ou Pernil 4kg;
2 kg Carne Molho Madeira;
1 Torta salgada para 15 pessoas (escolha entre os sabores: mista ou carne do sol);
1 kg de Vatapá de Frango;
1 kg de Salpicão;
1 kg de Arroz Natalina;
1 kg de Arroz Branco;
1 kg de Farofa Natalina;
1 Sobremesa (pavê ou torta de charlotte
2 Refrigerante de 2 litros

-----------------------------------------------------------

KIT NATALINO 2 - VALOR: R$ 699,00 - SERVE 10 PESSOAS

1 Peru ou Pernil 4kg;
1 kg de Salpicão;
1 kg de Arroz Natalina;
1 kg de Vatapá de Frango;
1 kg de Farofa Natalina;
1 Sobremesa (pavê ou torta charlotte)
100 Salgados.


"""
        sendMessage(msg, sen_num, me_num)
        
    elif(msgtext == "3"):
        msg = "Também estamos presentes no IFOOD, para facilidade de acesso, procure-nos lá: \n https://www.ifood.com.br/delivery/fortaleza-ce/primeira-linha-varjota/b8df1a09-34e3-471e-a950-24db5eaf3b14"
        sendMessage(msg, sen_num, me_num) 
        loop()
    elif(msgtext == "4"):
        msg = "Para atendimento específico e prioritário, acesse: \n https://api.whatsapp.com/send?phone=5585998500065&text=Ol%C3%A1,%20Padaria%20Primeira%20Linha!%20Gostaria%20de%20realizar%20um%20pedido..."
        sendMessage(msg, sen_num, me_num)
        loop()
    elif(msgtext == "5"):
        msg = "Acesse nosso site: \n https://linktr.ee/padariaprimeiralinha"
        sendMessage(msg, sen_num, me_num)

    
def ajuda():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    
    msg = "1 - Onde fica localizado?\n2 - Quero ver o cardápio\n3 - Ifood\n4 - Atendimento específico\n5 - Site\n"
    sendMessage(msg, sen_num, me_num)

def intro():
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = 'Olá, tudo bem?'
    sendMessage(msg, sen_num, me_num)
    msg = "Prazer eu sou o assistente virtual da Padaria Primeira linha e estou aqui pra ajudar!"
    sendMessage(msg, sen_num, me_num)
    msg = 'Qual serviço você deseja?'
    sendMessage(msg, sen_num, me_num)
    
def loop():
    
    sen_num = request.form.get("From")
    me_num = request.form.get("To")

    msg = "Você precisa de mais alguma ajuda?\n (digite 'sim' ou 'não')"
    sendMessage(msg, sen_num, me_num)

def especifico(num):
     sen_num = request.form.get("From")
     me_num = request.form.get("To")

     if(num == 1):
          msg = """
            Nosso Cardápio dispões dos seguintes pratos:
                Bandeja de Frios -------- R$ 130,00
                Vatapá de Camarão ------- R$ 90,00
                Vatapá de Frango -------- R$ 60,00
                Salpicão ---------------- R$ 65,00
                Tender ------------------ R$ 120,00
                Arroz Natalino ---------- R$ 45,00
                Arroz Branco ------------ R$ 25,00
                Arroz de Camarão -------- R$ 75,00
                Frango Quatro Queijos --- R$ 70,00
                Lagarto ao Molho Madeira - R$ 109,00
                Strogonoff de Carne ------ R$ 90,00
                Cento de Salgados (Coxinha, bolinha, pastel carne ou queijo) - R$ 69,90
                Mini Árabe Recheado (cento) - R$ 190,00
                Pão Americano - R$ 69,00
                Farofa Natalina - R$ 50,00
                Rabanada - R$ 55,00
                Patê de Frango - R$ 45,00
                Patê de Presunto - R$ 40,00
                Empadão Frango - R$ 90,00
                Empadão Carne do Sol - R$ 120,00
                Empadão Misto - R$ 109,00
                Quiche Camarão - R$ 190,00
                Quiche de Queijo c/ geléia de pimenta - R$ 150,00
                Quiche de Espinafre c/ ricota - R$ 150,00
                Quiche de Álho Poro - R$ 150,00
                Quiche de Tomate Seco c/ provolone - R$ 150,00

                Pavê Taça (p) - R$ 109,00
                Charlotte Taça (p) - R$ 109,00
                Pudim (M) - R$ 90,00 
                Taça Felicidade (g) - R$ 209,00
                Taça Felicidade (p) - R$ 109,00
                Docinho - R$ 2,00
                Bolo Indiano (M) - R$ 99,00
                Bolo da Vovó (M) - R$ 99,00
                Peru  - R$ 350,00 
                Pernil  4kg  - R$ 390,00
                Chester 4kg - R$ 299,00

KIT NATALINO 1 - VALOR: R$999,00  - SERVE 15 PESSOAS
                               
1 Peru ou Pernil 4kg;
2 kg Carne Molho Madeira;
1 Torta salgada para 15 pessoas (escolha entre os sabores: mista ou carne do sol);
1 kg de Vatapá de Frango;
1 kg de Salpicão;
1 kg de Arroz Natalina;
1 kg de Arroz Branco;
1 kg de Farofa Natalina;
1 Sobremesa (pavê ou torta de charlotte
2 Refrigerante de 2 litros

-----------------------------------------------------------

KIT NATALINO 2 - VALOR: R$ 699,00 - SERVE 10 PESSOAS

1 Peru ou Pernil 4kg;
1 kg de Salpicão;
1 kg de Arroz Natalina;
1 kg de Vatapá de Frango;
1 kg de Farofa Natalina;
1 Sobremesa (pavê ou torta charlotte)
100 Salgados.


"""
          sendMessage(msg, sen_num, me_num)
    
     elif(num == 2):
          msg = """Nossos Pratos com Vatapá são:
                Vatapá de Camarão ------- R$ 90,00
                Vatapá de Frango -------- R$ 60,00
          """
          sendMessage(msg, sen_num, me_num)
     elif(num == 3):
          msg = """
         
                Nossos Pratos com Arroz são:
                Arroz Natalino ---------- R$ 45,00
                Arroz Branco ------------ R$ 25,00
                Arroz de Camarão -------- R$ 75,00
"""
          sendMessage(msg, sen_num, me_num)
         
     elif(num == 4):
          msg = """
                Nossos pratos com Patê são:
                Patê de Frango - R$ 45,00
                Patê de Presunto - R$ 40,00
          """
          sendMessage(msg, sen_num, me_num)
     elif(num == 5):
          msg = """
                Nossos pratos de empadão são:
                Empadão Frango - R$ 90,00
                Empadão Carne do Sol - R$ 120,00
                Empadão Misto - R$ 109,00
"""
          sendMessage(msg, sen_num , me_num)
     elif(num == 6):
          msg = """
                Nossos pratos de Quiche são:
                Quiche Camarão - R$ 190,00
                Quiche de Queijo c/ geléia de pimenta - R$ 150,00
                Quiche de Espinafre c/ ricota - R$ 150,00
                Quiche de Álho Poro - R$ 150,00
                Quiche de Tomate Seco c/ provolone - R$ 150,00
"""
          sendMessage(msg, sen_num , me_num)
     elif(num == 7):
          msg = """
KIT NATALINO 1 - VALOR: R$999,00  - SERVE 15 PESSOAS
                               
1 Peru ou Pernil 4kg;
2 kg Carne Molho Madeira;
1 Torta salgada para 15 pessoas (escolha entre os sabores: mista ou carne do sol);
1 kg de Vatapá de Frango;
1 kg de Salpicão;
1 kg de Arroz Natalina;
1 kg de Arroz Branco;
1 kg de Farofa Natalina;
1 Sobremesa (pavê ou torta de charlotte
2 Refrigerante de 2 litros

-----------------------------------------------------------

KIT NATALINO 2 - VALOR: R$ 699,00 - SERVE 10 PESSOAS

1 Peru ou Pernil 4kg;
1 kg de Salpicão;
1 kg de Arroz Natalina;
1 kg de Vatapá de Frango;
1 kg de Farofa Natalina;
1 Sobremesa (pavê ou torta charlotte)
100 Salgados."""
          sendMessage(msg, sen_num, me_num)
def find_closest_match(user_input, valid_words):
   
    closest_match = min(valid_words, key=lambda word: Levenshtein.distance(user_input, word))
    return closest_match

if(__name__=="__main__"):
    port = int(os.environ.get("PORT", 5000))
    apbot.run(host='0.0.0.0', port=port)