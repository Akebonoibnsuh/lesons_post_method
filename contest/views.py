from django.shortcuts import render
from .forms import ContestForm


def proposal(request):
    if request.method == 'POST':
        form = ContestForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contest/form.html', {
                'form': ContestForm(),
                'success': True,
                'title': form.cleaned_data['title']
            })
        else:
            return render(request, 'contest/form.html', {
                'form': form,
                'success': False,
            })
    else:
        form = ContestForm()
    return render(request, 'contest/form.html', {'form': form})
