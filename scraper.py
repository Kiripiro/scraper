import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import pandas as pd
import re

async def scrape_electric_vehicles(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        
        electric_vehicles_data = []

        while True:
            await page.wait_for_selector('li.ais-Hits-item.mod-w-4.mod-w-6-md.mod-w-12-sm.u-brad-sm.u-o-hidden.u-bc-neutral-light-max.u-relative')
            
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')

            vehicles = soup.find_all('li', class_='ais-Hits-item mod-w-4 mod-w-6-md mod-w-12-sm u-brad-sm u-o-hidden u-bc-neutral-light-max u-relative')
            print(f"Number of vehicles found on this page: {len(vehicles)}")

            for vehicle in vehicles:
                img_tag = vehicle.find('img', class_='lazy u-absolute u-w-100 u-h-100 u-fs-xs alt-caption lazy-transparent')
                img_src = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else 'N/A'

                brand_tag = vehicle.find('span', class_='my-text mod-uppercase')
                model_name_tag = vehicle.find('span', class_='my-text mod-ellipsis')
                brand = brand_tag.get_text(strip=True) if brand_tag else 'N/A'
                model_name = model_name_tag.get_text(strip=True) if model_name_tag else 'N/A'

                date_tag = vehicle.find('li', string=re.compile(r'\d{4}'))
                date = date_tag.get_text(strip=True) if date_tag else 'N/A'
                
                mileage_tag = vehicle.find('li', string=re.compile(r'\d{1,3}(,\d{3})*\s*km'))
                mileage = mileage_tag.get_text(strip=True) if mileage_tag else 'N/A'
                
                warranty_tag = vehicle.find('li', string=re.compile(r'Garantie \d{1,2} mois', re.IGNORECASE))
                warranty = warranty_tag.get_text(strip=True) if warranty_tag else 'N/A'

                electric_vehicles_data.append({
                    'Brand': brand,
                    'Model Name': model_name,
                    'Date': date,
                    'Mileage': mileage,
                    'Warranty': warranty,
                    'Image URL': img_src
                })

            next_button = soup.find('a', {'aria-label': 'Next'})
            if next_button and 'disabled' not in next_button.attrs:
                next_page_url = next_button['href']
                await page.goto(next_page_url)
            else:
                break

        df = pd.DataFrame(electric_vehicles_data)
        df.to_csv('electric_vehicles.csv', index=False)
        print("Data scraped successfully and saved to electric_vehicles.csv")

        await browser.close()

asyncio.run(scrape_electric_vehicles('https://www.bymycar.fr/rechercher-un-vehicule?prod_VEHICLES%5BrefinementList%5D%5Bfuel%5D%5B0%5D=Electrique&prod_VEHICLES%5BhitsPerPage%5D=24'))
