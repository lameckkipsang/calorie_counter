from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Sum
from .models import FoodItem
from .forms import FoodItemForm


# Create your views here.
def tracker(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker')
    else:
        form = FoodItemForm()

    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)

    context = {
        'form': form,
        'food_items': food_items,
        'total_calories': total_calories,
    }
    return render(request, 'tracker.html', context)

def delete_food(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    item.delete()
    return redirect('tracker')

def reset_tracker(request):
    if request.method == 'POST':
        FoodItem.objects.all().delete()
    return redirect('tracker')
