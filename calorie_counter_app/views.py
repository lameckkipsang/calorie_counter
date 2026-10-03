from django.shortcuts import render,redirect
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
