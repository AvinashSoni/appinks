from django.template import Context,loader,RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound

def calcu(request):
	if request.POST:
		if '0' in request.POST.keys():
			b = request.POST['valueof']
			a = 0
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '1' in request.POST.keys():
			b = request.POST['valueof']
			a =1
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '2' in request.POST.keys():
			b = request.POST['valueof']
			a=2
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '3' in request.POST.keys():
			b = request.POST['valueof']
			a=3
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '4' in request.POST.keys():
			b = request.POST['valueof']
			a=4
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '5' in request.POST.keys():
			b = request.POST['valueof']
			a=5
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '6' in request.POST.keys():
			b = request.POST['valueof']
			a=6
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '7' in request.POST.keys():
			b = request.POST['valueof']
			a=7
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '8' in request.POST.keys():
			b = request.POST['valueof']
			a=8
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '9' in request.POST.keys():
			b = request.POST['valueof']
			a=9
			return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '+' in request.POST.keys():
			b = request.POST['valueof']
			a=' + '
			s = b.split()
			k = len(s)
			if k == 1:
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			else:
				if s[1] == '+':
					b = int(s[0]) + int (s[2])
					a = ' + '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '-':
					b = int(s[0]) - int (s[2])
					a = ' + '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '*':
					b = int(s[0]) * int (s[2])
					a = ' + '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '/':
					b = float(s[0]) / float (s[2])
					a = ' + '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '-' in request.POST.keys():
			b = request.POST['valueof']
			a=' - '
			s = b.split()
			k = len(s)
			if k == 1:
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			else:
				if s[1] == '+':
					b = int(s[0]) + int (s[2])
					a = ' - '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '-':
					b = int(s[0]) - int (s[2])
					a = ' - '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '*':
					b = int(s[0]) * int (s[2])
					a = ' - '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '/':
					b = float(s[0]) / float (s[2])
					a = ' - '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '*' in request.POST.keys():
			b = request.POST['valueof']
			a=' * '
			s = b.split()
			k = len(s)
			if k == 1:
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			else:
				if s[1] == '+':
					b = int(s[0]) + int (s[2])
					a = ' * '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '-':
					b = int(s[0]) - int (s[2])
					a = ' * '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '*':
					b = int(s[0]) * int (s[2])
					a = ' * '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '/':
					b = float(s[0]) / float (s[2])
					a = ' * '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif '/' in request.POST.keys():
			b = request.POST['valueof']
			a=' / '
			s = b.split()
			k = len(s)
			if k == 1:
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			else:
				if s[1] == '+':
					b = int(s[0]) + int (s[2])
					a = ' / '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '-':
					b = int(s[0]) - int (s[2])
					a = ' / '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '*':
					b = int(s[0]) * int (s[2])
					a = ' / '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
				elif s[1] == '/':
					b = float(s[0]) / float (s[2])
					a = ' / '
					return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			
		elif 'clear' in request.POST.keys():
			return HttpResponseRedirect('/calcu/')
		
		elif '=' in request.POST.keys():
			b = request.POST['valueof']
			s = b.split()
			if s[1] == '+':
				b = int(s[0]) + int (s[2])
				a = ''
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			elif s[1] == '-':
				b = int(s[0]) - int (s[2])
				a = ''
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			elif s[1] == '*':
				b = int(s[0]) * int (s[2])
				a = ''
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
			elif s[1] == '/':
				b = float(s[0]) / float (s[2])
				a = ''
				return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))
	else:
		b = ''
		a = ''
		return render_to_response('calcu.html',context_instance=RequestContext(request,{"b":b,"a":a,}))

			
