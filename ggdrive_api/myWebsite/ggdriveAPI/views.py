# Google import
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Django import
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from ggdriveAPI.models import About
from ggdriveAPI.serializers import AboutSerializer

resources = [
    'About',
    'Changes',
    'Channels',
    'Comments',
    'Files',
    'Permissions',
    'Replies',
    'Revisions',
    'Teamdrives'
]

API_name = 'drive'
API_version = 'v3'

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Create your views here.
def index(request):
    return render(request, 'ggdriveAPI/index.html', {'resources': resources})

def about(request):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build(API_name, API_version, credentials=creds)

    # Call the Drive v3 API
    results = service.about().get(fields='kind, user').execute()
    
    if results:
        about_content = About(contents=Response(results).data)
        about_content.save()
        serializer = AboutSerializer(about_content)
        return JsonResponse(serializer.data, safe=False)
        # print(serializer.data)
        # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        # print(serializer.is_valid())
        # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

def changes(request):
    return HttpResponse('Changes Page')

def channels(request):
    return HttpResponse('Channels Page')

def comments(request):
    return HttpResponse('Comments Page')

def files(request):
    return HttpResponse('Files Page')

def permissions(request):
    return HttpResponse('Permissions Page')

def replies(request):
    return HttpResponse('Replies Page')

def revisions(request):
    return HttpResponse('Revisions Page')

def teamdrives(request):
    return HttpResponse('Teamdrives Page')
