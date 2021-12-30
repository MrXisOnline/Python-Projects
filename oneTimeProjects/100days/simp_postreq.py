import requests

USERNAME = "mrxonline"
TOKEN = "9647F9B27F52E8A2"
url = "https://pixe.la/v1/users"
# para = {
#     "token": "9647F9B27F52E8A2",
#     "username": "mrxonline",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=url,json=para)
# print(response.text)
#
# graph_url = f"{url}/{USERNAME}/graphs"
# graph_header = {
#     "X-USER-TOKEN":TOKEN
# }
# graph_para = {
#     "id": "graph1",
#     "name": "Coding Tracker",
#     "unit": "Hour",
#     "type": "float",
#     "color": "momiji"
# }
# response = requests.post(url=graph_url,json=graph_para,headers=graph_header)
# print(response)
# pix_url = f"{url}/{USERNAME}/graphs/graph1"
# header = {
#     "X-USER-TOKEN":TOKEN
# }
# pixel_para = {
#     "date":"20210315",
#     "quantity": "15"
# }
# response = requests.post(url=pix_url,headers=header,json=pixel_para)
# print(response.text)
# pix_url = f"{url}/{USERNAME}/graphs/graph1/20210314"
# header = {
#     "X-USER-TOKEN":TOKEN
# }
# pixel_para = {
#     "quantity": "4.5"
# }
# response = requests.put(url=pix_url,headers=header,json=pixel_para)
# print(response.text)
pix_url = f"{url}/{USERNAME}/graphs/graph1/20210315"
header = {
    "X-USER-TOKEN":TOKEN
}
response = requests.delete(url=pix_url,headers=header)
print(response.text)
