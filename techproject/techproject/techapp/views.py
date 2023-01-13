from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, "index.html")


def operation(request):
    x = int(request.POST['num1'])
    y = int(request.POST['num2'])
    add = x + y
    multi = x * y
    div = x/y
    sub = x-y

    res = {
        'addition': add,
        'multiplication': multi,
        'division': div,
        'subtraction': sub}

    return render(request, "result.html", {'result': res})
