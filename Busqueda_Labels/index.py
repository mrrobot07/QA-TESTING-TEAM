
#importar las librerias de selenium
from selenium import webdriver;

#inicializar el browser y la busqueda de un elemento en si
browser = webdriver.Firefox();
browser.get('https://www.google.com');


#funcion para buscar los elementos de manera dinámica
def labelsSearch(textos):
    for x in textos:
        try:
            result = browser.find_element_by_xpath("//*[contains(@value,'"+ x +"')] | //*[contains(text(),'"+ x +"')]").text;
            print("PASSED: " + x + "\n");
        except:
            print("FAILED: " + x + "\n");

labels = ["Buscar con Google","Me siento con suerte","Gmail","Imágenes"];
labelsSearch(labels);
