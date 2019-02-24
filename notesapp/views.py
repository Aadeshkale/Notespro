from django.shortcuts import render,redirect
from django.views import View
from notesapp.forms import LoginForm,InsertForm,DeleteForm,UpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import sessions
from notesapp.models import NotesInfo

class LoginView(View):
    def get(self,request):
        myfrom=LoginForm()
        return render(request,'login.html',{'myform':myfrom})
    def post(self,request):
        myform=LoginForm(request.POST)
        if myform.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            if User.objects.get(email=email):
                ob=User.objects.get(email=email)
                username=ob.username
                if authenticate(username=username, password=password):
                    request.session[email]=email
                    return redirect('menu',username)
                else:
                    messages.warning(request,'Wrong Password :(')    
            else:
                messages.warning(request,'Email is not registered :(')
            return redirect(request.path_info)
        else:
            messages.warning(request,'Invalid Data :(')
            return redirect(request.path_info)
            
class MainView(View):
      def get(self,request,username):
          ob=User.objects.get(username=username)
          email=ob.email
          if request.session.has_key(email):
            return render(request,'main.html',{'username':username})
          else:
              messages.warning(request,'You need to login first :(')
              return redirect('login')
class LogoutView(View):
    def get(self,request,username):
        ob=User.objects.get(username=username)
        email=ob.email
        del request.session[email]
        messages.success(request,'logout Successfully :)')
        return redirect('login')

class InsertView(View):
    def get(self,request,username):
        ob=User.objects.get(username=username)
        email=ob.email
        myform=InsertForm()
        if request.session.has_key(email):
            return render(request,'insert.html',{'username':username,'myform':myform})
        else:
            messages.warning(request,'You need to login first :(')
            return redirect('login')
    def post(self,request,username):
        myform=InsertForm(request.POST)
        if myform.is_valid():
            myform.save()
            messages.success(request,'Your Note added Successfully :)')
            return redirect(request.path_info)

class DisplayView(View):
    def get(self,request,username):
        ob=User.objects.get(username=username)
        email=ob.email
        data=NotesInfo.objects.all().order_by('-datetime')
        if request.session.has_key(email):
            return render(request,'display.html',{'data':data})
        else:
            messages.warning(request,'You need to login first :(')
            return redirect('login')

class UpdateView(View):
    def get(self,request,username):
        ob=User.objects.get(username=username)
        email=ob.email
        myform=UpdateForm()
        if request.session.has_key(email):
            return render(request,'update.html',{'myform':myform})
        else:
            messages.warning(request,'You need to login first :(')
            return redirect('login')
    def post(self,request,username):
        myform=UpdateForm(request.POST)
        if myform.is_valid():
            ids=request.POST['ids']
            if NotesInfo.objects.filter(id=ids):
                ob=NotesInfo.objects.filter(id=ids)
                subject=request.POST['subject']
                discription=request.POST['discription']
                ob.update(subject=subject,discription=discription)
                messages.success(request,'Note Updated Successfully :)')
            else:
                messages.warning(request,'Invalid Note id :(')
            return redirect(request.path_info)
        else:
            messages.warning(request,'Invalid Data :(')
            return redirect(request.path_info)
            
class DeleteView(View):
    def get(self,request,username):
        ob=User.objects.get(username=username)
        email=ob.email
        myform=DeleteForm()
        if request.session.has_key(email):
            return render(request,'delete.html',{'myform':myform})
        else:
            messages.warning(request,'You need to login first :(')
            return redirect('login')
    def post(self,request,username):
        myform=DeleteForm(request.POST)
        if myform.is_valid():
            ids=request.POST['ids']
            if NotesInfo.objects.filter(id=ids):
                ob=NotesInfo.objects.filter(id=ids)
                ob.delete()
                messages.success(request,'Note Deleted Successfully :)')
            else:
                messages.warning(request,'Invalid Note Id :(')
        return redirect(request.path_info)
