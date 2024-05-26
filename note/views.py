from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from .models import Note, Image
import json

@csrf_exempt
def store_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        title = data.get('title')
        category = data.get('category')
        note_text = data.get('note')
        summary = data.get('summary')
        time = data.get('time')
        images_data = data.get('images')

        # 创建一个新的Note对象
        note = Note.objects.create(username=username, title=title, category=category, note=note_text, summary=summary, time=time)

        # 对于每个图像数据，创建一个新的Image对象
        for image_data in images_data:
            start = image_data.get('start')
            base64 = image_data.get('base64')
            Image.objects.create(note=note, start=start, base64=base64)

        return HttpResponse('success')

    else:
        return HttpResponse('failure')

@csrf_exempt
def get_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        time = data.get('time')
        print(username, time)
        # 查询数据库，获取所有的Note对象
        note = Note.objects.filter(username=username, time=time).first()
        if note:
            note_values = model_to_dict(note)  # Convert the Note instance to a dictionary
            images = Image.objects.filter(note=note).values()
            note_values['images'] = list(images)
            return JsonResponse(note_values)
        else:
            return HttpResponse('No note found', status=404)
    else:
        return HttpResponse('failure')

@csrf_exempt
def get_all_notes(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        notes = Note.objects.filter(username=username).values()
        for note in notes:
            images = Image.objects.filter(note_id=note['id']).values()
            note['images'] = list(images)
        return JsonResponse(list(notes), safe=False)
    else:
        return HttpResponse('failure')

@csrf_exempt
def change_note(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        time = data.get('time')
        title = data.get('title')
        category = data.get('category')
        note_text = data.get('note')
        summary = data.get('summary')
        images_data = data.get('images')
        old_time = data.get('old_time')
        note = Note.objects.filter(username=username, time=old_time).first()
        if note:
            note.title = title
            note.category = category
            note.note = note_text
            note.summary = summary
            note.time = time
            note.save()
            Image.objects.filter(note=note).delete()
            for image_data in images_data:
                start = image_data.get('start')
                base64 = image_data.get('base64')
                Image.objects.create(note=note, start=start, base64=base64)
            return HttpResponse('success')
        else:
            return HttpResponse('No note found', status=404)
    else:
        return HttpResponse('failure')