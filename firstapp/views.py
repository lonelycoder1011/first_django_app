from django.http import HttpResponse
from datetime import date

def home(request):
    # Create a simple html page as a string
    template = "<html>" \
                "This is your first view" \
               "</html>"
    # Return the template as content argument in HTTP response
    return HttpResponse(content=template)

def index(request):
    return HttpResponse("Hello, world! This is the index page.")

def get_date(request):
    today = date.today()
    template = f"<html>Today's date is {today}</html>"
    return HttpResponse(content=template)

# def get_date(request):
#     today = date.today()
#     template = "<html>" \
#                 "Today's date is {}" \
#                "</html>".format(today)
#     return HttpResponse(content=template)