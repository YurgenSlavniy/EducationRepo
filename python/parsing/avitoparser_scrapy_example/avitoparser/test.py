import requests
import wget

url = 'https://www.ap22.ru/netcat_files/multifile/2546/90766/palms_3242342_960_720.jpg'
wget.download(url)

# response = requests.get(url)
#
# with open('palms.jpg', 'wb') as f:
#     f.write(response.content)
#
# response = requests.get(url, stream=True)
# handle = open(target_path, "wb")
# for chunk in response.iter_content(chunk_size=512):
#     if chunk:  # filter out keep-alive new chunks
#         handle.write(chunk)
