import bs4
import requests
import openpyxl

# creating excel sheet
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Rank', 'Movie Name', 'Year Of Release', 'IMDB Rating'])

# scrapping
try:
    source = requests.get('https://m.imdb.com/chart/top/')
    source.raise_for_status()
    soup = bs4.BeautifulSoup(source.text, 'html.parser')
    movies = soup.find('section', id='chart-content').find_all('div', class_='col-xs-12 col-md-6')

    for movie in movies:
        title_year_number = movie.find('h4').text.splitlines()
        rank = title_year_number[1]
        title = title_year_number[2]
        year = title_year_number[3]
        rating = movie.find('span', class_='imdb-rating').text
        print(rank, title, year, rating)
        sheet.append([rank, title, year, rating])

except Exception as e:
    print(e)

excel.save('IMDB Movie Ratings.xlsx')
