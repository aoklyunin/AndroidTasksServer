import json
import logging

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Task

logger = logging.getLogger(__name__)


def index(request):
    latest_question_list = Task.objects.order_by("author")
    template = loader.get_template("tasks/index.html")
    context = {
        "latest_question_list": latest_question_list,
        "tasks": Task.objects.all()
    }
    return HttpResponse(template.render(context, request))


@csrf_exempt
def add(request):
    if request.method == "POST":
        response_data = {"status": "ok"}
        logger.info("got request body: " + str(request.body))
        data = json.loads(request.body)
        try:
            usname = data["user"]
            tlist = data["tasks"]
            Task.objects.filter(author=usname).delete()
            for t in tlist:
                try:
                    task = Task.objects.create(
                        author=usname,
                        title=t["title"],
                        text=t["text"],
                        solved=bool(t["solved"]),
                    )
                    task.save()
                except Exception as e:
                    logger.info("bad task json: " + str(e))
                    response_data = {"status": "bad task json: " + str(e)}
        except Exception as e:
            logger.info("bad json: " + str(e))
            response_data = {"status": "bad json: " + str(e)}
    else:
        response_data = {"status": "not post request"}

    return HttpResponse(json.dumps(response_data), content_type="application/json")
