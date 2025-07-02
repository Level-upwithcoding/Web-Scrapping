# Importing all necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from time import sleep
import pandas as pd
# Creating dictionary to save our extracted data
movies = {
    "title": [],
    "year": [],
    "duration": [],
    "imdb": [],
    "genres": [],
    "director": [],
    "stars": [],
    "metascore": []
}
# Determine options, so we can open browser and have a vision what code really is doing
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.implicitly_wait(5)
driver.get("https://www.imdb.com/")

# Clicking and going on that page, where we can load all our data
search_button = driver.find_element(By.ID, "suggestion-search-button")
search_button.click()

sleep(2)

movies_tv = driver.find_element(By.CSS_SELECTOR, "a[data-testid = 'advanced-search-chip-tt']")
movies_tv.click()

sleep(2)

moviess = driver.find_element(By.CSS_SELECTOR, "button[data-testid='test-chip-id-movie']")
moviess.click()

driver.execute_script("document.body.style.zoom='50%'")
sleep(2)


release_date = driver.find_element(By.XPATH, "//div[text() = 'Release date']")
release_date.click()

release_date_from = driver.find_element(By.CSS_SELECTOR, "input[name = 'release-yearmonth-start-input']")
release_date_from.send_keys("2010-01")

release_date_to = driver.find_element(By.CSS_SELECTOR, "input[name = 'release-yearmonth-end-input']")
release_date_to.send_keys("2025-05")

sleep(1)

results = driver.find_element(By.CSS_SELECTOR, "button[data-testid = 'adv-search-get-results']")
results.click()
driver.execute_script("document.body.style.zoom='100%'")
# In this example, we try to load 2250 movie's element, each page has 50 element, so with the help of while loop first we will load whole page
page_count = 0
while page_count != 44:
    actions = ActionChains(driver)
    sleep(2)
    more_buttons = driver.find_element(By.CSS_SELECTOR, "span.ipc-see-more__text")
    actions.move_to_element(more_buttons).perform()
    more_buttons.click()
    page_count += 1
sleep(3)

# Saving all movie url's in one list
movies_url = driver.find_elements(By.CSS_SELECTOR, "a.ipc-title-link-wrapper")
movies_link = [x.get_attribute("href") for x in movies_url]
# Now it is not important, to open every movie's url repeatedly so we can work on the same browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# Creating for loop to go directly on every url and extract every necessary data from that page
counting = 0
for links in movies_link:
    driver.get(links)
    movie_title = driver.find_element(By.CSS_SELECTOR, "span.hero__primary-text").text
    movies["title"].append(movie_title)

    try:
        year = driver.find_element(By.XPATH, "//a[contains(@class, 'ipc-link--baseAlt') and contains(text(), '20')]").text
        movies["year"].append(year)
    except:
        year = "no info"
        movies["year"].append(year)
    try:
        duration = driver.find_element(By.XPATH, "//li[@class='ipc-inline-list__item'][contains(., 'h') or contains(., 'm')]").text
        movies["duration"].append(duration)
    except:
        duration = "no info"
        movies["duration"].append(duration)

    try:
        imdb = driver.find_element(By.CSS_SELECTOR, "span.sc-d541859f-1").text
        movies["imdb"].append(imdb)
    except:
        imdb = "no info"
        movies["imdb"].append(imdb)
    try:
        genres = ", ".join([x.text for x in driver.find_elements(By.CSS_SELECTOR, "span.ipc-chip__text")])
        movies["genres"].append(genres)
    except:
        genres = "no info"
        movies["genres"].append(genres)
    try:
        director = driver.find_element(By.CSS_SELECTOR, "a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link").text
        movies["director"].append(director)
    except:
        director = "no info"
        movies["director"].append(director)
    try:
        stars = ", ".join([x.text for x in driver.find_elements(By.CSS_SELECTOR, "a.ipc-metadata-list-item__list-content-item.ipc-metadata-list-item__list-content-item--link")[2:5]])
        movies["stars"].append(stars)
    except:
        stars = "no info"
        movies["stars"].append(stars)

    try:
        metascore = driver.find_element(By.CSS_SELECTOR, "span.sc-9fe7b0ef-0.hDuMnh.metacritic-score-box").text
        movies["metascore"].append(metascore)
    except:
        metascore = "no info"
        movies["metascore"].append(metascore)


    counting += 1
    print(counting)

# And last, we can save all scraped data to an excel file, with the help of pandas library
df = pd.DataFrame(movies)
df.to_excel("movies.xlsx")





