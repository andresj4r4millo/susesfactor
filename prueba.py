import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Inicializa el controlador del navegador (en este caso, Microsoft Edge)
driver = webdriver.Edge(executable_path='msedgedriver.exe')

try:
    driver.get("https://performancemanager8.successfactors.com/login?bplte_logout=1&company=comunicaci&_s.crb=VG1RqGoWUmkzkcagqGY%252fybzahzatv77ql1k8j0nbZ2E%253d#/login")
    
    # Iniciar sesión
    while True:
        try:
            driver.find_element(By.XPATH,'//*[@id="__input1-inner"]').send_keys("EC7061B")
            driver.find_element(By.XPATH,'//*[@id="__input2-inner"]').send_keys("Onecont2024*")
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="__button2-content"]').click()
            time.sleep(4)
            break
        except:
            print("Error al iniciar sesión")
    
    # Esperar a que la página se cargue completamente
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]'))
    )
    print("Página cargada")
    
    # Cambia el contexto al div principal
    div_principal = driver.find_element(By.ID, "shellbarContainer")
    driver.switch_to.frame(div_principal)
    
    # Buscar y interactuar con los elementos necesarios dentro del div principal
    while True:
        try:
            # Encuentra y realiza acciones en los elementos dentro del div principal
            button = driver.find_element(By.XPATH, '//*[@id="ui5wc_14-inner"]')
            button.click()
            button.send_keys("Texto de prueba")

            break
        except:
            print("Error al buscar e interactuar con elementos")
            continue
finally:
    # Cambia de vuelta al contexto principal antes de cerrar el navegador
    driver.switch_to.default_content()
    
    # Cierra el navegador al finalizar
    driver.quit()