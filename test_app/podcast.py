from test_app.models import Podcast
from test_app.forms import CreateNewPodcast


class PodcastCls:
    @staticmethod
    def get_data(id=0):
        result_dict = {}
        try:
            if id == 0:
                ls = Podcast.objects.all()
                result_dict["value"] = ls
            else:
                song = Podcast.objects.get(id=id)
                result_dict["value"] = song
            result_dict["status"] = 200
        except Podcast.DoesNotExist:
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

    @staticmethod
    def create_form(request):
        result_dict = {}
        try:
            if request.method == "POST":
                form = CreateNewPodcast(request.POST)
                result_dict["status"] = 200
                result_dict["value"] = form
            else:
                form = CreateNewPodcast()
                result_dict["status"] = 200
                result_dict["value"] = form
        except Exception as e:
            result_dict["status"] = 500
            result_dict["value"] = str(e)
        return result_dict

    @staticmethod
    def update_form(request, id):
        result_dict = {}
        try:
            if request.method == "POST":
                form = CreateNewPodcast(request.POST, instance=Podcast.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
            else:
                form = CreateNewPodcast(instance=Podcast.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
        except Podcast.DoesNotExist:
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

