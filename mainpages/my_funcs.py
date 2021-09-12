from official_use.models import Category, Lesson

def get_data(category):
    objs = Lesson.objects.filter(category__name = category)
    return objs