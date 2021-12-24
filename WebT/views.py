from django.shortcuts import render, redirect, get_object_or_404
from .models import Sensor, TData
from .form import SensorForm
import datetime
import pytz


OurTimeZone = pytz.timezone('Europe/Moscow')
today = datetime.datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.now(OurTimeZone) + datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def get_sensor():
    try:
        pk = Sensor.objects.all()[0].pk
    except:
        pk = 0
    return pk


def graph_temp(request, pk=get_sensor(), days = 1):
    data = TData.objects.filter(sensor=pk, datetime__gt=(datetime.datetime.now(OurTimeZone) - datetime.timedelta(days=days)))
    sensors = Sensor.objects.all()
    if request.method == "POST":
        form = SensorForm(request.POST)
        if form.is_valid():
            sensor = form.save(commit=False)
            sensor.save()
            sensors = Sensor.objects.all()
            return render(request, 'graph.html', {'TDatas': data, 'Sensor': sensors,'form': form, 'pk': pk })
    else:
        form = SensorForm()
    return render(request, 'graph.html', {'TDatas': data, 'Sensor': sensors,'form': form, 'pk': pk })


def sensor_edit(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == "POST":
        form = SensorForm(request.POST, instance=sensor)
        if form.is_valid():
            sensor = form.save(commit=False)
            sensor.save()
            return redirect('TData', pk=sensor.pk)
    else:
        form = SensorForm(instance=sensor)
    return render(request, 'sensor_edit.html', { 'form': form, 'pk': pk })


def sensor_delete(request, pk):
    sensor = get_object_or_404(Sensor, pk=pk)
    if request.method == "POST":
        sensor.delete()
        return redirect('TData')
    return render( request, 'sensor_delete.html', {'sensor': sensor})
