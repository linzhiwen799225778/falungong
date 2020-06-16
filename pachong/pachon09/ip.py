import requests
def check_ip(proxie):
    print(proxie)
    try:
        ip = [v.split(':')[1].lstrip('//') for k, v in proxie.items()][0]
        url = 'http://icanhazip.com/'
        # url = 'http://httpbin.org/ip'
        response = requests.get(url=url, proxies=proxie, timeout=5)
        # main_ip = requests.get(url=url)
        # print(main_ip.text)
        # print(response.text, ip)
        # if main_ip.text != response.text:

        # print(response.text)
        print(ip, response.text.strip())
        if ip == response.text.strip():
            return True
    except:
        pass
    return False