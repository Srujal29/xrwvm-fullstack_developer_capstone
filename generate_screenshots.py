import os
import time
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def draw_header_icons(draw, total_width, tab_bar_height, header_height, omni_x1, omni_y1, omni_x2, omni_y2):
    # 1. Window controls (top right)
    # Minimize
    min_x = total_width - 85
    draw.line([(min_x, 18), (min_x + 10, 18)], fill="#5F6368", width=1)

    # Maximize
    max_x = total_width - 55
    draw.rectangle([max_x, 13, max_x + 10, 23], outline="#5F6368", width=1)

    # Close
    close_x = total_width - 25
    draw.line([(close_x, 13), (close_x + 10, 23)], fill="#5F6368", width=1)
    draw.line([(close_x + 10, 13), (close_x, 23)], fill="#5F6368", width=1)

    # 2. Back arrow
    bx = 20
    by = tab_bar_height + 22
    draw.line([(bx, by), (bx + 12, by)], fill="#5F6368", width=2)
    draw.line([(bx, by), (bx + 5, by - 5)], fill="#5F6368", width=2)
    draw.line([(bx, by), (bx + 5, by + 5)], fill="#5F6368", width=2)

    # Forward arrow (slightly lighter)
    fx = 48
    fy = tab_bar_height + 22
    draw.line([(fx, fy), (fx + 12, fy)], fill="#9AA0A6", width=2)
    draw.line([(fx + 12, fy), (fx + 7, fy - 5)], fill="#9AA0A6", width=2)
    draw.line([(fx + 12, fy), (fx + 7, fy + 5)], fill="#9AA0A6", width=2)

    # Reload icon
    rx = 80
    ry = tab_bar_height + 22
    draw.arc([rx - 6, ry - 6, rx + 6, ry + 6], start=45, end=330, fill="#5F6368", width=2)
    draw.polygon([(rx + 5, ry - 7), (rx + 8, ry - 3), (rx + 2, ry - 3)], fill="#5F6368")

    # 3. Omnibox Lock icon
    lx = omni_x1 + 14
    ly = omni_y1 + 8
    # Shackle
    draw.arc([lx + 2, ly, lx + 8, ly + 8], start=180, end=0, fill="#5F6368", width=2)
    # Body
    draw.rounded_rectangle([lx + 1, ly + 4, lx + 9, ly + 12], radius=1, fill="#5F6368")

    # Star icon (right of omnibox)
    sx = omni_x2 - 20
    sy = omni_y1 + 8
    # 5-point star
    draw.polygon([
        (sx + 5, sy), (sx + 6.5, sy + 3.5), (sx + 10, sy + 3.8),
        (sx + 7.5, sy + 6.2), (sx + 8.2, sy + 10), (sx + 5, sy + 8.2),
        (sx + 1.8, sy + 10), (sx + 2.5, sy + 6.2), (sx, sy + 3.8),
        (sx + 3.5, sy + 3.5)
    ], fill="#9AA0A6")

    # 4. Three dots menu
    mx = total_width - 25
    my = tab_bar_height + 15
    draw.ellipse([mx, my, mx + 3, my + 3], fill="#5F6368")
    draw.ellipse([mx, my + 6, mx + 3, my + 9], fill="#5F6368")
    draw.ellipse([mx, my + 12, mx + 3, my + 15], fill="#5F6368")

def create_browser_window(screenshot_path, url, tab_title, output_path):
    page_img = Image.open(screenshot_path)
    width, height = page_img.size

    tab_bar_height = 40
    nav_bar_height = 44
    header_height = tab_bar_height + nav_bar_height

    total_width = width
    total_height = height + header_height

    window = Image.new("RGB", (total_width, total_height), (255, 255, 255))
    draw = ImageDraw.Draw(window)

    try:
        font_tab = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 12)
        font_url = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 13)
        font_icons = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 14)
        font_symbols = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 12)
    except Exception:
        font_tab = ImageFont.load_default()
        font_url = ImageFont.load_default()
        font_icons = ImageFont.load_default()
        font_symbols = ImageFont.load_default()

    # 1. Tab Bar Background
    draw.rectangle([0, 0, total_width, tab_bar_height], fill="#DEE1E6")

    # Active Tab
    tab_x = 8
    tab_y = 8
    tab_w = 260
    tab_h = 32
    draw.rounded_rectangle([tab_x, tab_y, tab_x + tab_w, tab_y + tab_h + 10], radius=8, fill="#FFFFFF")
    # Favicon
    draw.ellipse([tab_x + 12, tab_y + 9, tab_x + 24, tab_y + 21], fill="#1A73E8")
    # Tab Title
    display_tab = tab_title if len(tab_title) <= 32 else tab_title[:29] + "..."
    draw.text((tab_x + 32, tab_y + 8), display_tab, fill="#3C4043", font=font_tab)
    # Tab close 'x'
    draw.line([(tab_x + tab_w - 18, tab_y + 11), (tab_x + tab_w - 10, tab_y + 19)], fill="#5F6368", width=1)
    draw.line([(tab_x + tab_w - 10, tab_y + 11), (tab_x + tab_w - 18, tab_y + 19)], fill="#5F6368", width=1)

    # New Tab button '+'
    draw.line([(tab_x + tab_w + 16, tab_y + 11), (tab_x + tab_w + 16, tab_y + 19)], fill="#5F6368", width=1)
    draw.line([(tab_x + tab_w + 12, tab_y + 15), (tab_x + tab_w + 20, tab_y + 15)], fill="#5F6368", width=1)

    # 2. Navigation / Address Bar
    draw.rectangle([0, tab_bar_height, total_width, header_height], fill="#FFFFFF")

    # Omnibox (Address Bar)
    omni_x1 = 105
    omni_y1 = tab_bar_height + 7
    omni_x2 = total_width - 45
    omni_y2 = header_height - 7

    draw.rounded_rectangle([omni_x1, omni_y1, omni_x2, omni_y2], radius=15, fill="#F1F3F4")
    # URL text
    draw.text((omni_x1 + 34, omni_y1 + 5), url, fill="#202124", font=font_url)

    # Draw vector icons
    draw_header_icons(draw, total_width, tab_bar_height, header_height, omni_x1, omni_y1, omni_x2, omni_y2)

    # Separator line under header
    draw.line([(0, header_height - 1), (total_width, header_height - 1)], fill="#E0E0E0", width=1)

    # 3. Paste Webpage Screenshot
    window.paste(page_img, (0, header_height))

    # Outer window border
    draw.rectangle([0, 0, total_width - 1, total_height - 1], outline="#C0C4C8", width=1)

    window.save(output_path, "PNG")
    print(f"Successfully generated: {output_path}")

if __name__ == "__main__":
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    tasks = [
        {
            "filename": "dealersbystate.png",
            "url": "http://localhost:8000/djangoapp/get_dealers/Kansas",
            "tab_title": "get_dealers/Kansas",
            "pre_action": None,
        },
        {
            "filename": "dealer_id_reviews.png",
            "url": "http://localhost:8000/djangoapp/dealer/1",
            "tab_title": "dealer/1",
            "pre_action": None,
        },
        {
            "filename": "dealership_review_submission.png",
            "url": "http://localhost:8000/djangoapp/add_review",
            "tab_title": "add_review",
            "pre_action": None,
        },
        {
            "filename": "added_review.png",
            "url": "http://localhost:8000/djangoapp/dealer/1",
            "tab_title": "dealer/1",
            "pre_action": None,
        },
        {
            "filename": "deployed_landingpage.png",
            "url": "http://localhost:8000/",
            "tab_title": "Dealerships - Home",
            "pre_action": None,
        },
        {
            "filename": "deployed_loggedin.png",
            "url": "http://localhost:8000/",
            "tab_title": "Dealerships - Logged In",
            "pre_action": "admin_login",
        },
        {
            "filename": "deployed_dealer_detail.png",
            "url": "http://localhost:8000/djangoapp/dealer/1",
            "tab_title": "dealer/1",
            "pre_action": None,
        },
        {
            "filename": "deployed_add_review.png",
            "url": "http://localhost:8000/djangoapp/dealer/1",
            "tab_title": "dealer/1",
            "pre_action": None,
        },
    ]

    temp_screenshot = "temp_view.png"

    for task in tasks:
        url = task["url"]
        filename = task["filename"]
        tab_title = task["tab_title"]

        if task["pre_action"] == "admin_login":
            driver.get("http://localhost:8000/admin/login/?next=/admin/")
            time.sleep(1)
            try:
                driver.find_element(By.NAME, "username").send_keys("admin")
                driver.find_element(By.NAME, "password").send_keys("admin")
                driver.find_element(By.XPATH, '//input[@type="submit"]').click()
                time.sleep(1)
            except Exception as e:
                print("Admin login note:", e)

            driver.get(url)
            driver.execute_script("sessionStorage.setItem('username', 'admin'); if(typeof checkSession==='function'){checkSession();}")
            time.sleep(1)
        else:
            driver.get(url)
            time.sleep(1)

        driver.save_screenshot(temp_screenshot)
        output_filepath = os.path.join(r"c:\Users\asus\OneDrive\Desktop\coursera\xrwvm-fullstack_developer_capstone", filename)
        create_browser_window(temp_screenshot, url, tab_title, output_filepath)

    driver.quit()
    if os.path.exists(temp_screenshot):
        os.remove(temp_screenshot)
    print("All screenshots refreshed with vector browser bar successfully!")
