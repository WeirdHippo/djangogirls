from django.http import JsonResponse
from django.shortcuts import render
from apiclient.discovery import build

# Create your views here.

DEVELOPER_KEY = "AIzaSyBSBMkFC_fyyGs1cVqubH26sb4OkkFyuD4"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def form_action(request):
    name =  request.POST['name']
    email = request.POST['email']
    comments = request.POST['comments']
    print(name, email, comments)

def search_name(keyword):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=3
    ).execute()

    return search_response


def search_word(keyword):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


    search_rep = youtube.search().list(
    q=keyword,
    part="id,snippet",
        maxResults=3
    ).execute()

    return search_rep

def search_api(request):
    a = request.POST['keyword']
    print(a)
    # request.post
    #search_name(a)
    return JsonResponse({ "word" : search_word(a) , "name" : search_name(a)})

def form(request):
    return  render(request, 'blog/form.html', {})

def post_list(request):
    return render(request, 'blog/index.html', {})