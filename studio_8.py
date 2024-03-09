import requests
import time
from bs4 import BeautifulSoup as bs

class Quote:
    def __init__(self, text, author, tags):
        self.text = text
        self.author = author
        self.tags = tags


def main():
    url = "https://quotes.toscrape.com/"
    r = requests.get(url)
    soup = bs(r.content, "html.parser")

    

    top_tags = []
    quotes = []
    while True:
        time.sleep(1)
        relative_url = get_next_url(soup)
        if relative_url is None:
            break
        next_page = url + relative_url


        r = requests.get(next_page)
        soup = bs(r.content, "html.parser")
        quotes.extend(scrape_quotes(soup))


        
        

        
    

    top_ten_tags(quotes)
    
    print("--------------------------------------")

    get_shortest_and_longest(quotes)

    print("--------------------------------------")

    authors_with_multiple_quotes(quotes)


    return



def scrape_quotes(soup: bs):
    quotes = soup.find_all("div", {"class": "quote"})

    quotes_list=[]

    for quote in quotes:

        

        text = quote.find("span", {"class": "text"}).get_text(strip=True)
        print(text)
        author = quote.find("small", {"class": "author"}).get_text(strip=True)
        print(author)
        

        tags = quote.find_all("a", {"class": "tag"})
        tags_text = []
        for tag in tags:
            tags_text.append(tag.get_text(strip=True))
            
        print(tags_text)
        

        quotes_list.append(Quote(text, author, tags_text))


        print("------------------------------------")

    return quotes_list

def get_next_url(soup: bs):
    list_item = soup.find("li", {"class": "next"})
    if list_item is None:
        return None
    anchor = list_item.find("a")
    url = anchor["href"]

    return url

def get_shortest_and_longest(quotes):

    longest = 0
    shortest = 100000

    longest_quotes = ""
    shortest_quote = ""

    for quote in quotes:
        if len(quote.text) > longest:
            longest = len(quote.text)
            longest_quote = quote.text
        
        if len(quote.text) < shortest:
            shortest = len(quote.text)
            shortest_quote = quote.text

    print("Answer #2 - Shortest Quote is," , shortest_quote, "with" , shortest, "characters.")
    print("--------------------------------------")
    print("Answer #3 - Longest Quote is," , longest_quote, "with" , longest, "characters.")


def top_ten_tags(quotes):
    

    print("Answer #1 -")

    all_tags = []
    every_tag = []
    #top_ten_tags=[]
    for quote in quotes:
        all_tags.append(quote.tags)
    
    for i in all_tags:
        for j in i:
            every_tag.append(j)


    x = 0
    instances_min = 2
    every_single_tag = list(set(every_tag))
    for i in every_single_tag:
        if i in every_tag:
            count_instances = every_tag.count(i)
            if x < 10:
                if count_instances > instances_min:
                    print(i, "appeared ", count_instances, "times")
                    x = x + 1
                if count_instances == 3:
                    instances_min = instances_min + 1
                if instances_min == 4:
                    instances_min = instances_min - 1



def authors_with_multiple_quotes(quotes):

    print("Answer #4 -")
    all_authors = []
    for quote in quotes:
        all_authors.append(quote.author)

    every_author = list(set(all_authors))
    for i in every_author:
        if i in all_authors:
            count_authors = all_authors.count(i)
            if count_authors > 2:
                print(i , "has ", count_authors, "quotes")

    



    return









if __name__ == "__main__":
    main()