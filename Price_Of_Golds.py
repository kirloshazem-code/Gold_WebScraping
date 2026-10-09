import requests
from bs4 import BeautifulSoup
import csv
import time


gold_details = []
link = "https://market.isagha.com/prices"
def main_code():
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "html.parser")
    
    Golds = soup.find_all("div",{"class": "desktop-table"})    
    for i in Golds:
        table = i.find("table")
        rows = table.find("tbody").find_all("tr")
        
        for row in rows:
            columns = row.find_all("td")
            
            if len(columns) >= 4:
                guage = columns[0].get_text(strip=True)
                sell_price = columns[1].get_text(strip=True)
                buy_price = columns[3].get_text(strip=True)
                
                gold_details.append({
                    'guage': guage, 
                    'sell_price': sell_price,
                    'buy_price': buy_price
                })
                
                
                
def save_to_csv(data):
    with open("D:/gold_prices.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Guage", "Sell Price", "Buy Price"])

        # Data
        writer.writerows(data)

    print("Data saved successfully to gold_prices.csv")
    
    
# تشغيل البرنامج كل ساعة
while True:
    print("Getting latest gold prices...")

    main_code()

    print("Waiting 1 hour for the next update...\n")

    time.sleep(3600)


main_code()
save_to_csv([[item['guage'], item['sell_price'], item['buy_price']] for item in gold_details])