# Chat con Asesor Financiero

## Problema:
Las mayoría de las personas no maneja sus finanzas de la forma correcta. Se endeudan y no tienen ahorros. A pesar de tener ingresos estables y sobra para ahorrar por mes.
Una solución es necesaria para que cada vez más personas empiecen a ahorrar y puedan mejorar su calidad de vida.

## Desarrollo de la propuesta:
La solución está basada en el uso de la generación de texto de OPEN AI para ayudar al usuario a tomar mejores decisiones financieras. Y también se utiliza la generación de imágenes de OPEN AI para generar una imagen que tenga el plan de acción tratado en el chat, para que el usuario se lo pueda llevar.

## Justificación de la viabilidad del proyecto: 
El proyecto es viable utilizando la API de OPEN AI. En este caso serían 3 partes del proceso en el que se usa la API:
- El primer paso es para el asesoramiento que se le da al usuario mediante el rol que se le da al sistema en el primer mensaje.
- El segundo paso arranca una vez que terminó el asesoramiento al usuario. Se toma todo el historial de chat entre el user y el asesor y se lo brindamos a la API de chat GPT, para que genere un prompt específico para generar la imagen, que eso sucede en el 3er paso
. El tercer paso es usar el prompt generado por la API de Chat GPT para darselo a DALL-E 3, y que genere el plan de acción en formato imagen.

## Objetivos:
Asesorar al usuario con sus decisiones financieras y brindarle un plan de acción.

## Metodología: 
El proyecto se llevará a cabo usando python, y la API de OpenAI, para generar textos e imágenes de acuerdo a la interacción del asistente con el usuario.
### Procedicientos:
- Importar el módulo de OpenAI, que sería la biblioteca de python que brinda openAI para interactuar con todos sus modelos.
- Importar json, un módulo de python que sirve para interactuar con datos en formato json (En este caso sería el historial de chats, ya que al prompt para generar la imagen, el chat se lo envío en ese formato).
- Obtener la API KEY de OpenAI para poder recibir respuestas del modelo de chat GPT.
- Crear un chatCompletion usando la API de openAI para poder interactuar con el modelo que elija en el header de la solicitud.
- Crear un contexto para brindarle al sistema y que entienda como tiene que actuar
- Almacenar toda la conversación
- Usar la conversación para generar un prompt y después una imagen, ambos con la API de Open AI (texto - texto y texto - imagen)

## Ténicas utilizadas: 
- One Shot Prompting: La uso en todas las solicitudes que hago a openAI en el código, para poder darle contexto al sistema.
- Few Shot Prompting: La uso para que el asistente entienda como debe responder a las preguntas del usuario en una primera instancia.

## Implementación: 
- En el archivo index.py desarrollé el código

# Mejoras
- Agregué "gpt-4o" como modelo a la hora de generar el prompt que se va a pasar a Dall-e 3 para tener mejores resultados que con "gpt 4o mini".
- Agregué detalles en el prompt que se le da a "gpt 4o" para que la imagen sea lo más real posible.

