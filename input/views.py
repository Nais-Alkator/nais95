from django.shortcuts import render
from .models import Input


def get_main(request):
    return render(request, "base.html")


def get_inputs(request):
    inputs = request.POST.getlist("input_item")
    new_inputs = [Input(value=input) for input in inputs]
    Input.objects.bulk_create(new_inputs)
    return render(request, "inputs.html", context={"inputs": new_inputs})