import re
import bs4
import time
import textacy
import requests
import operator
import threading
import multiprocessing
from googletrans import Translator
from timeout_decorator import timeout

class ExtraccionRespuestas():
    
    def __init__(self):
        self.translator = Translator()
        #TranslatorGoogle.__init__(self)
        self.stopwords = ['y','a','o','de','del','la','los','las','actualmente','fueron','como', 'buenas', 'pronto', 'tener', 'mío', 'quien', 'mas', 'ademas', 'debido', 'éste', 'cual', 'sigue', 'cierto', 'mía', 'con', 'haya', 'tuyas', 'suya', 'muchos', 'hicieron', 'mal', 'buena', 'misma', 'ayer', 'aún', 'mucha', 'tendrán', 'nos', 'solo', 'próximos', 'apenas', 'ninguna', 'éstos', 'dónde', 'míos', 'podrian', 'entre', 'nosotros', 'allí', 'siendo', 'deben', 'durante', 'pueda', 'pocos', 'vaya', 'mios', 'consigo', 'cuantos', 'primeros', 'estado', 'consigue', 'verdad', 'adrede', 'trabaja', 'cada', 'ciertos', 'el', 'tu', 'hacemos', 'diferente', 'estas', 'aquél', 'antaño', 'vez', 'todo', 'última', 'comentó', 'nuevas', 'sino', 'del', 'tenga', 'primero', 'ella', 'desde', 'porque', 'encuentra', 'mismas', 'propios', 'además', 'menos', 'luego', 'asi', 'todavía', 'contigo', 'mismo', 'no', 'tanto', 'mias', 'había', 'raras', 'grandes', 'al', 'sería', 'lado', 'cuando', 'somos', 'nuestras', 'ellas', 'ésa', 'aquel', 'si', 'tres', 'creo', 'embargo', 'podrá', 'hemos', 'cuanto', 'nueva', 'quedó', 'sabemos', 'alguna', 'eras', 'día', 'hubo', 'siguiente', 'debajo', 'usted', 'hacen', 'incluso', 'cuándo', 'tercera', 'van', 'cuantas', 'habia', 'manifestó', 'tras', 'eramos', 'nuevo', 'aunque', 'entonces', 'donde', 'solas', 'todas', 'bueno', 'podría', 'un', 'realizado', 'ésas', 'solamente', 'ahí', 'supuesto', 'una', 'proximo', 'sabes', 'tenido', 'trata', 'la', 'antes', 'próximo', 'nosotras', 'dos', 'veces', 'pocas', 'ser', 'todavia', 'arriba', 'bastante', 'aquella', 'arribaabajo', 'aquellas', 'eran', 'esos', 'mencionó', 'dejó', 'llegó', 'últimos', 'peor', 'gran', 'otra', 'despacio', 'igual', 'aun', 'alguno', 'intentar', 'aquélla', 'intenta', 'poner', 'ampleamos', 'aquellos', 'principalmente', 'junto', 'antano', 'ambos', 'cuatro', 'da', 'algo', 'su', 'están', 'ustedes', 'fue', 'más', 'todos', 'es', 'ocho', 'eres', 'poca', 'por', 'seis', 'demasiado', 'se', 'nuevos', 'dado', 'usamos', 'conseguimos', 'pudo', 'ninguno', 'existen', 'ese', 'buenos', 'contra', 'sus', 'tuvo', 'consiguen', 'estuvo', 'ultimo', 'habían', 'alrededor', 'segunda', 'realizó', 'hay', 'que', 'cualquier', 'tendrá', 'afirmó', 'últimas', 'intentamos', 'estar', 'algunos', 'cuántas', 'haces', 'estaba', 'cuál', 'nuestro', 'enseguida', 'explicó', 'primera', 'pasada', 'propias', 'dia', 'pasado', 'dicen', 'toda', 'llevar', 'nada', 'mio', 'vamos', 'total', 'muy', 'lleva', 'encima', 'tan', 'demás', 'os', 'unas', 'usan', 'expresó', 'vuestra', 'consideró', 'largo', 'horas', 'propia', 'quiénes', 'saber', 'claro', 'tarde', 'aquéllas', 'cerca', 'tambien', 'tampoco', 'cuales', 'debe', 'excepto', 'será', 'siete', 'vuestros', 'aqui', 'lejos', 'verdadero', 'pueden', 'saben', 'dar', 'esto', 'detrás', 'ante', 'fui', 'partir', 'bien', 'puede', 'aquello', 'quizas', 'sea', 'hago', 'mayor', 'sean', 'tus', 'usa', 'acuerdo', 'usar', 'era', 'cinco', 'agregó', 'ex', 'han', 'eso', 'través', 'te', 'nuestra', 'estamos', 'podriamos', 'ahora', 'siempre', 'hacia', 'de', 'mías', 'sé', 'ahi', 'mia', 'quiere', 'puedo', 'mejor', 'bajo', 'este', 'para', 'habla', 'uso', 'qué', 'trabajo', 'suyas', 'realizar', 'suyo', 'éstas', 'delante', 'conmigo', 'añadió', 'hablan', 'mucho', 'atras', 'les', 'aproximadamente', 'hace', 'podeis', 'ir', 'ésos', 'dieron', 'podria', 'tiempo', 'tuyos', 'quizá', 'varias', 'estados', 'tiene', 'dentro', 'medio', 'ver', 'ha', 'vais', 'lugar', 'hoy', 'me', 'ello', 'modo', 'quién', 'también', 'pesar', 'tenemos', 'sabe', 'hacerlo', 'hacer', 'repente', 'cuáles', 'buen', 'despues', 'sin', 'estos', 'menudo', 'ya', 'tienen', 'uno', 'alli', 'muchas', 'existe', 'sí', 'conseguir', 'tuyo', 'soy', 'dijo', 'cuenta', 'teneis', 'estaban', 'propio', 'casi', 'país', 'haber', 'yo', 'vuestras', 'adelante', 'considera', 'nunca', 'final', 'vosotras', 'esa', 'fuera', 'días', 'primer', 'sera', 'posible', 'esas', 'respecto', 'parece', 'va', 'aseguró', 'esta', 'cierta', 'podemos', 'poder', 'pues', 'él', 'dice', 'las', 'serán', 'trabajamos', 'segun', 'algún', 'quiza', 'dan', 'así', 'ningunas', 'trabajar', 'varios', 'son', 'hasta', 'ciertas', 'tengo', 'general', 'cosas', 'cuánta', 'nuestros', 'mí', 'después', 'vuestro', 'momento', 'informó', 'último', 'sido', 'detras', 'podrias', 'segundo', 'conocer', 'anterior', 'solos', 'estará', 'lo', 'consigues', 'intentas', 'decir', 'he', 'mismos', 'breve', 'dicho', 'ningún', 'otros', 'usas', 'mis', 'ellos', 'dijeron', 'intentais', 'otras', 'quizás', 'aquéllos', 'tal', 'dias', 'pais', 'cómo', 'indicó', 'podrían', 'en', 'tenía', 'señaló', 'ésta', 'temprano', 'soyos', 'los', 'fin', 'deprisa', 'mediante', 'según', 'parte', 'manera', 'habrá', 'hecho', 'mientras', 'quienes', 'tuya', 'poco', 'estais', 'ti', 'aquí', 'ése', 'sólo', 'mi', 'cuánto', 'intento', 'ningunos', 'dio', 'sola', 'intentan', 'otro', 'podrán', 'queremos', 'fuimos', 'unos', 'algunas', 'salvo', 'estan', 'voy', 'diferentes', 'pero', 'enfrente', 'tú', 'cuanta', 'cuántos']
        self.tipo_preguntas = ['qué', 'cómo', 'cuándo', 'dónde', 'quién', 'quiénes', 'cuáles', 'cuál', 'cuánto', 'cuántos','cuánta', 'cuántas']
        self.informacion_hilos = ['', '', '', '', '']
        self.thread_num = 3
        self.proxies = {'http':'http://sistemasProxies:Adrian2010%25%25@mx.smartproxy.com:20000','https':'https://sistemasProxies:Adrian2010%25%25@mx.smartproxy.com:20000'}
        self.clasifica_preguntas = {'qué':'explicación', 'cómo':'explicación', 'cuándo':'tiempo', 'dónde':'lugar', 'quién':'sujetos', 'quiénes':'sujetos', 'cuáles':'explicación', 'cuál':'explicación', 'cuánto':'cantidad', 'cuántos':'cantidad',
                      'cuánta':'cantidad', 'cuántas':'cantidad'}
    
    def TokenizationL(self,texto):
        texto = texto.lower()
        tokens = re.split(r'\(\d+\)|[\s\.,:;?¿!/{}\"”“]+', texto)
        return tokens
    
    def ExtraerURL(self,html):
        sopa = bs4.BeautifulSoup(html, "html.parser")
        urls = [child.get("href") for link in sopa.find_all("h3", class_="r") for child in link.contents]
        if not urls:
            for link in sopa.find_all("div", class_="r"):
                for child in link.contents:
                    try:
                        urls.append(child.get("href"))
                    except AttributeError:
                        print('error')
        urls = [url for url in urls if url != None]
        return urls
    
    
    def ExtraerInformacion(self,url, num_hilo):
        status ='connect'
        while status =='connect':
            try:
                r = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    }, proxies=self.proxies)
                status='OK'
            except:
                pass
        html = r.text
        sopa = bs4.BeautifulSoup(html, "html.parser")
        cadena = ''
        
        for tex in sopa.find_all('p'):
            try:
                text = re.sub(r'<[^>]*>|\\x..','', str(tex))
                if text[-1] != '.':
                    cadena = cadena + text + '. '
                else:
                    cadena = cadena + text
                    
            except IndexError:
                pass

        cadena = cadena.replace('\xa0', ' ')
        cadena = cadena.replace('\t', '')
        cadena = cadena.replace('\n', ' ')
        cadena = cadena.replace('.', '. ')
        cadena = cadena + " . "
        frase_tokens = self.TokenizationL(cadena)

        self.lock.acquire()
        self.informacion_hilos[int(num_hilo)] = cadena
        self.lock.release()
        
    
    def RecortarPregunta(self,peticion):
        peticion =self.preprocesamiento_pregunta(peticion)
        if 'cómo se llama' in peticion:
            peticion = peticion.replace('cómo se llama','quién es')
        peticion = self.TokenizationL(peticion)
        #print('esto es peticion',peticion)
        for i in range(len(peticion)):
            if peticion[i] in self.tipo_preguntas:
                peticion = peticion[i:]
                break
        print('esto es peticion', ' '.join(peticion))
        return ' '.join(peticion).strip()
        
        
    def ObtenerInformacion(self,peticion):

        self.informacion_hilos = ['', '', '', '', '']
        
        peticion = self.RecortarPregunta(peticion)
        self.palabrasClave =[palabra for palabra in self.TokenizationL(peticion) if palabra not in self.stopwords]
        self.palabrasClave = self.palabrasClave + list(map(lambda x: x.capitalize (), self.palabrasClave))
        status ='connect'
        while status == 'connect':
            try:
                r = requests.get("https://www.google.com.mx/search?q=" + peticion.replace(' ', '+').replace('ó','o').replace('á','a').replace('é','e').replace('í','i').replace('ú','u'), headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0',
                'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
                    }, proxies=self.proxies)
                status='OK'
            except:
                pass
        
        html = r.text
        url_primario = r.url
        print(url_primario)
        
        # ---------SE REVISAN LOS RECUADROS DE GOOGLE---------------------

        respuesta = self.InfoRecuadros(peticion, html)
        if (respuesta != None):
            respuesta = respuesta.replace('Descripción','').replace('Wikipedia','').replace('Más elementos…','')
            return respuesta
        informacion_final = ''
    
        try:
            self.threading_Multi(html)
        except IndexError:
            pass     
 
        if self.informacion_hilos:
            Respuestas=[self.Answers(i,self.palabrasClave) for i in self.informacion_hilos]
            RespuestasValoradas = sorted(Respuestas, key=lambda tup: float(tup[1]), reverse=True)
            respuesta = RespuestasValoradas[0][0]
            return respuesta
        else:
            return 'no esta funcionando bien el internet'
            

    def threading_Multi(self,html):
        self.lock = multiprocessing.Lock()
        enlaces = self.ExtraerURL(html)
        self.all_threads = []

        for i in range(self.thread_num):
            t1 = threading.Thread(target=self.ExtraerInformacion, args=(enlaces[i], str(i)), daemon=True)
            t1.start()
            self.all_threads.append(t1)

        for current_thread in self.all_threads:
            current_thread.join()  
    
    def preprocesamiento_pregunta(self,pregunta):
        pregunta = ' '+pregunta+' '
        pregunta = pregunta.replace(' porque ', ' por qué ')
        pregunta = pregunta.replace(' Porque ', ' por qué ')
        pregunta = pregunta.replace(' Que ', ' qué ')
        pregunta = pregunta.replace(' Qué ', ' qué ')
        pregunta = pregunta.replace(' que ', ' qué ')
        pregunta = pregunta.replace(' Como ', ' cómo ')
        pregunta = pregunta.replace(' Cómo ', ' cómo ')
        pregunta = pregunta.replace(' como ', ' cómo ')
        pregunta = pregunta.replace(' Cuando ', ' cuándo ')
        pregunta = pregunta.replace(' Cuándo ', ' cuándo ')
        pregunta = pregunta.replace(' cuando ', ' cuándo ')
        pregunta = pregunta.replace(' Donde ', ' dónde ')
        pregunta = pregunta.replace(' Dónde ', ' dónde ')
        pregunta = pregunta.replace(' donde ', ' dónde ')
        pregunta = pregunta.replace(' Cual ', ' cuál ')
        pregunta = pregunta.replace(' Cuál ', ' cuál ')
        pregunta = pregunta.replace(' cual ', ' cuál ')
        pregunta = pregunta.replace(' Cuales ', ' cuáles ')
        pregunta = pregunta.replace(' Cuáles ', ' cuáles ')
        pregunta = pregunta.replace(' cuales ', ' cuáles ')
        pregunta = pregunta.replace(' Quien ', ' quién ')
        pregunta = pregunta.replace(' Quién ', ' quién ')
        pregunta = pregunta.replace(' quien ', ' quién ')
        pregunta = pregunta.replace(' Quienes ', ' quiénes ')
        pregunta = pregunta.replace(' Quiénes ', ' quiénes ')
        pregunta = pregunta.replace(' quienes ', ' quiénes ')
        pregunta = pregunta.replace(' Cuánta ', ' cuánta ')
        pregunta = pregunta.replace(' Cuanta ', ' cuánta ')
        pregunta = pregunta.replace(' cuanta ', ' cuánta ')
        pregunta = pregunta.replace(' Cuánto ', ' cuánto ')
        pregunta = pregunta.replace(' Cuanto ', ' cuánto ')
        pregunta = pregunta.replace(' cuanto ', ' cuánto ')
        pregunta = pregunta.replace(' Cuántas ', ' cuántas ')
        pregunta = pregunta.replace(' Cuantas ', ' cuántas ')
        pregunta = pregunta.replace(' cuantas ', ' cuántas ')
        pregunta = pregunta.replace(' Cuántos ', ' cuántos ')
        pregunta = pregunta.replace(' Cuantos ', ' cuántos ')
        pregunta = pregunta.replace(' cuantos ', ' cuántos ')
        pregunta = pregunta.replace(' en qué año ', ' cuándo ')
        pregunta = pregunta.replace(' qué año ', ' cuándo ')
        return pregunta.strip()
    
    def InfoRecuadros(self,pregunta, html):
        pregunta = self.preprocesamiento_pregunta(pregunta)
        pregunta_tokenizada = self.TokenizationL(pregunta)
        posicion2 = [word for word in pregunta_tokenizada if word in self.tipo_preguntas]
        
        try:
            palabra_pregunta = posicion2[0]
        except  IndexError:
            return None

        tipo_pregunta = self.clasifica_preguntas[palabra_pregunta]
        soup = bs4.BeautifulSoup(html, "html.parser")
        #pprint.pprint(soup)
        
        # -------------------------------Busca Fechas-------------------------------
        
        if tipo_pregunta == 'tiempo':
           
            cuadro = None
            #cuando nacio alguien
            if re.search('naci(o|ó)', pregunta):
                try:
                    if soup.find('span', attrs={'class': 'w8qArf'}):

                        busqueda1 = soup.find_all('span', attrs={'class': 'w8qArf'})
                        for j,i in enumerate(busqueda1):
                            if 'Fecha' in i.text:
                                pivote=j
                                break
                        busqueda1 = soup.find_all('span', attrs={'class': 'LrzXr kno-fv'})

                        return busqueda1[pivote].text
                except:
                    cuadro = None

            #cuando murio alguien
            elif re.search('muri(o|ó)', pregunta):
                try:
                    if soup.find('span', attrs={'class': 'w8qArf'}):

                        busqueda1 = soup.find_all('span', attrs={'class': 'w8qArf'})
                        for j,i in enumerate(busqueda1):
                            if 'Fallecimiento' in i.text:
                                pivote=j
                                break
                        busqueda1 = soup.find_all('span', attrs={'class': 'LrzXr kno-fv'})

                        return busqueda1[pivote].text
                except:
                    cuadro = None
            
            #cuando ocurrio la primera guerra mundial
            elif soup.find('div', attrs={'class': 'Z0LcW'}):
                return str(soup.find('div', attrs={'class': 'Z0LcW'}).text)
            
            #OK un destacado primera linea cuando se descubrio america
            elif soup.find('div', attrs={'class': 'd9FyLd'}):
                return str(soup.find('div', attrs={'class': 'd9FyLd'}).text)
            
            #OK"cuando es el dia de la mujer"
            #"cuando es el dia del padre"
            elif soup.find('div', attrs={'class': 'gsrt vk_bk dDoNo'}):
                return str(soup.find('div', attrs={'class': 'gsrt vk_bk dDoNo'}).text)
            
            #OK"cuando se descubrieron los rayos x
            #cuando se creo el internet
            #cuando se descubrieron los antibioticos
            #cuando se descubrio la electricidad
            elif soup.find('span', attrs={'class': 'e24Kjd'}):
                return str(soup.find('span', attrs={'class': 'e24Kjd'}).text)

        # #----------------------------------------------------------------------------

        # -------------------------------Busca Cantidades-------------------------------
        
        if tipo_pregunta == 'cantidad':
            cuadro = None
            
            #cuanto cuesta una mac
            if soup.find('div', attrs={'class': 'rwVHAc'}):
                return str(soup.find('div', attrs={'class': 'rwVHAc'}).text).replace('Amazon MX','')
            
            #cuanto vale un euro
            if soup.find('div', attrs={'class': 'dDoNo vk_bk gsrt'}):
                return str(soup.find('div', attrs={'class': 'dDoNo vk_bk gsrt'}).text)
            
            #cuantas calorias tiene una tortilla
            elif soup.find('div', attrs={'class': 'Z0LcW an_fna'}):
                return str(soup.find('div', attrs={'class': 'Z0LcW an_fna'}).text)
            
            #cuantos siglos duro la cultura mexica
            elif soup.find('span', attrs={'class': 'e24Kjd'}):
                return str(soup.find('span', attrs={'class': 'e24Kjd'}).text)
            
            #cuanto mide Ariana Grande
            elif soup.find('div', attrs={'class': 'Z0LcW'}):
                return str(soup.find('div', attrs={'class': 'Z0LcW'}).text)
            
            #cuanto pesa un oso polar
            elif soup.find('div', attrs={'class': 'title'}):
                return str(soup.find('div', attrs={'class': 'title'}).text)
            
            #cuantos habitantes tiene CDMX
            elif soup.find('div', attrs={'class': 'kpd-ans kno-fb-ctx KBXm4e'}):
                return str(soup.find('div', attrs={'class': 'kpd-ans kno-fb-ctx KBXm4e'}).text)
            
            #"cuantas millas son 5 km"  CONVERSIONES
            elif soup.find('div', attrs={'id': 'NotFQb'}):
                Texto = str(soup.find('div', attrs={'id': 'NotFQb'}).input).split('value=')[1]                
                return Texto.split('"')[1]
        # -----------------------------------------------------------------------------------------

        # ------------------------------Busca quien------------------------------------------------
        
        if tipo_pregunta == 'sujetos':
            cuadro = None
            
            #quien descubri el radio
            try:
                if re.search('(D|d)escubri(o|ó)', pregunta):
                    return str(soup.find('div', attrs={'class': 'LGOjhe'}).text)
            except:
                return 'por el momento no tengo la respuesta'

            #quien escribio el quijote
            if soup.find('div', attrs={'class': 'Z0LcW'}):
                return str(soup.find('div', attrs={'class': 'Z0LcW'}).text)
            
            #quien es el hombre mas rico del mundo
            if soup.find('div', attrs={'class': 'LGOjhe'}):
                return str(soup.find('div', attrs={'class': 'LGOjhe'}).text)
            
            #quien creo netflix
            try:
                if soup.find('div', attrs={'class': 'Z1hOCe'}):
                    busqueda1 = soup.find_all('div', attrs={'class': 'Z1hOCe'})
                    for j,i in enumerate(busqueda1):
                        if 'Fundadores' in i.text or 'Propietario' in i.text:
                            pivote=j
                            break

                    busqueda2 = busqueda1[pivote].find_all('a', attrs={'class': 'fl'})
                    nombres = [L.text for L in busqueda2]

                    if len(nombres)>1:
                        nombres[-1]= 'y '+nombres[-1]

                    return ' '.join(nombres)
            except:
                cuadro = None
            
            #quien canta  un mundo ideal
            if soup.find('span', attrs={'class': 'LrzXr kno-fv'}):
                return str(soup.find('span', attrs={'class': 'LrzXr kno-fv'}).text)
        # -----------------------------------------------------------------------------------------

        # ------------------------------Busca Lugar------------------------------------------------
        if tipo_pregunta == 'lugar':
            
            cuadro = None
            #
            if soup.find('div', attrs={'class': 'e24Kjd'}):
                return str(soup.find('div', attrs={'class': 'e24Kjd'}).text)
                        
            #donde nacio Luis miguel
            try:
                if soup.find('span', attrs={'class': 'w8qArf'}):
                    busqueda1 = soup.find_all('span', attrs={'class': 'w8qArf'})
                    for j,i in enumerate(busqueda1):
                        if 'Lugar' in i.text:
                            pivote=j
                            break
                    busqueda1 = soup.find_all('span', attrs={'class': 'LrzXr kno-fv'})

                    return busqueda1[pivote].text
            except:
                cuadro = None
                
            #donde nacio chabelo
            if soup.find('div', attrs={'class': 'Z0LcW'}):
                return str(soup.find('div', attrs={'class': 'Z0LcW'}).text)
            
            
            #donde vive el ajolote
            if soup.find('div', attrs={'class': 'LGOjhe'}):
                return str(soup.find('div', attrs={'class': 'LGOjhe'}).text)
    
        # -----------------------------------------------------------------------------------------

        # ------------------------------Busca Explicaciones----------------------------------------
        
        if tipo_pregunta == 'explicación':
            cuadro = None
            
            #que tal esta el clima en CDMX
            if re.search('clima (en|por|hoy)', pregunta):
                try:
                    print(soup.find('div', attrs={'class': "vk_gy vk_h"}).text)
                    clima = str((float(str(soup.find('span', attrs={'class': 'wob_t'}).text))))
                except:
                    return 'por el momento no puedo revisar esta informacion'
                return str(round(float(clima),1))+ ' celcius '+ str(soup.find('span', attrs={'id': 'wob_dc'}).text)
            
            #cual es la casa mas cercana
            try:
                if re.search('m(a|á)s? cerca(no)?', pregunta):
                    #return 'aqui de dejo un link: '+'https://www.google.com/maps/search/'+''+'/@20.6768517,-103.3562147,14.72z'
                    busqueda1 = soup.find('div', attrs={'class': 'AEprdc vk_c ihlL4d'})
                    return 'https://www.google.com.mx/'+str(busqueda1).replace('href="','"')
            except:
                return 'por ahora no cuento con esta funcion'
            #AEprdc vk_c ihlL4d
            if soup.find('div', attrs={'class': 'LGOjhe'}):
                #print('hay LGOjhe')
                return str(soup.find('div', attrs={'class': 'LGOjhe'}).text)

            #que es un ajolote definiciones
            if soup.find('div', attrs={'class': 'PZPZlf hb8SAc kno-fb-ctx'}):
                return str(soup.find('div', attrs={'class': 'PZPZlf hb8SAc kno-fb-ctx'}).text)
            
            #que comen los conejos
            
            #que hora es
            if soup.find('div', attrs={'class': 'gsrt vk_bk dDoNo'}):
                return str(soup.find('div', attrs={'class': 'gsrt vk_bk dDoNo'}).text)
            
            #que dia es hoy
            if soup.find('div', attrs={'class': 'vk_bk dDoNo'}):
                return str(soup.find('div', attrs={'class': 'vk_bk dDoNo'}).text)
            
            #que comen los hamsters
            if soup.find('div', attrs={'class': 'e24Kjd'}):
                return str(soup.find('div', attrs={'class': 'e24Kjd'}).text)
            
            #como cuidar el agua
            if soup.find('div', attrs={'class': 'RqBzHd'}):
                return str(soup.find('div', attrs={'class': 'RqBzHd'}).text)
            
            #por que murio benito juarez
            if soup.find('div', attrs={'class': 'Z0LcW'}):
                return str(soup.find('div', attrs={'class': 'Z0LcW'}).text)

        # -----------------------------------------------------------------------------------------
            
    def NumeroPalabras(self,frase):
        cont = 1
        for i in frase:
            if i == ' ':
                cont+=1
        return cont

    def Answers(self,texto,PalabrasClave):
        
        if len(texto)<100:
            RespuestaCorta=texto
            return (RespuestaCorta,0.01)
        
        doc = textacy.Doc(texto,lang='es_core_news_md')
        frecuencia_palabras = doc.to_bag_of_terms(ngrams=(1,2,3),named_entities=True,weighting='count',as_strings=True)
        frecuencia_maxima = max(frecuencia_palabras.values())

        for w in frecuencia_palabras.keys():
            frecuencia_palabras[w]=(frecuencia_palabras[w]/frecuencia_maxima)
        lista_oraciones = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', texto)

        lista_oraciones = [oracion for oracion in lista_oraciones if len(oracion)>= 45]

        puntuacion_oraciones={}
        for ora in lista_oraciones:
            for w in self.TokenizationL(ora):
                if w in frecuencia_palabras.keys() and w not in self.stopwords:
                    if ora not in puntuacion_oraciones.keys():
                        puntuacion_oraciones[ora]=frecuencia_palabras[w]
                    else:
                        if w in PalabrasClave:
                            puntuacion_oraciones[ora]+=(frecuencia_palabras[w])*10
                        else:
                            puntuacion_oraciones[ora]+=frecuencia_palabras[w]
            
        RespuestaCorta = sorted(puntuacion_oraciones.items(), key=operator.itemgetter(1),reverse=True)
        RespuestaCorta =[(i[0],i[1]/self.NumeroPalabras(i[0])) for i in RespuestaCorta]
        Puntuacion = sum ([i[1] for i in RespuestaCorta][:1])
        RespuestaCorta = ' '.join([i[0] for i in RespuestaCorta][:1])
        
        return (RespuestaCorta, Puntuacion)


    #@timeout(10,use_signals=False)
    def MainUser(self,Question):
        texto = self.ObtenerInformacion(Question)
        """if self.translator.detect(texto).lang == 'en':
            print('esto se manda a traducir',texto)
            texto = self.translate(texto)[0]"""
        return texto


if __name__ == '__main__':

    Q_A=ExtraccionRespuestas()
    pregunta = 'como esta el clima hoy'
    start=time.time()
    print(Q_A.MainUser(pregunta))
    print('esto tardo',time.time()-start)