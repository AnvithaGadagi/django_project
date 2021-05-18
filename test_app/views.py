from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .song import SongCls
from .podcast import PodcastCls
from .audiobook import AudiobookCls


# Create your views here.
def get(request, audioFileType, id=0):
    print("get")
    function_call_dict = {
        "song": SongCls.get_data,
        "podcast": PodcastCls.get_data,
        "audiobook": AudiobookCls.get_data
    }
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    if chosen_operation_function is not None:
        result_dict = chosen_operation_function(id)
        if result_dict["status"] == 200:
            if id == 0:
                return render(request, "test_app/get_all.html", {"ls": result_dict["value"], "type": audioFileType}, status=200)
            else:
                return render(request, "test_app/get.html", {"item": result_dict["value"], "type": audioFileType}, status=200)
        else:
            return render(request, "test_app/home.html", {"value": result_dict["value"]}, status=result_dict["status"])
    else:
        return render(request, "test_app/home.html", {"value":"Invalid Request"},status=400)


def create(request, audioFileType):
    function_call_dict = {
        "song": SongCls.create_form,
        "podcast": PodcastCls.create_form,
        "audiobook": AudiobookCls.create_form
    }
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    if chosen_operation_function is not None:
        result_dict = chosen_operation_function(request)
        status = result_dict["status"]
        value = result_dict["value"]
        if status == 200:
            if value.is_valid():
                value.save()
                return HttpResponseRedirect(reverse("get", args=[audioFileType]))
            else:
                return render(request, "test_app/create.html", {"form": value, "type": audioFileType}, status=status)
        else:
            return render(request, "test_app/home.html", {"value": value}, status=status)
    else:
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def update(request, audioFileType, id):
    function_call_dict = {
        "song": SongCls.update_form,
        "podcast": PodcastCls.update_form,
        "audiobook": AudiobookCls.update_form
    }
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    if chosen_operation_function is not None:
        result_dict = chosen_operation_function(request,id)
        status = result_dict["status"]
        form = result_dict["value"]
        if status == 200:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse("get", args=[audioFileType]))
            else:
                return render(request, "test_app/update.html", {"form": form, "type": audioFileType, "update_id": id}, status=200)
        else:
            return render(request, "test_app/home.html", {"value":form}, status=status)
    else:
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)



def delete(request, audioFileType, id):
    print(request,id)
    function_call_dict = {
        "song": SongCls.get_data,
        "podcast": PodcastCls.get_data,
        "audiobook": AudiobookCls.get_data
    }
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    if chosen_operation_function is not None:
        result_dict = chosen_operation_function(id)
        status = result_dict["status"]
        value = result_dict["value"]
        if status == 200:
            value.delete()
            return HttpResponseRedirect(reverse("get", args=[audioFileType]))
        else:
            return render(request, "test_app/home.html", {"value": value}, status=status)
    else:
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def home(request):
    return render(request, "test_app/home.html", {})