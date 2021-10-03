import speech_recognition as sr
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyttsx3
import keyboard
import time
from selenium import webdriver

navegador = webdriver.Chrome("chromedriver.exe")

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

newVoiceRate = 200
engine.setProperty('rate', newVoiceRate)


def talk(text):
    engine.say(text)
    engine.runAndWait()


while True:
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            talk('Iniciando')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='pt-BR')
            command = command.lower()
            print(command)
            if 'cadastrar clientes' or 'cadastrar cliente' in command:
                navegador.get("http://localhost/sitecadastroconsultaclientes/")
                while True:
                    with sr.Microphone() as source:
                        listener.adjust_for_ambient_noise(source)
                        btnCadastrar = navegador.find_element_by_xpath('/html/body/section/div/div/div/div/form/button')
                        nome = navegador.find_element_by_xpath(
                            '/html/body/section/div/div/div/div/form/div[1]/div/input')
                        cpf = navegador.find_element_by_xpath(
                            '/html/body/section/div/div/div/div/form/div[2]/div/input')
                        tel = navegador.find_element_by_xpath(
                            '/html/body/section/div/div/div/div/form/div[3]/div/input')
                        dn = navegador.find_element_by_xpath('/html/body/section/div/div/div/div/form/div[4]/div/input')
                        talk('Dados')
                        voice = listener.listen(source)
                        command = listener.recognize_google(voice, language='pt-BR')
                        command = command.lower()
                        if 'nome' in command:
                            command = command.replace("nome", "")
                            command = command.lower()
                            nome.send_keys(command)
                            print(command)
                        if 'cpf' in command:
                            command = command.replace("cpf", "")
                            command = command.lower()
                            cpf.send_keys(command)
                            print(command)
                        if 'telefone' in command:
                            command = command.replace("telefone", "")
                            command = command.lower()
                            tel.send_keys(command)
                            print(command)
                        if 'nascimento' in command:
                            command = command.replace('nascimento', "")
                            command = command.replace('/', "")
                            command = command.replace(' ', "")
                            command = command.lower()

                            tel.click()
                            actions = ActionChains(navegador)
                            actions.send_keys(Keys.TAB * 1)
                            actions.perform()
                            for i in command:
                                print(i)
                                time.sleep(0.1)
                                keyboard.press(i)
                            btnCadastrar.click()
                        if 'parar' in command:
                            break
    except:
        pass
