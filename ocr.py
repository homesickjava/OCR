from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID='19608290'
API_KEY='Lus16HEdFSoe3wPQArLu0UBu'
SECRET_KEY='HOC1jVgIjyQAAKpFam5aiDqrN1ozGlgG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """

filePath = "./pic/hc1.jpg"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filePath)

""" 调用通用文字识别, 图片参数为本地图片 """
#client.basicGeneral(image);

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
dict = client.basicGeneral(image, options)

for i in dict["words_result"]:
	print(str(i["words"]))

#url = "https//www.x.com/sample.jpg"

""" 调用通用文字识别, 图片参数为远程url图片 """
#client.basicGeneralUrl(url);

""" 如果有可选参数 """
'''
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
'''
""" 带参数调用通用文字识别, 图片参数为远程url图片 """
#client.basicGeneralUrl(url, options)