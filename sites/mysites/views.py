from django.shortcuts import render

# Create your views here.
def testcase(request):
	template = "index.html"
	context = {}
	return render(request, template, context)