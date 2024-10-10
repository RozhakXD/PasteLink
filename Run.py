from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import sys
import random
from time import sleep

COLORS = {
    'KUNING': '\x1b[1;93m',
    'PUTIH': '\x1b[1;97m',
    'HIJAU': '\x1b[1;92m',
    'MERAH': '\x1b[1;91m',
    'RESET': '\x1b[0m'
}

def Agen_Pengguna_Acak(platform: str):
    major_version = random.randint(70, 120)
    build_number = random.randint(0, 9999)
    patch_number = random.randint(0, 9999)
    safari_versions = random.choice([533, 534, 535, 536, 537, 538])
    if platform != 'Android':
        windows_versions = random.choice(
            [
                "Windows NT 10.0; Win64; x64",
                "Windows NT 10.0; WOW64",
                "Windows NT 6.3; Win64; x64",
                "Windows NT 6.3; WOW64",
                "Windows NT 6.2; Win64; x64",
                "Windows NT 6.2; WOW64",
                "Windows NT 6.1; Win64; x64",
                "Windows NT 6.1; WOW64",
                "Windows NT 5.1; Win64; x64",
                "Windows NT 5.1; WOW64"
            ]
        )
        return (f'Mozilla/5.0 ({windows_versions}) AppleWebKit/{safari_versions}.36 (KHTML, like Gecko) Chrome/{major_version}.0.{build_number}.{patch_number} Safari/{safari_versions}.36')
    else:
        android_versions = random.choice(
            [
                "14", "13", "12", "11", "10", "9", "8.1", "8.0", "7.1", "7.0"
            ]
        )
        builds = random.choice(
            [
                "UP1A.231005.007", "RP1A.201005.004", "QP1A.190711.020", 
                "RP1A.200720.013", "UPB1.190623.012"
            ]
        )
        devices = random.choice([
                "Samsung Galaxy S21", "Samsung Galaxy Note 20",
                "OnePlus 9", "Xiaomi Mi 11", "Huawei P40", "Oppo Find X3",
                "SM-S918B", "Pixel 7", "Nexus 6P", "Pixel 4a"
            ]
        ) # Tambahkan Device Model Lain Agar Mengurangi Resiko Perangkat Yang Sama!
        return (f'Mozilla/5.0 (Linux; Android {android_versions}; {devices} Build/{builds}; wv) AppleWebKit/{safari_versions}.36 (KHTML, like Gecko) Version/4.0 Chrome/{major_version}.0.{build_number}.{patch_number} Mobile Safari/{safari_versions}.36')

def Kirimkan_Permintaan(url: str):
    try:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Host": "pastelink.net",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Site": "none",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "{}".format(Agen_Pengguna_Acak(platform=random.choice(['Windows', 'Android']))),
        }
        response = requests.get(url=url, headers=headers, verify=True, allow_redirects=True)
        if response.status_code == 200:
            return ('success')
        else:
            return ('failed')
    except (requests.exceptions.RequestException) as e:
        return ('error')

def Spam_Permintaan(url: str, num_requests: int, max_workers: int):
    status_counts = {'success': 0, 'failed': 0, 'error': 0}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(Kirimkan_Permintaan, url) for _ in range(num_requests)]
        for future in as_completed(futures):

            results = future.result()
            status_counts[results] = status_counts.get(results, 0) + 1

            print(f"{COLORS['PUTIH']}[{COLORS['HIJAU']}*{COLORS['PUTIH']}] Success:{COLORS['HIJAU']} {status_counts['success']}{COLORS['PUTIH']}, Failed:{COLORS['KUNING']} {status_counts['failed']}{COLORS['PUTIH']}, Error:{COLORS['MERAH']} {status_counts['error']}{COLORS['RESET']}     ", end='\r')
            sleep(1.0)

    print(f"{COLORS['PUTIH']}[{COLORS['HIJAU']}*{COLORS['PUTIH']}] Success:{COLORS['HIJAU']} {status_counts['success']}{COLORS['PUTIH']}, Failed:{COLORS['KUNING']} {status_counts['failed']}{COLORS['PUTIH']}, Error:{COLORS['MERAH']} {status_counts['error']}{COLORS['RESET']}     ")
    print(f"\n{COLORS['PUTIH']}Ringkasan:{COLORS['RESET']}                                    ")
    print(f"{COLORS['PUTIH']}[{COLORS['HIJAU']}*{COLORS['PUTIH']}] Tampilan Sukses:{COLORS['HIJAU']} {status_counts['success']}{COLORS['RESET']}")
    print(f"{COLORS['PUTIH']}[{COLORS['HIJAU']}*{COLORS['PUTIH']}] Tampilan Gagal:{COLORS['KUNING']} {status_counts['failed']}{COLORS['RESET']}")
    print(f"{COLORS['PUTIH']}[{COLORS['MERAH']}!{COLORS['PUTIH']}] Permintaan Error:{COLORS['MERAH']} {status_counts['error']}{COLORS['RESET']}")

    return ('null')

if __name__=='__main__':
    print(r"""{}______         _       _     _       _    
| ___ \       | |     | |   (_)     | |   
| |_/ /_ _ ___| |_ ___| |    _ _ __ | | __
|  __/ _` / __| __/ _ \ |   | | '_ \| |/ /
| | | (_| \__ \ ||  __/ |___| | | | |   < 
{}\_|  \__,_|___/\__\___\_____/_|_| |_|_|\_\ v1.5.0{}
""".format(COLORS['MERAH'], COLORS['PUTIH'], COLORS['RESET'])) # Coded by Rozhak
    tautan = input(f"{COLORS['PUTIH']}[{COLORS['HIJAU']}?{COLORS['PUTIH']}] Tautan:{COLORS['HIJAU']} ")
    if tautan.startswith('https://pastelink.net') == True:
        num_requests = int(input(f"{COLORS['PUTIH']}[{COLORS['HIJAU']}?{COLORS['PUTIH']}] Jumlah Permintaan:{COLORS['MERAH']} "))
        print("")
        Spam_Permintaan(url=tautan, num_requests=num_requests, max_workers=10)
        sys.exit(1)
    else:
        print(f"\n{COLORS['PUTIH']}[{COLORS['MERAH']}?{COLORS['PUTIH']}]{COLORS['MERAH']} Tautan Salah!{COLORS['RESET']}")
        sys.exit(0)
# Tampilan: 597
# Example: https://pastelink.net/gyvotcyb