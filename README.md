# Q_A Questions&Answers

_Este módulo es un poco básico, lo que realiza es una solicitud requests a google y directamente extrae la la respuesta a la pregunta que fue realizada, en caso de que esta pregunta no se encuentre en las respuestas rápidas que brinda google, el sistema scrapea las primeras páginas y realiza un análisis de NLP para extraer la respuesta de forma sintetizada así como determinar cual de las páginas contiene la mejor respuesta._

## Comenzando 🧠➕🤖 = 👍

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer cómo desplegar el proyecto.


### Pre-requisitos 📋

_Antes de instalar el proyecto es importante contar con las siguientes paqueterias y las versiones mostradas, actualmente solo funciona con dichas versiones._

_NOTA: Es altamente recomendable utilizar entornos virtuales, para evitar problemas de compatibilidad con otros archivos_

* beautifulsoup4==4.7.1
* textacy==0.6.2
* msgpack==0.6.1
* spacy
* es-core-news-sm --> este programa se instala escribiendo en la terminal "python -m spacy download es_core_news_sm"_

_Desde tu terminal ejecuta los siguientes comandos_
```
pip install beautifulsoup4==4.7.1
pip install textacy==0.6.2
pip install msgpack
pip install -U spacy
python -m spacy download en_core_web_sm
```

### Instalación 🔧
_NOTA: Tambien subí una versión solo para ejecutar_

_Para la instalación de este programa lo unico que tienes que hacer es descargar el archivo .tar.gz y ejecutar el siguiente comando (tomando en cuenta el número de versión del archivo):_

```
pip install Preguntas\&Respuestas-1.6.1.tar.gz
```

_Una vez instalado puedes utilizarlo en tus scripts escribiendo las siguientes líneas_

```
from QuestionsAnswers.Q_A import ExtraccionRespuestas
QAnswer = ExtraccionRespuestas()

pregunta = "Cuando murió Benito Juárez"
respuesta =QAnswer.MainUser(pregunta)

print(respuesta)

18 de julio de 1872, Palacio Nacional, Ciudad de México, México

```
_El codigo te retornará un string con la respuesta a la pregunta_

_algunos ejemplos de preguntas faciles son:_

* Quien Descubrio america?
* Que es el amor?
* Cuantos años tiene Chabelo?
* Donde esta el Taj Mahal?
* Cuando fue la primera guerra mundial?
* Por que vuelan los aviones?

_Preguntas mas complejas como:_

* Que pasa si metes una uva al microondas?
* Que opinas del nuevo presidente de México?
* Analisis y opinion de pelicula de Avengers endgame
* Que puedo hacer para pasar un examen si no estudie?

_La segunda parte de preguntas es mucho mas complejo que las primeras, como esta segunda parte requiere de mas procesamiento y NLP ademas del scrapeo a distintas paginas, se demora un poco mas de tiempo en retornar una respuesta_

## Construido con 🛠️

_Las Herramientas que se utilizaron para la creación de este proyecto fueron_

* [spacy](https://spacy.io/models) - modelo de lenguaje natural
* [textacy](https://pypi.org/project/textacy/) - Procesamiento de textos
* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Extraccion de datos de paginas WEB

## Autor ✒️

* **Luis Gerardo Fosado Baños** - *Trabajo y Documentación*- [GerardoX1](https://github.com/GerardoX1)


## Licencia 📄

Este proyecto está bajo la Licencia LuisGerardoF - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓.
* aqui dejo mi Linkedin (linkedin.com/in/gerardo-fosado-0ab957165)



---
