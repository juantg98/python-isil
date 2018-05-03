from django.http import HttpResponse


def lis(request):

    nums= list(range(1, 101))
    
    return (HttpResponse(nums))