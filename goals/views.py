from .forms import CreatePlanForm
from .models import Plan
from .utils import get_response
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from todo.models import Task
import json 


@login_required
def create_plan(request):
    if request.method == "GET":
        form = CreatePlanForm()
        return render(request, 'create_plan.html', {'form': form})
    elif request.method == "POST":
        form = CreatePlanForm(request.POST)
        if form.is_valid:
            name = request.POST.get("name")
            if name in Plan.objects.filter(name=name):
                messages.add_message(request, constants.ERROR, "Can't have 2 plans whith the same name")
                return redirect('/create_plan')
            objective = request.POST.get("objective")
            max_date = request.POST.get(str("max_date"))
            weekly_hours = request.POST.get(str("weekly_hours"))
            date = str(datetime.now())
            response = get_response(name, objective, max_date, weekly_hours, date)
            plan = Plan(
                user=request.user,
                name=name,
                objective=objective,
                max_date=max_date,
                weekly_hours=weekly_hours
            )
            plan.save()
            
            new_tasks = json.loads(response)
                        
            for new_task in new_tasks['tasks']:
                task = Task(
                    user=request.user,
                    title=new_task['title'],
                    description=new_task['description'],
                    group=new_task['group'],
                    hours=new_task['estimated_hours'],
                    date=new_task['date'],
                    plan=plan
                )   
                task.save()
            messages.add_message(request, constants.SUCCESS, 'Plan created successfully')
            return redirect('/index')
        else:
            messages.add_message(request, constants.ERROR, 'Invalid fornat')
            return redirect('/create_plan')
  

@login_required
def plans(request):
    plans = Plan.objects.filter(user=request.user)
    return render(request, 'plans.html', {'plans': plans})


@login_required
def view_plan(request, id):
    plan = Plan.objects.filter(id=id)
    if not plan:
        return redirect('/index')
    tasks = Task.objects.filter(plan=plan[0]).order_by("date", "group")
    total = 0
    done = 0
    for task in tasks:
        total += 1
        if task.status == 'DONE':
            done += 1
    progress = "%.1f" % (done * 100 / total)
    plan_name = plan[0]
    return render(request, 'view_plan.html', {'progress': progress, 'plan': plan_name, 'tasks': tasks, 'total': total, 'done': done})



