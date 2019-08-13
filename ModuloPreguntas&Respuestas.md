# Q_A Questions&Answers

_Este modulo es un poco basico, lo que realiza es una solicitud requests a google y directamente extrae la la respuesta a la pregunta que fue realizada, en caso de que esta pregunta no se encuentre en las respuestas rapidas que brinda google, el sistema scrapea las primeras paginas y realiza un analisis de NLP para extraer la respuesta de forma sintetizada asi como determinar cual de las paginas contiene la mejor respuesta._

## Comenzando 🧠➕🤖 = 👍

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Antes de instalar el proyecto es importante contar con las siguientes paqueterias y las versiones mostradas, actualmente solo funciona con dichas versiones._

_NOTA: Es altamente recomendable utilizar entornos virtuales, para evitar problemas de compatibilidad con otros archivos_

_beautifulsoup4==4.7.1
textacy==0.6.2
msgpack==0.6.1
spacy
es-core-news-sm --> este programa se instala escribiendo en la terminal "python -m spacy download es_core_news_sm"_

_Desde tu terminal ejecuta los siguientes comandos_
```
pip install beautifulsoup4==4.7.1
pip install textacy==0.6.2
pip install msgpack
pip install -U spacy
python -m spacy download en_core_web_sm
```

### Instalación 🔧

_Para la instalacion de este programa lo unico que tienes que hacer es descargar el archivo .tar.gz y ejecutar el siguiente comando (tomando en cuenta el numero de version del archivo):_

```
pip install Preguntas\&Respuestas-1.6.1.tar.gz
```

_Una ves instalado puedes utilizarlo en tus scrips escribiendo las siguientes lineas_

```
from QuestionsAnswers.Q_A import ExtraccionRespuestas
QAnswer = ExtraccionRespuestas()

pregunta = "Cuando murio benito juarez"
respuesta =QAnswer.MainUser(pregunta)

print(respuesta)

```
_El codigo te retornara un string con la respuesta a la pregunta_

## Construido con 🛠️

_Las Herramientas que se utilizaron para la creacion de este proyecto fueron_

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
