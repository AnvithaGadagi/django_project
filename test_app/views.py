from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from test_app.models import Audiobook, Podcast, Song
from .forms import CreateNewSong, CreateNewPodcast, CreateNewAudiobook


# Create your views here.
def get(request, audioFileType, id=0):
    if id == 0:
        if audioFileType == "song":
            ls = Song.objects.all()
            return render(request, "test_app/get_all.html", {"ls": ls, "type": "song"})
        elif audioFileType == "podcast":
            ls = Podcast.objects.all()
            return render(request, "test_app/get_all.html", {"ls": ls, "type": "podcast"})
        elif audioFileType == "audiobook":
            ls = Audiobook.objects.all()
            return render(request, "test_app/get_all.html", {"ls": ls, "type": "audiobook"})
        else:
            return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)
    else:
        if audioFileType == "song":
            try:
                song = Song.objects.get(id=id)
            except Song.DoesNotExist:
                return render(request, "test_app/home.html", {"value": "Song doesn't Exists for given id"}, status=400)
            return render(request, "test_app/get.html", {"item": song, "type": "song"}, status=200)
        elif audioFileType == "podcast":
            try:
                podcast = Podcast.objects.get(id=id)
            except Podcast.DoesNotExist:
                return render(request, "test_app/home.html", {"value": "Podcast doesn't Exists for given id"}, status=400)
            return render(request, "test_app/get.html", {"item": podcast, "type": "podcast"}, status=200)
        elif audioFileType == "audiobook":
            try:
                audiobook = Audiobook.objects.get(id=id)
            except Audiobook.DoesNotExist:
                return render(request, "test_app/home.html", {"value": "Audiobook doesn't Exists for given id"}, status=400)
            return render(request, "test_app/get.html", {"item": audiobook, "type": "audiobook"}, status=200)
        else:
            return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def create(request, audioFileType):
    if request.method == "POST":
        if audioFileType == "song":
            try:
                form = CreateNewSong(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/song")
                else:
                    return render(request, "test_app/create.html", {"form": form, "type": "song"}, status=500)
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
        elif audioFileType == "podcast":
            try:
                form = CreateNewPodcast(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/podcast")
                else:
                    return render(request, "test_app/create.html", {"form": form, "type": "podcast"}, status=500)
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
        elif audioFileType == "audiobook":
            try:
                form = CreateNewAudiobook(request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/audiobook")
                else:
                    return render(request, "test_app/create.html", {"form": form, "type": "audiobook"}, status=500)
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
        else:
            return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)
    else:
        if audioFileType == "song":
            form = CreateNewSong()
            return render(request, "test_app/create.html", {"form": form, "type": "song"})
        elif audioFileType == "podcast":
            form = CreateNewPodcast()
            return render(request, "test_app/create.html", {"form": form, "type": "podcast"})
        elif audioFileType == "audiobook":
            form = CreateNewAudiobook()
            return render(request, "test_app/create.html", {"form": form, "type": "audiobook"})
        else:
            return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def update(request, audioFileType, id):
    if request.method == "POST":
        if audioFileType == "song":
            try:
                form = CreateNewSong(request.POST, instance=Song.objects.get(id=id))
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/song")
                else:
                    return render(request, "test_app/update.html", {"form": form, "type": "song", "update_id": id})
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
        elif audioFileType == "podcast":
            try:
                form = CreateNewPodcast(request.POST, instance=Podcast.objects.get(id=id))
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/podcast")
                else:
                    return render(request, "test_app/update.html", {"form": form, "type": "podcast", "update_id": id})
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
        elif audioFileType == "audiobook":
            try:
                form = CreateNewAudiobook(request.POST, instance=Audiobook.objects.get(id=id))
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/audiobook")
                else:
                    return render(request, "test_app/update.html", {"form": form, "type": "audiobook", "update_id": id})
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
        else:
            return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)
    else:
        if audioFileType == "song":
            try:
                song = Song.objects.get(id=id)
                form = CreateNewSong(instance=song)
            except Song.DoesNotExist:
                return render(request, "test_app/home.html", {"value": "Invalid Id Update Request"}, status=400)
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
            return render(request, "test_app/update.html", {"form": form, "type": "song", "update_id": id})
        elif audioFileType == "podcast":
            try:
                podcast = Podcast.objects.get(id=id)
                form = CreateNewPodcast(instance=podcast)
            except Podcast.DoesNotExist:
                return render(request, "test_app/home.html", {"value": "Invalid Id Update Request"}, status=400)
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
            return render(request, "test_app/update.html", {"form": form, "type": "podcast", "update_id": id})
        elif audioFileType == "audiobook":
            try:
                audiobook = Audiobook.objects.get(id=id)
                form = CreateNewAudiobook(instance=audiobook)
            except Audiobook.DoesNotExist:
                return render(request, "test_app/home.html", {"value": "Invalid Id Update Request"}, status=400)
            except Exception as e:
                return render(request, "test_app/home.html", {"value": "Invalid Request" + str(e)}, status=500)
            return render(request, "test_app/update.html", {"form": form, "type": "audiobook", "update_id": id})
        else:
            return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def delete(request, audioFileType, id):
    if audioFileType == "song":
        try:
            song = Song.objects.get(id=id)
            song.delete()
        except Song.DoesNotExist:
            return render(request, "test_app/home.html", {"value": "Invalid Id Delete Request"}, status=400)
        return HttpResponseRedirect("/song")
    elif audioFileType == "podcast":
        try:
            podcast = Podcast.objects.get(id=id)
            podcast.delete()
        except Podcast.DoesNotExist:
            return render(request, "test_app/home.html", {"value": "Invalid Id Delete Request"}, status=400)
        return HttpResponseRedirect("/podcast")
    elif audioFileType == "audiobook":
        try:
            audiobook = Audiobook.objects.get(id=id)
            audiobook.delete()
        except Audiobook.DoesNotExist:
            return render(request, "test_app/home.html", {"value": "Invalid Id Delete Request"}, status=400)
        return HttpResponseRedirect("/audiobook")
    else:
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def home(request):
    return render(request, "test_app/home.html", {})