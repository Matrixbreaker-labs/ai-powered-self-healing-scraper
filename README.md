🤖 AI-Powered Self-Healing Web Scraper & Intelligent Data Pipeline
A production-grade, asynchronous web scraping architecture built with Python, Playwright, and OpenAI's Structured Outputs (GPT-4o-mini). This system bypasses traditional, fragile CSS/XPath selector methods by leveraging AI to extract clean, validated data from dynamic, JavaScript-heavy websites and exports it into professionally formatted Excel and CSV sheets.
---
⚡ Core Architectural Superiorities
Selector-Free Extraction: Eliminates fragile extraction logic. Raw, unformatted web payloads are fed into a deterministic AI engine using Pydantic schemas.
Asynchronous Processing: Powered by Python's `asyncio` and `Playwright` browser context routines to handle dynamic JS rendering efficiently.
Anti-Bot Resiliency: Hardened with custom User-Agent spoofing, optimized request headers, and advanced `networkidle` state tracking to bypass strict anti-scraping firewalls.
Production-Grade Exporter: Converts raw text strings into structurally isolated data structures using Pandas, featuring automatic column-width calculation and UTF-8-sig encoding compatibility.
---
🛠️ System Components
The application is architected into 4 clean, modular pipelines:
```
[Target URL] ➡️ [Playwright Engine (Async/Headless)] ➡️ [Raw DOM/Text Payload]
                                                                ⬇️
[Formatted Excel / CSV] ⬅️ [Pandas Formatting Engine] ⬅️ [OpenAI Structured Validation]
```
Playwright Scraper Engine: Launches clean browser contexts to scrape asynchronous scripts.
AI JSON Parsing Pipeline: Directs unstructured data layouts into rigorous structural parameters using type-safe parsing models.
Dataframe Isolation Module: Sanitizes and logs structural nodes into unified data matrices.
Auto-Formatting Export Gateway: Outputs human-readable file sheets equipped with native text padding logic.
---
🚀 Setup & Execution
Prerequisites
Ensure you have Python 3.10+ installed on your local environment.
1. Installation
Clone the repository and install the production dependencies along with the core Chromium browser packages:
```bash
git clone https://github.com/YOUR_USERNAME/ai-powered-scraper.git
cd ai-powered-scraper
pip install playwright openai pydantic pandas openpyxl
playwright install chromium
```
2. Configure Environment Locks
Create a secure configuration environment or plug your authentication token directly into your runtime execution setup:
```bash
export OPENAI_API_KEY="your-actual-production-openai-api-key"
```
3. Initialize Engine Run
Execute the main application pipeline script:
```bash
python main.py
```
---
📊 Sample Outputs
Raw Source Fragment
```html
<div class='product-card'>
    <h2 class='title-xyz'>Advanced Python Algorithmic Trading Course</h2>
    <span class='old-price'>\$499</span>
    <span class='current-promo-price'>\$199.99</span>
    <p class='rating-stars'>4.8 out of 5 stars</p>
</div>
```
AI-Extracted Production Sheet Structure
The system completely normalizes unaligned web items into pristine tables:
Course Title	Price	Rating
Advanced Python Algorithmic Trading Course	$199.99	4.8 / 5
---
🛡️ Exception Safeguards
API Rate Limit Protection: Built-in auto-throttling mechanisms prevent server-side request choking.
Encoding Safety Locks: Employs `utf-8-sig` writing paradigms to preserve native localized currency codes (`$`, `€`, `£`) without rendering corruption.
Memory Leak Containment: Automatically caps text context sizes up to 15,000 characters to optimize processing expenses.
---
Developed by a Professional AI & Automation System Architect.
