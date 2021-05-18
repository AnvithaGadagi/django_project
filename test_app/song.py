from test_app.models import Song
from test_app.forms import CreateNewSong


class SongCls:
    @staticmethod
    def get_data(id):
        result_dict = {}
        try:
            if id == 0:
                ls = Song.objects.all()
                result_dict["value"] = ls
            else:
                song = Song.objects.get(id=id)
                result_dict["value"] = song
            result_dict["status"] = 200
        except Song.DoesNotExist:
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

    @staticmethod
    def create_form(request):
        result_dict = {}
        try:
            if request.method == "POST":
                form = CreateNewSong(request.POST)
                result_dict["status"] = 200
                result_dict["value"] = form
            else:
                form = CreateNewSong()
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
                form = CreateNewSong(request.POST, instance=Song.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
            else:
                form = CreateNewSong(instance=Song.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
        except Song.DoesNotExist:
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

