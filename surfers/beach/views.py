import json
from urllib.request import urlopen

from django.shortcuts import render


# Create your views here.
from .apikeys import *


def wave(request):

    with urlopen(
            "http://www.khoa.go.kr/oceangrid/grid/api/fcIndexOfType/search.do?ServiceKey="+khoa_key+"&Type=BE&ResultType=json") as url:
        sea_json_file = url.read()

    sea_json = json.loads(sea_json_file.decode('utf-8'))

    # print(sea_json['result']['data'][0],sea_json['result']['data'][1],)
    # print(json.dumps(sea_json['result']['data'], indent=4, ensure_ascii=False))

    # print(sea_json['result']['data'][0]['name'])
    # print(sea_json['result']['data'][0]['water_temp'])
    # print(sea_json['result']['data'][0]['wave_height'])

    # for x in sea_json['result']['data']:
    #     print(x['name'])
    #     print(x['date'], x['time_type'])
    #     print('수온 : ', x['water_temp'], '도')
    #     print('파도 : ', x['wave_height'], 'm')

    beach_info = []
    one_beach = []
    for i in range(len(sea_json['result']['data'])):
        one_beach.append(sea_json['result']['data'][i])
        temp_test = list(one_beach)

        if i % 6 == 5 or i == len(sea_json['result']['data']):
            beach_info.append(temp_test)
            one_beach.clear()

    context = {
        # 'beach': sea_json['result']['data']
        'beach': beach_info,
        'apikey': google_key
    }

    return render(request, 'beach/map.html', context)
