from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa el navegador y abre la página web

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
#driver = webdriver.Edge()
driver.get('https://servicios-de-valoracion.apps.bancolombia.com/Evaluaciones')

# Localiza el botón por su ID y realiza un clic
boton = driver.find_element_by_class_name('botonPositivo btn btn-primary')##driver.find_element(By.ID, 'id_del_boton')
boton.click()

# Cierra el navegador
# Tercera prueba
driver.quit()