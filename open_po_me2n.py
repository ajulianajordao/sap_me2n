import time
import pyautogui
import csv

# Função para esperar até que um elemento apareça na tela
def wait_until_appears(image_path, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if pyautogui.locateOnScreen(image_path) is not None:
            return True
        time.sleep(1)
    return False

# Função para clicar em um elemento com base em sua imagem
def click_element(image_path):
    element_location = pyautogui.locateOnScreen(image_path)
    if element_location is not None:
        pyautogui.click(element_location.left + element_location.width / 2, element_location.top + element_location.height / 2)

# Espera até que a janela SAP ME2N apareça
if wait_until_appears('me2n_window.png'):
    # Preenche os campos necessários
    pyautogui.write('seu_numero_documento')
    pyautogui.press('enter')

    # Espera até que a lista de resultados ME2N seja carregada
    if wait_until_appears('me2n_results.png'):
        # Clique no botão de exportação
        click_element('export_button.png')

        # Espera até que a opção de exportação para CSV seja visível
        if wait_until_appears('csv_option.png'):
            # Clica na opção de exportação para CSV
            click_element('csv_option.png')

            # Aguarda até que a janela de salvamento do arquivo apareça
            if wait_until_appears('save_dialog.png'):
                # Preenche o nome do arquivo e pressiona Enter
                pyautogui.write('caminho/para/salvar/dados.csv')
                pyautogui.press('enter')
                print("Dados exportados para dados.csv")
            else:
                print("Erro: Janela de salvamento do arquivo não encontrada.")
        else:
            print("Erro: Opção de exportação para CSV não encontrada.")
    else:
        print("Erro: Lista de resultados ME2N não carregada.")
else:
    print("Erro: Janela SAP ME2N não encontrada.")
