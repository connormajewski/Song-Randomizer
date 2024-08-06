from googleapiclient.discovery import build
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Song
from random import randint

def index(request):

    flag = False

    if request.GET.get('arg') is not None:
        flag = True

    # Set session variables to be used by POST and GET requests inside of index().

    layout_changed = request.session.get('layout_changed', False)
    song_added = request.session.get('song_added', False)
    video_list = request.session.get('video_list', [])
    song_success = request.session.get('song_success', False)
    song_found = request.session.get('song_found', False)

    request.session['video_list'] = []
    request.session['song_added'] = False
    request.session['song_success'] = False
    request.session['song_found'] = False

    videos = []

    if request.method == "POST":

        request.session['layout_changed'] = True

        # If user is adding a song, check that addSong() returns correctly, then update appropriate flags and redirect.

        if request.POST.get("songData"):

            if addSong(request.session['videoId'], request.session['videoTitle'], request.session['videoArtist']) == 0:

                request.session['song_success'] = True

            request.session['song_added'] = True

        else:

            # Create Youtube API, limit search results to top result.

            search_request = request.POST['searchQuery']

            youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

            search = youtube.search().list(

                q=search_request,
                part='id,snippet',
                maxResults=1,

            ).execute()

            # Filter through returned data, adding video data to video array only if it is categorized as music or a music video.

            for element in search.get('items', []):

                if element['id']['kind'] == 'youtube#video':

                    video_id = element['id']['videoId']

                    video_details_response = youtube.videos().list(
                        part='snippet',
                        id=video_id
                    ).execute()

                    for video in video_details_response.get('items', []):

                        category_id = video['snippet']['categoryId']

                        if category_id == '10':
                            videos.append(element)

            # If the length of videos is > 0, it means the search was successful. Set flag to indicate success, and add video information to session variables.

            if len(videos) > 0:

                for video in videos:

                    request.session['song_found'] = True

                    request.session['video_list'] += [[video['snippet']['title'], video['snippet']['channelTitle'], video['id']['videoId']]]

                    request.session['videoId'] = video_id
                    request.session['videoTitle'] = video['snippet']['title']
                    request.session['videoArtist'] = video['snippet']['channelTitle']

        # If POST request, redirect back to same webpage. This creates the appearance that all user actions occur on a single page.

        return redirect(index)

    # All requests fall down to this segment. This sets the variables to be passed through to the HTML page, which determines its layout.

    request.session['layout_changed'] = False

    context = {
        "layout_changed": layout_changed,
        "video_list": video_list,
        "flag": flag,
        "song_added": song_added,
        "random_song": getRandomSong(Song),
        "song_success": song_success,
        "song_found": song_found
    }

    return HttpResponse(render(request, "song_site/index.html", context))

# Function to add a song to the Song database. Used when POST request is sent with appropriate flag.

def addSong(songId, songName, songArtist):

    try:
        Song.objects.create(name = songName, artist=songArtist, songId = songId)
        return 0
    except:
        return -1

# Function to pull a random song from the Song database. Used to generate random song when page is loaded.

def getRandomSong(songDatabase):

    count = songDatabase.objects.count()

    return Song.objects.all()[randint(0, count - 1)]




