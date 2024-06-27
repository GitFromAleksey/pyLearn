import json
import proxy_checking.proxy_checking


FILE = 'Free_Proxy_List.json'
# https://geonode.com/free-proxy-list
def ReadProxyFile(file_name: str):
    with open(file_name, 'r') as f:
        content = f.read()
        j_data = json.loads(content)
        return j_data
        # for j_item in j_data:
        #     print(j_item)
    return None

def main():
    proxy_list = ReadProxyFile(FILE)

    chckr = proxy_checking.ProxyChecker()

    for proxy in proxy_list:
        proxy_str = proxy['ip'] + ':' + proxy['port']
        print(f'Check: {proxy_str}, {proxy["city"]}')
        proxy_check_result = chckr.check_proxy(proxy_str)
        print(proxy_check_result)
        if proxy_check_result['status'] == True:
            good_proxy = {}
            good_proxy['ip_port'] = proxy['ip']
            good_proxy['port'] = proxy['port']
            good_proxy['time_response'] = proxy_check_result['time_response']
            good_proxy['type'] = proxy_check_result['type']
            good_proxy['country'] = proxy_check_result['country']
            good_proxy['city'] = proxy_check_result['city']
            with open('good_proxyes.txt', 'a+') as f:
                f.writelines(json.dumps(good_proxy) + '\n')
                f.close()


if __name__ == '__main__':
    main()
