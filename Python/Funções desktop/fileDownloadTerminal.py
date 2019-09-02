import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    tamanho = r.headers.get('Content-Length')
    print(tamanho)
    dl=0
    cont=0
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                dl += len(chunk)
                f.write(chunk)
                done = (dl*100)/int(tamanho)
                if(done>cont):
                  cont+=1
                  print("%d porcent" %done)
             else:
                print("100 porcent")     
    return local_filename

download_file("Link file")