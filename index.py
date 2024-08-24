import openai
import json
import os
import requests
import time

apikey= openai.api_key = ""

few_shot_prompting = [
    {"role": "user", "content": "Hola"},
    {"role": "assistant", "content": "Hola, en que puedo ayudarte relacionado a las finanzas?"},
    {"role": "user", "content": "Quiero saber si es bueno invertir en bitcoin"},
    {"role": "assistant", "content": "Depende de cada inversor, perfil, ahorros, aversion al riesgo. Para poder ayudarte mejor te voy a hacer algunas preguntas: Primero, me indicarías si ya invertiste alguna vez en algún activo o es tu primera vez?"},
    {"role": "user", "content": "Nunca invertí"},
    ]

chatHistory = [{"role": "system", "content": f"Actuá como un asesor financiero. Hacé todas las preguntas necesarias para llegar a la mejor respuesta posible a la preugnta inicial del user. Y terminá el chat con una respuesta específica a lo que el usuario consulta. Tenés que dar respuestas cortas. Y hacer todas las preguntas necesarias. Si vas a hacer preguntas, hacelas de a una, y esperá la respuesta del usuario para pasar a la siguiente si es que la pregunta siguiente todavía es relevante. Acá tenés un ejemplo para guiarte de como deberías ser el chat {few_shot_prompting}"}]

def chatInfinit(chat, history):
    if history != "":
        question = history
    else:
        question = input('Tu turno: \n')
    
    chatHistory.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
    messages=chat,
    model="gpt-4o-mini",
    temperature=1,
    n=1,
    )
    assistant = response.choices[0].message
    chatHistory.append(assistant)
    print(f"Asistente: {assistant.content} \n")

def createPrompt(chat):
    chatString = json.dumps(chat, ensure_ascii=False)
    respuesta = openai.ChatCompletion.create(
        messages=[
            {"role": "system", "content": "Sos un sistema que recibe un historial de chat entre un asesor financiero y un usuario y genera el prompt más específico posible para que al darselo a DALL-E 3, este genere una imagen de una hoja de papel con el plan de acción para resolver la duda del usuario. Tiene que ser un plan de acción visual, con los pasos brindados por el asesor, para que el usuario al ver la imagen entienda el paso a paso y que tiene que hacer. La imagen tiene que ser REAL een cuanto al contenido que muestra del chat. La imagen tiene que mostrar datos reales sacados del chat"},
            {"role": "user", "content": chatString}
            ],
        model="gpt-4o",
        temperature=0,
        n=1
    )
    promptGenerado = respuesta.choices[0].message.content
    return createImage(promptGenerado)


def createImage(prompt):
    image = openai.Image.create(
        prompt= prompt,
        model="dall-e-3",
        size="1024x1024",
        quality="standard",
        n=1
    )
    imageUrl = image.data[0].url
    print(image.data[0].url)
    return imageUrl

def saveImage(imageUrl):
    response = requests.get(imageUrl)

    if response.status_code == 200:
        id = int(time.time())
        fileName = f"imagenChatFinaciero {id}"
        print("FileName: ", fileName)
        fileName += '.png'

        directory = "./image_generated"

        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = os.path.join(directory, fileName)

        with open(filepath, "wb") as f:
            f.write(response.content)
            print("La imagen ha sido descargada y almacenada correctamente en:", filepath)


def chatSession():
    print("Chatea con nuestro asesor financiero \n")
    while True:
        try:
            continueChat
            chatInfinit(chatHistory, continueChat)
        except:
            continueChat = ""
            chatInfinit(chatHistory, continueChat)

        continueChat = input("Tu respuesta (write x to exit): ")
        if continueChat == "x":
            responseFinal = input("Antes de irte, ¿Te gustaría generar un plan de acción visual [Y/N] \n").lower()
            if responseFinal == "y":
                print("Cargando plan de acción... \n")
                imageUrlObtained = createPrompt(chatHistory)

                saveImage(imageUrlObtained)

                print("Gracias por usar nuestro chat \n")
            else:
                print("Gracias por usar nuestro chat financiero \n")
                break
            break

chatSession()

