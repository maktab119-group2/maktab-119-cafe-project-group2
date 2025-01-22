from django.shortcuts import render


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)  # Include request.FILES here
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'cafe/add_menu_item.html', {'form': form})


def edit_menu_item(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)  # Include request.FILES here
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'cafe/edit_menu_item.html', {'form': form})
