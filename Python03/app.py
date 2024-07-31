# Quais tecnologias devem ser utilizadas
# Selenium
# Pyautogui

# Quais sao os passos manuais que quero automatizar?
#  1 - Entrar no site
#  2 - rolas a pagina inteira para baixo para carregar os produtos e clicar em "carregar mais" para visualizar o restante dos produtos
#  3 - Rolar a pagina totalmente para baixo
#  4 - Subir totalmente de volta para o topo
#  5 - Clicar em Subir planilha de precos
#  6 - Carregar planilhas "precos-produtos-atualizados.xlsx"

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

# Caminho do perfil do Chrome
chrome_profile_path = "/Users/leandroalexandre/Library/Application Support/Google/Chrome/Default"
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")

# Inicializa o driver do Chrome
driver = webdriver.Chrome(options=options)
driver.get('https://precos-de-produtos.netlify.app/')
sleep(5)

# Role até o final da página
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

# Encontre e clique no botão "Carregar Mais"
botao_carregar_mais = driver.find_element(
    By.XPATH, "//button[@id='loadMoreButton']")
sleep(2)
botao_carregar_mais.click()
sleep(2)

# Role novamente até o final da página
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

# Role até o topo da página
driver.execute_script('window.scrollTo(0, 0);')
sleep(3)

# Encontre e clique no botão "Carregar Planilha de Produtos"
botao_carregar_planilha_de_produtos = driver.find_element(
    By.XPATH, "//button[@class='btn btn-primary btn-custom']")
sleep(2)
botao_carregar_planilha_de_produtos.click()

# Aguarde um tempo suficiente para o diálogo do Finder abrir
sleep(3)

# Use pyautogui para inserir o caminho do arquivo e pressionar enter
pyautogui.write(
    '/Users/leandroalexandre/Desktop/Py/PyProjetos/Python03/precos-produtos-atualizados.xlsx')
sleep(1)
pyautogui.press('return')

input('Aperte enter no terminal para fechar o programa')

# Feche o driver do Chrome
driver.quit()
