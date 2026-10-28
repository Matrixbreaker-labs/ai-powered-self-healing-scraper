import asyncio
import os
from playwright.async_api import async_playwright
from openai import OpenAI
from pydantic import BaseModel
from typing import List
import pandas as pd

# ==============================================================================
# 1. AI DATA SCHEMA SETUP
# ==============================================================================
class CourseInfo(BaseModel):
    title: str
    price: str
    rating: str

class ExtractedData(BaseModel):
    courses: List[CourseInfo]

# Initialize OpenAI Client (Make sure OPENAI_API_KEY environment variable is set)
client = OpenAI()

# ==============================================================================
# 2. AI DATA PIPELINE MODULE
# ==============================================================================
def parse_html_with_ai(html_content: str) -> ExtractedData:
    """Processes unstructured HTML or text via OpenAI Structured Outputs."""
    print("[AI MODULE] Processing raw web data with OpenAI Engine...")
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": "You are a specialized enterprise data extraction pipeline. Extract all course names, prices, and ratings from the provided raw web content into a clean structured format."
            },
            {"role": "user", "content": html_content}
        ],
        response_format=ExtractedData,
    )
    return response.choices.message.parsed

# ==============================================================================
# 3. EXPORT MODULE (Excel & CSV Saver Engine)
# ==============================================================================
def export_data_to_files(ai_data: ExtractedData, base_filename: str = "scraped_data"):
    """Transforms validated Pydantic objects into clean Excel and CSV files."""
    print(f"\n[EXPORT ENGINE] Normalizing data records into dataframes...")
    
    data_list = []
    for item in ai_data.courses:
        data_list.append({
            "Course Title": item.title,
            "Price": item.price,
            "Rating": item.rating
        })
    
    df = pd.DataFrame(data_list)
    
    if df.empty:
        print("[WARNING] Extraction matrix is empty. No files generated.")
        return

    # 1. Export Clean CSV
    csv_filename = f"{base_filename}.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    print(f"💾 [SUCCESS] Clean data written to CSV format: {csv_filename}")
    
    # 2. Export Auto-Formatted Excel Sheet
    excel_filename = f"{base_filename}.xlsx"
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Scraped Data')
        
        worksheet = writer.sheets['Scraped Data']
        for col in worksheet.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = col.column_letter
            worksheet.column_dimensions[col_letter].width = max(max_len + 3, 12)
            
    print(f"📊 [SUCCESS] Professional structural formatting applied to Excel: {excel_filename}")

# ==============================================================================
# 4. CORE PLAYWRIGHT SCRAPING ENGINE (Asynchronous Architecture)
# ==============================================================================
async def scrape_live_website(url: str):
    """Launches headless engine, extracts dynamic DOM strings and initializes pipelines."""
    print(f"[SCRAPER] Initializing headless browser engine for: {url}")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        try:
            await page.goto(url, wait_until="networkidle", timeout=30000)
            print("[SCRAPER] Dom trees and server traffic successfully mapped.")
            
            raw_body_text = await page.locator("body").inner_text()
            clean_raw_text = "\n".join([line.strip() for line in raw_body_text.split("\n") if line.strip()])
            
            await browser.close()
            print("[SCRAPER] Headless session terminated cleanly.")
            
            ai_result = parse_html_with_ai(clean_raw_text[:15000])
            export_data_to_files(ai_result, base_filename="production_scraped_output")
                
        except Exception as e:
            print(f"[CRITICAL ERROR] Scraping operation compromised: {e}")
            await browser.close()

if __name__ == "__main__":
    target_url = "https://www.scrapethissite.com/pages/"
    asyncio.run(scrape_live_website(target_url))
