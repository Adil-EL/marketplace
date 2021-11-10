#automatic scrapping
from scrapers import pcmaroc_urls_collector, pcmaroc_item_crawler
from feed_db import Add_laptops

base_url_pcmaroc = "https://pcmaroc.com/12-pc-portable#"
base_url_ultra_pc = "https://www.ultrapc.ma/19-pc-portables"
base_url_avito = "https://www.avito.ma/fr/maroc/ordinateurs_portables-%C3%A0_vendre"
links = pcmaroc_urls_collector(base_url = base_url_pcmaroc)
laptops = []

for url in links:
    laptop = pcmaroc_item_crawler(url)
    laptops.append(laptop)
    

print("\n *******\n")

Add_laptops(laptops)

#-------------------------- To Do -------------------------------------
# 1 automatically update avito scrapp everyday

# from pymongo import MongoClient

# URI = "mongodb+srv://AdilLaptops:AdilLaptops@laptops.m72a4.mongodb.net/laptops"
# client =MongoClient(URI)
# db =client.laptops
# db.laptops.insert_one(laptop_document)