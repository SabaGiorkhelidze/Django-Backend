import json
from ninja import NinjaAPI
from content.models import Article, Category, Tag
from modules.models import Block, Menu
from django.core.serializers import serialize
from django.http import JsonResponse
from users.models import CustomUser
from ninja.errors import HttpError

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


# ____POST REQUESTS_____


@api.post("/add_articles")
def create_article(request, title: str, description: str, author_id: int, category_id: int, main_image: str, is_published: bool):
    try:
        author = CustomUser.objects.get(id=author_id)
    except CustomUser.DoesNotExist:
        raise HttpError(400, "Invalid Author ID")
    
    article = Article(title=title, description=description, author=author, category_id=category_id, main_image=main_image, is_published=is_published)
    article.save()
    return JsonResponse({'message': 'Article created successfully'})


@api.post("/add_categories")
def create_category(request, name: str, logo: str):
    category = Category(name=name, logo=logo)
    category.save()
    return JsonResponse({'message': 'Category created successfully'})

# this route is success
@api.post("/add_tags")
def create_tag(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        tag = Tag(name=name)
        tag.save()
        return JsonResponse({'message': 'Tag created successfully'})
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Error decoding JSON'}, status=400)


@api.post("/add_menus")
def create_menu(request, name: str, link: str, is_external: bool, category_id: int, is_active: bool):
    menu = Menu(name=name, link=link, is_external=is_external, category_id=category_id, is_active=is_active)
    menu.save()
    return JsonResponse({'message': 'Menu created successfully'})


@api.post("/add_blocks")
def create_block(request, articles, block_style: str, position: str, row: int, title: str, show_title: bool):
    block = Block(block_style=block_style, position=position, row=row, title=title, show_title=show_title)
    block.save()
    block.articles.add(*articles)
    return JsonResponse({'message': 'Block created successfully'})

