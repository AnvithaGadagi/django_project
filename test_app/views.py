from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .song import SongCls
from .podcast import PodcastCls
from .audiobook import AudiobookCls


# get function to get data for the specific audiofiletype and id(optional)
def get(request, audioFileType, id=0):
    # function_call_dict to store all functions of different audioFileType
    function_call_dict = {
        "song": SongCls.get_data,   # get song data
        "podcast": PodcastCls.get_data,     # get podcast data
        "audiobook": AudiobookCls.get_data  # get audiobook data
    }
    # Get the function of the requested audioFileType
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    # Check if the requested audioFileType is valid
    if chosen_operation_function is not None:
        # call the function and get the result_dict
        result_dict = chosen_operation_function(id)
        # Check for the result status 200 (Success)
        if result_dict["status"] == 200:
            # If id is 0 indicates requested all the data in the audioFileType
            if id == 0:
                return render(request, "test_app/get_all.html", {"ls": result_dict["value"], "type": audioFileType}, status=200)
            else:   # return only requested id data of the audioFileType
                return render(request, "test_app/get.html", {"item": result_dict["value"], "type": audioFileType}, status=200)
        else:   # If status is (Not Success) then return with the status and specific message
            return render(request, "test_app/home.html", {"value": result_dict["value"]}, status=result_dict["status"])
    else:   # If audioFileType is invalid then return status 400
        return render(request, "test_app/home.html", {"value": "Invalid Request"},status=400)

# create function to create/add specific audiofiletype to database
def create(request, audioFileType):
    # function_call_dict to store all functions of different audioFileType
    function_call_dict = {
        "song": SongCls.create_form,    # create song form
        "podcast": PodcastCls.create_form,  # create podcast form
        "audiobook": AudiobookCls.create_form   # create audiobook form
    }
    # Get the function of the requested audioFileType
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    # Check if the requested audioFileType is valid
    if chosen_operation_function is not None:
        # call the function and get the result_dict
        result_dict = chosen_operation_function(request)
        status = result_dict["status"]
        value = result_dict["value"]
        # Check for the result status 200 (Success)
        if status == 200:
            # If form values are valid then save data to database
            if value.is_valid():
                value.save()
                # show all the data of the requested audioFileType
                return HttpResponseRedirect(reverse("get", args=[audioFileType]))
            else:   # form values are empty/invalid
                # return the form to add data
                return render(request, "test_app/create.html", {"form": value, "type": audioFileType}, status=status)
        else:   # If status is (Not Success) then return with the status and specific message
            return render(request, "test_app/home.html", {"value": value}, status=status)
    else:   # If audioFileType is invalid then return status 400
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def update(request, audioFileType, id):
    function_call_dict = {
        "song": SongCls.update_form,
        "podcast": PodcastCls.update_form,
        "audiobook": AudiobookCls.update_form
    }
    # Get the function of the requested audioFileType
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    # Check if the requested audioFileType is valid
    if chosen_operation_function is not None:
        # call the function and get the result_dict
        result_dict = chosen_operation_function(request,id)
        status = result_dict["status"]
        form = result_dict["value"]
        # Check for the result status 200 (Success)
        if status == 200:
            # If updated form is updated with the valid data then save data to database
            if form.is_valid():
                form.save()
                # show all the data of the requested audioFileType
                return HttpResponseRedirect(reverse("get", args=[audioFileType]))
            else:   # return update form to edit data
                return render(request, "test_app/update.html", {"form": form, "type": audioFileType, "update_id": id}, status=200)
        else:   # If status is (Not Success) then return with the status and specific message
            return render(request, "test_app/home.html", {"value":form}, status=status)
    else:   # If audioFileType is invalid then return status 400
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)



def delete(request, audioFileType, id):
    print(request,id)
    function_call_dict = {
        "song": SongCls.get_data,
        "podcast": PodcastCls.get_data,
        "audiobook": AudiobookCls.get_data
    }
    # Get the function of the requested audioFileType
    chosen_operation_function = function_call_dict.get(audioFileType, None)
    # Check if the requested audioFileType is valid
    if chosen_operation_function is not None:
        # call the function and get the result_dict
        result_dict = chosen_operation_function(id)
        status = result_dict["status"]
        value = result_dict["value"]
        # Check for the result status 200 (Success)
        if status == 200:
            # data is valid to delete then delete it from database.
            value.delete()
            # show all the data of the requested audioFileType
            return HttpResponseRedirect(reverse("get", args=[audioFileType]))
        else:   # If status is (Not Success) then return with the status and specific message
            return render(request, "test_app/home.html", {"value": value}, status=status)
    else:   # If audioFileType is invalid then return status 400
        return render(request, "test_app/home.html", {"value": "Invalid Request"}, status=400)


def home(request):
    return render(request, "test_app/home.html", {})