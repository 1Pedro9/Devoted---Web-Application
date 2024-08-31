from django.shortcuts import render, redirect, HttpResponse
from .models import Member, Journal, Plan, Category
import datetime

# Create your views here.
def index(request):
    if aut_user(request):
        return render(request, 'index.html')
    else:
        return redirect('login')

def dashboard(request):
    if aut_user(request):
        member_id = request.session.get("member_id")
        member = Member.objects.filter(member_id=member_id).first()
        plan = Plan.objects.filter(member=member)
        journal = Journal.objects.filter(member=member)
        
        # Name for the credit card
        name = f"{member.first_name} {member.last_name}"
        
        # Total bank account
        total = 0
        for i in journal:
            total += i.amount
            
        # Credit cards - Plan
        card = []
        colors = ['linear-gradient(135deg, #0f9d58 0%, #C6F28F 100%)', 'linear-gradient(135deg, #6a1b9a 0%, #BA8FF2 100%)', 'linear-gradient(135deg, #1e5799 0%, #7db9e8 100%)']
        color_count = 0
        count = 0
        
        for i in plan:
            card.append({'plan': i.plan, 'color': colors[color_count], 'count': count, 'left': count*60, 'zindex': len(plan)-count})
            color_count += 1
            count += 1
            if(color_count >= len(colors)):
                color_count = 0
        
        return render(request, 'dashboard.html', {'name': name, 'total': total, "plans": card, 'journal': journal})
    else:
        return redirect('login')

def budget(request):
    if aut_user(request):
        return render(request, 'budget.html')
    else:
        return redirect('login')

def journal(request):
    if aut_user(request):
        member_id = request.session.get("member_id")
        member = Member.objects.filter(member_id=member_id).first()
        plan = Plan.objects.filter(member=member)
        journal = Journal.objects.filter(member=member)
        
        new_journal = []
        prev = None
        prev_date = None
        total_month = 0
        crj_month = 0
        cpj_month = 0
        for i in journal:
            if prev is None:
                prev = i.date.strftime("%Y-%m")
                prev_date = i.date
            if prev is not None:
                current = i.date.strftime("%Y-%m")
                if current == prev:
                    new_journal.append({'journal_id': i.journal_id, 'journal': i.journal, 'date': i.date, 'amount': i.amount, 'details': i.details, 'is_new': 0, 'prev': prev_date, 'month_total': total_month, 'income': crj_month, 'expenses': cpj_month})
                else:
                    new_journal.append({'journal_id': i.journal_id, 'journal': i.journal, 'date': i.date, 'amount': i.amount, 'details': i.details, 'is_new': 1, 'prev': prev_date, 'month_total': total_month, 'income': crj_month, 'expenses': cpj_month})
                    total_month = 0
                    crj_month = 0
                    cpj_month = 0
                if i.journal == "crj":
                    crj_month += i.amount
                elif i.journal == "cpj":
                    cpj_month += i.amount
                # total_month += i.amount
                prev = i.date.strftime("%Y-%m")
                prev_date = i.date
        total = 0
        for i in journal:
            total += i.amount
        
        last_income = crj_month
        last_expenses = cpj_month
        
        #General Ledger Section
        months = []
        prev = None
        prev_date = None
        total_month = 0
        crj_month = 0
        cpj_month = 0
        for i in journal:
            if prev is None:
                prev = i.date.strftime("%Y-%m")
                prev_date = i.date
            if prev is not None:
                current = i.date.strftime("%Y-%m")
                if current == prev:
                    pass
                else:
                    is_positive = 0
                    if crj_month >= cpj_month:
                        is_positive = 1
                    is_pos = 0
                    if total_month >= 0:
                        is_pos = 1
                    cf = total_month + crj_month - cpj_month
                    cf_pos = 0
                    if cf >= 0:
                        cf_pos = 1
                    total_ = abs(total_month-cpj_month)
                    if total_month + crj_month >= abs(total_month-cpj_month):
                        total_ = total_month + crj_month
                    months.append({'total': total_month, 'prev': prev_date, 'is_positive': is_positive, 'income': crj_month, 'expenses': cpj_month, 'bf': total_month, "is_pos": is_pos, 'cf': cf, 'cf_pos': cf_pos, "total": total_})
                    total_month = crj_month - cpj_month
                    crj_month = 0
                    cpj_month = 0
                if(i.journal == "crj"):
                    crj_month += i.amount
                else :
                    cpj_month -= i.amount
                prev = i.date.strftime("%Y-%m")
                prev_date = i.date
                
        is_positive = 0
        if crj_month >= cpj_month:
            is_positive = 1
        is_pos = 0
        if total_month >= 0:
            is_pos = 1
        cf = total_month + crj_month - cpj_month
        cf_pos = 0
        if cf >= 0:
            cf_pos = 1
        total_ = abs(total_month-cpj_month)
        if total_month + crj_month >= abs(total_month-cpj_month):
            total_ = total_month + crj_month
        months.append({'total': total_month, 'prev': prev_date, 'is_positive': is_positive, 'income': crj_month, 'expenses': cpj_month, 'bf': total_month, "is_pos": is_pos, 'cf': cf, 'cf_pos': cf_pos, "total": total_})
        
        return render(request, 'journal.html', {'journal': new_journal, 'total': total, 'last_expenses': last_expenses, 'last_income': last_income, 'gl': months})
    else:
        return redirect('login')

def assets(request):
    if aut_user(request):
        return render(request, 'assets.html')
    else:
        return redirect('login')

def notifications(request):
    if aut_user(request):
        return render(request, 'notifications.html')
    else:
        return redirect('login')

def login(request):
    return render(request, 'login.html')


def aut_user(request):
    
    member = request.session.get('member_id', 0)
    if member == 0:
        return False
    return True

def user_login(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        members = Member.objects.filter(username=username, password=password)
        if len(members) == 1:
            request.session['member_id'] = members[0].member_id
            return redirect('index')
        else:
            return redirect('login')

def user_signup(request):
    if(request.method == "POST"):
        pass

def add_journal(request):
    if request.method == "POST":
        journal = request.POST.get("journal")
        date = request.POST.get("date")
        details = request.POST.get("details")
        amount = request.POST.get("amount")
        category_id = request.POST.get("category_id")
        
        date_ = date.split("/")
        date_new = datetime.datetime(int(date_[0]), int(date_[1]), int(date_[2]))
        
        member_id = request.session.get('member_id')
        plan_id = request.session.get("plan_id")
        member = Member.objects.filter(member_id=member_id).first()
        plan = Plan.objects.filter(plan_id=plan_id).first()
        category = Category.objects.filter(category_id=1).first()
        
        j = Journal(
            journal = journal,
            date = date,
            details = details,
            amount = amount,
            category=category,
            member = member,
            plan=plan
        )
        valid = False
        if presence_validation([journal, date, details, amount, category, member, plan]):
            valid = True 
            
        if valid:
            # j.save()
            return HttpResponse("Success")
        else:
            return HttpResponse("Failed")
    return HttpResponse("Error:400")

def presence_validation(array):
    valid = True
    for i in array:
        if i == "" or i == None or i == 0:
            valid = False
    return valid