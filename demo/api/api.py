from ninja import NinjaAPI
from content.models import Article, Category, Tag
from modules.models import Block, Menu
from django.core.serializers import serialize
from django.http import JsonResponse

api = NinjaAPI()


@api.get('/articles')
def list_articles(request, category_id: int = None, tag_id: int = None, skip: int = 0, limit: int = 100):
    queryset = Article.objects.all()
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    if tag_id:
        queryset = queryset.filter(tag_id=tag_id)
    serialized_data = serialize('json', queryset[skip:skip+limit])
    return JsonResponse(serialized_data, safe=False)


@api.get("/blocks")
def list_blocks(request):
    blocks = Block.objects.all()
    serialized_data = serialize('json', blocks)
    return JsonResponse(serialized_data, safe=False)


@api.get("/menus")
def list_menus(request):
    menus = Menu.objects.all()
    serialized_data = serialize('json', menus)
    return JsonResponse(serialized_data, safe=False)


@api.get("/tags")
def list_tags(request):
    tags = Tag.objects.all()
    serialized_data = serialize('json', tags)
    return JsonResponse(serialized_data, safe=False)


@api.get("/categories")
def list_categories(request):
    categories = Category.objects.all()
    serialized_data = serialize('json', categories)
    return JsonResponse(serialized_data, safe=False)
