from test_app.models import Podcast
from test_app.forms import CreateNewPodcast


class PodcastCls:
    # Function to retrieve Podcast data
    @staticmethod
    def get_data(id=0):
        # Variable to store return data.
        result_dict = {}
        try:
            # If id==0 then return all the podcasts
            if id == 0:
                ls = Podcast.objects.all()
                result_dict["value"] = ls
            else:   # Return podcast having specified id
                song = Podcast.objects.get(id=id)
                result_dict["value"] = song
            result_dict["status"] = 200
        # Return status success(200) and value with the podcast data
        except Podcast.DoesNotExist:    # If Id doesn't Exists then return status Invalid request(400)
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

    # Function to retrieve Podacst Form
    @staticmethod
    def create_form(request):
        # Variable to store return data.
        result_dict = {}
        try:
            # If request method is POST then create form with the POST data
            if request.method == "POST":
                form = CreateNewPodcast(request.POST)
                # status Success(200) and value should be form with POST data
                result_dict["status"] = 200
                result_dict["value"] = form
            else:   # If Get method then return empty form
                form = CreateNewPodcast()
                # status Success(200) and value should be form with empty data
                result_dict["status"] = 200
                result_dict["value"] = form
        except Exception as e:  # If there is any Exception then status is Internal Error(500)
            result_dict["status"] = 500
            result_dict["value"] = str(e)
        return result_dict

    @staticmethod
    def update_form(request, id):
        # Variable to store return data.
        result_dict = {}
        try:
            # If request method is POST then create form with the POST data of the specific Id
            if request.method == "POST":
                form = CreateNewPodcast(request.POST, instance=Podcast.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
            else:    # If Get method then return form with specified Id data filled
                form = CreateNewPodcast(instance=Podcast.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
        except Podcast.DoesNotExist:    # If Id doesn't Exists then return status Invalid request(400)
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

