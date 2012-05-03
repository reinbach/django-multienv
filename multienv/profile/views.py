from core.shortcuts import request_to_response

#---------------------------------------------------------------------------
def admin_list(request):
    return render_to_response(request, 'index.html')
