from test_app.models import Song
from test_app.forms import CreateNewSong


class SongCls:
    # Function to retrieve Song data
    @staticmethod
    def get_data(id):
        # Variable to store return data.
        result_dict = {}
        try:
            if id == 0:
                # If id==0 then return all the songs
                ls = Song.objects.all()
                result_dict["value"] = ls
            else:   # Return song having specified id
                song = Song.objects.get(id=id)
                result_dict["value"] = song
            # Return status success(200) and value with the song data
            result_dict["status"] = 200
        except Song.DoesNotExist:   # If Id doesn't Exists then return status Invalid request(400)
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

    # Function to retrieve Song Form
    @staticmethod
    def create_form(request):
        # Variable to store return data.
        result_dict = {}
        try:
            # If request method is POST then create form with the POST data
            if request.method == "POST":
                form = CreateNewSong(request.POST)
                # status Success(200) and value should be form with POST data
                result_dict["status"] = 200
                result_dict["value"] = form
            else:   # If Get method then return empty form
                form = CreateNewSong()
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
                form = CreateNewSong(request.POST, instance=Song.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
            else:   # If Get method then return form with specified Id data filled
                form = CreateNewSong(instance=Song.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
        except Song.DoesNotExist:   # If Id doesn't Exists then return status Invalid request(400)
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

