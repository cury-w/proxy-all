import requests
import re
import os

# 定义代理源
PROXY_SOURCES = {
    "http": [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http%2Chttps",
    ],
    "socks4": [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    ],
    "socks5": [
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    ]
}

def is_valid_proxy(proxy):
    # 过滤掉 0.0.0.0, 127.0.0.1 等无效 IP
    invalid_ips = ['0.0.0.0', '127.0.0.1', 'localhost']
    ip = proxy.split(':')[0]
    if ip in invalid_ips:
        return False
    # 简单的私有 IP 过滤 (可选，但通常代理不应该是私有 IP)
    if ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.16.'):
        return False
    return True

def fetch_proxies(url):
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            proxies = []
            # 处理 Geonode API 的 JSON 格式
            if "geonode.com" in url:
                data = response.json()
                for item in data.get('data', []):
                    proxies.append(f"{item['ip']}:{item['port']}")
            else:
                # 处理普通文本格式
                proxies = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', response.text)
            
            # 过滤无效代理
            return [p for p in proxies if is_valid_proxy(p)]
    except Exception as e:
        print(f"Error fetching from {url}: {e}")
    return []

def main():
    # 确保 proxy 目录存在
    if not os.path.exists("proxy"):
        os.makedirs("proxy")

    for proto, urls in PROXY_SOURCES.items():
        all_proxies = set()
        print(f"Fetching {proto} proxies...")
        for url in urls:
            proxies = fetch_proxies(url)
            all_proxies.update(proxies)
            print(f"  Fetched {len(proxies)} from {url}")
        
        # 保存到文件
        file_path = f"proxy/{proto}.txt"
        with open(file_path, "w") as f:
            f.write("\n".join(sorted(list(all_proxies))))
        print(f"Saved {len(all_proxies)} {proto} proxies to {file_path}")

if __name__ == "__main__":
    main()
