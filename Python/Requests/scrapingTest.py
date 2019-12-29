import requests
from bs4 import BeautifulSoup

class Orient:
  
  def getMovies():
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    link = "link"

    req = requests.get(link, headers=headers)
    if req.status_code == 200:
      print('Requisição bem sucedida!')
      content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    rangeFilms = soup.find(name='li', attrs={'id': 'semat'}).get_text()
    films = soup.find_all(name='div', attrs={'class': 'sh-horarios'})
    for film in films:
      try:
        dataFilm={}
        dataFilm['nameFilm'] = film.h2.get_text()

        if('3d' in str(film.img['src'])):
          dataFilm['3d'] = True
          data = film.find_all(name='div', attrs={'class': 'sh-legs'})
          film.img['src'] = str(data)

        if('nacional' in str(film.img['src'])):
          dataFilm['typeExibition'] = 'Nacional'
        elif('dublado' in str(film.img['src'])):
          dataFilm['typeExibition'] = 'Dublado'
        elif('legendado' in str(film.img['src'])):
          dataFilm['typeExibition'] = 'Legendado'

        dataFilm['room'] = (film.span.get_text()).split("-")[0]
        dataFilm['room'] = dataFilm['room'][:len(dataFilm['room'])-1]

        try:
          dataFilm['hour'] = (film.span.get_text()).split("-")[2]
        except:
          dataFilm['hour'] = (film.span.get_text()).split("-")[1]
        if('A' in dataFilm['hour']):
          dataFilm['day'] = 'Somente Quarta'
          dataFilm['hour'] = dataFilm['hour'].replace("A","")
        elif('B' in dataFilm['hour']):
          dataFilm['day'] = 'Exceto Quarta'
          dataFilm['hour'] = dataFilm['hour'].replace("B","")

        dataFilm['hour'] = dataFilm['hour'].replace(" ","")

        print(dataFilm)    
      except Exception as e:
        if("'NoneType' object is not subscriptable" in str(e)):
          pass
        else:
          print(e)


Orient.getMovies()
