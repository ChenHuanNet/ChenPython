import Models.MyResult
from django.http import JsonResponse


def submitform(request):
    # f = Models.MyResult.ApiResult()
    # f.code = 0
    # # 实体转成Dict对象 但是__init__初始化赋值会失效
    # dic = dict((name, getattr(f, name)) for name in dir(f) if not name.startswith('__'))
    # print(dic)

    if request.method != "POST":
        myresult = {}
        myresult['code'] = -1
        myresult['message'] = '请使用POST请求'
        return JsonResponse(myresult, json_dumps_params={'ensure_ascii': False})

    realname = '空'
    birthday = '空'
    if 'realname' in request.POST:
        realname = request.POST['realname']
    if 'birthday' in request.POST:
        birthday = request.POST['birthday']

    myresult = {}
    myresult['code'] = 0
    myresult['message'] = realname + ',' + birthday
    myresult['data'] = [{"realname": realname, "birthday": birthday}]

    # JsonResponse  默认仅支持Dict 参数输出
    return JsonResponse(myresult, json_dumps_params={'ensure_ascii': False})


def submitGetList(request):
    print(request.method)
    if request.method != "GET":
        myresult = {}
        myresult['code'] = -1
        myresult['message'] = '请使用GET请求'
        return JsonResponse(myresult, json_dumps_params={'ensure_ascii': False})

    realname = 123
    birthday = 456
    myresult = {}
    myresult['code'] = 0
    myresult['message'] = '提交成功'
    myresult['data'] = [{"realname": realname, "birthday": birthday}]

    # JsonResponse  默认仅支持Dict 参数输出
    return JsonResponse(myresult, json_dumps_params={'ensure_ascii': False})
