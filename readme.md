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
¿Cómo se llevará a cabo el proyecto? ¿Qué procedimientos implementarás para lograr los objetivos? Justifica tus respuestas.

## Herramientas y tecnologías: 
¿Qué técnicas de prompting utilizarás? Justifica tus respuestas 

## Implementación: 
Desarrolla el prompt y el código que te permitirá llegar a tu solución propuesta.



