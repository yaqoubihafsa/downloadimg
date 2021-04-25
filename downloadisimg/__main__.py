import requests

def download(url, file_name):
    with open(file_name, 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

if __name__ == '__main__':
    download(url, file_name)
                