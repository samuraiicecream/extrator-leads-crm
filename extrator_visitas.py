from playwright.sync_api import sync_playwright
import time
import pandas as pd 
import os 
from dotenv import load_dotenv

load_dotenv()

class ExatratorVisistas:
    def __init__(self, url_login, usuario, senha, url_crm):
        self.url_login = url_login
        self.usuario = usuario
        self.senha = senha 
        self.url_crm = url_crm
        self.dados_extraidos = []
    def executar(self):
        with sync_playwright() as p:
            navegador = p.chromium.launch(headless=False)
            pagina = navegador.new_page()

            print("Acessando a página de login...")
            pagina.goto(self.url_login)

            pagina.fill('#email', self.usuario)
            print("E-mail preenchido")
            
            pagina.fill('input[type="password"]', self.senha)
            print("Senha preenchida.")
            
            pagina.click('button:has-text("Entrar")')
            print("Cliquei em entrar, aguardando carregamento...")

            pagina.wait_for_load_state('networkidle')
            print("Login concluído com sucesso!")

            print('Acessando o módulo de visitação...')
            pagina.goto(self.url_crm)
            pagina.wait_for_load_state('networkidle')

            print("acessando o módulo de visitação...")
          

            print("Buscando informações na tela...")

            while True:
                pagina.wait_for_selector('.lead-info')
                time.sleep(2)
            
                bloco_de_leads = pagina.locator('.lead-info').all()


           

                for bloco in bloco_de_leads:
                    nome=bloco.locator('.lead-name').inner_text().strip()
                    detalhes_email = bloco.locator('.lead-details').inner_text().strip()

                    self.dados_extraidos.append({
                    'Nome' : nome,
                    'Email': detalhes_email
                })
                print(f"Extraidos {len(bloco_de_leads)} leads desta página. Total até agora: {len(self.dados_extraidos)}")

                botao_proximo = pagina.locator("[wire\\:click*='next']")
            
                if botao_proximo.is_visible():
                 print("indo para a próxima página...")
                 botao_proximo.click()

                 pagina.wait_for_load_state('networkidle')

                else: 
                     print("Chegamos na ultima pagina! encerramos a busca.")
                     
                     break

 
        
        print("Navegador fechado. Extração finalizada com sucesso!")
        print("\n--- RESULTADO DA EXTRAÇÃO ---")

        for dado in self.dados_extraidos:
                    print(f"Nome: {dado['Nome']} | E-mail: {dado['Email']}")


        print("\nSalvando os dados em um arquivo...")

        df_visitantes = pd.DataFrame(self.dados_extraidos)


        df_visitantes.to_csv('visitantes_extraidos.csv', index=False)
        print("Sucesso! Arquivo 'visitantes_extraidos.csv' foi criado na sua pasta.")



       # print('Acessando o modulo de visitação...')#


          #print("Buscando alunos pré-matriculados...")#


         #  elementos_pre_matricula = pagina.locator("text='Pre-matricula").all()#
            

       #   for elemento in elementos_pre_matricula
              #  texto_do_elemento = elemento.inner_text()#
           #   print(f"Encontrei uma tag: {texto_do_elemento}")#

            
      
          #  print("Extração finalizada!")#


if __name__ == '__main__':
    # Busca as variáveis do .env
    url_secreta = os.getenv("URL_SISTEMA")
    usuario_secreto = os.getenv("USUARIO_SISTEMA")
    senha_secreta = os.getenv("SENHA_SISTEMA")
    url_crm_secreta = os.getenv("URL_CRM")

    
    meu_extrator = ExatratorVisistas(
        url_login=url_secreta,
        usuario=usuario_secreto,
        senha=senha_secreta,
        url_crm=url_crm_secreta 
    )
    meu_extrator.executar()
print("\n--")