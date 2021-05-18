from test_app.models import Audiobook
from test_app.forms import CreateNewAudiobook


class AudiobookCls:
    @staticmethod
    def get_data(id):
        result_dict = {}
        try:
            if id == 0:
                ls = Audiobook.objects.all()
                result_dict["value"] = ls
            else:
                song = Audiobook.objects.get(id=id)
                result_dict["value"] = song
            result_dict["status"] = 200
        except Audiobook.DoesNotExist:
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

    @staticmethod
    def create_form(request):
        result_dict = {}
        try:
            if request.method == "POST":
                form = CreateNewAudiobook(request.POST)
                result_dict["status"] = 200
                result_dict["value"] = form
            else:
                form = CreateNewAudiobook()
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
                form = CreateNewAudiobook(request.POST, instance=Audiobook.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
            else:
                form = CreateNewAudiobook(instance=Audiobook.objects.get(id=id))
                result_dict["status"] = 200
                result_dict["value"] = form
        except Audiobook.DoesNotExist:
            result_dict["status"] = 400
            result_dict["value"] = "Id Does Not Exists"
        return result_dict

