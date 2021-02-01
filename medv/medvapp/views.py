from django.shortcuts import render
import numpy as np
from .apps import getPredictions


# our home page view
def home(request):    
    return render(request, 'index.html')

# our result page view
def result(request):
    CHAS = int(request.GET['CHAS'])
    RM = int(request.GET['RM'])
    LOG_NOX = np.log(int(request.GET['LOG_NOX']))
    LOG_DIS = np.log(int(request.GET['LOG_DIS']))
    LOG_LSTAT = np.log(int(request.GET['LOG_LSTAT']))

    result = getPredictions(CHAS, RM, LOG_NOX, LOG_DIS,LOG_LSTAT)

    return render(request, 'result.html', {'result':result})
