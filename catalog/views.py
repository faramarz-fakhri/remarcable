from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.db.models import Q
from .models import Item, Category, Tag
from .forms import ItemFilterForm

def item_list(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    selected_category = request.GET.get("category")
    selected_tags = request.GET.getlist("tags")

    if selected_category:
        items = items.filter(category_id=selected_category)

    if selected_tags:
        items = items.filter(tags__id__in=selected_tags).distinct()

    return render(request, "catalog/item_list.html", {
        "items": items,
        "categories": categories,
        "tags": tags,
        "selected_category": selected_category,
        "selected_tags": selected_tags,
    })

