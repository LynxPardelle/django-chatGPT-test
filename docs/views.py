from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Doc, DocSection
from datetime import datetime

# Create your views here.


def author(request):
    return HttpResponse("""<h1>Lynx Pardelle</h1>
    <h2>From Docs APP</h2>                    
    """)


def createDoc(request):
    try:
        document = Doc(
            doc_title=request.POST['doc_title'],
            doc_text=request.POST['doc_text'],
            doc_date=datetime.datetime.now())
        print(document)
        if (not document):
            raise Exception("Document does not exist")
        return JsonResponse({'document': document})
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def createDocSection(request, doc_id):
    try:
        document = Doc.objects.get(doc_id=doc_id)
        if (not document):
            raise Exception("Document does not exist")
        document_section = DocSection(
            doc_id=document,
            doc_section_title=request.POST['doc_section_title'],
            doc_section_text=request.POST['doc_section_text'],
            doc_section_date=datetime.datetime.now())
        print(document_section)
        return JsonResponse({'document_section': document_section})
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def readMany(request):
    try:
        documents = list(Doc.objects.values())
        print(documents)
        print(len(documents))
        if (not documents or len(documents) == 0):
            raise Exception("There are no documents")
        return JsonResponse({'documents': documents})
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def read(request, doc_id):
    try:
        document = Doc.objects.get(doc_id=doc_id)
        print(document)
        if (not document):
            raise Exception("Document does not exist")
        return JsonResponse({'document': document})
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def updateDoc(request, doc_id):
    try:
        document = Doc.objects.get(doc_id=doc_id)
        if (not document):
            raise Exception("Document does not exist")
        document.doc_title = request.POST['doc_title']
        document.doc_text = request.POST['doc_text']
        print(document)
        return JsonResponse({'document': document})
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def updateDocSection(request, doc_section_id):
    try:
        document_section = DocSection.objects.get(
            doc_section_id=doc_section_id)
        if (not document_section):
            raise Exception("Document Section does not exist")
        document_section.doc_section_title = request.POST['doc_section_title']
        document_section.doc_section_text = request.POST['doc_section_text']
        print(document_section)
        return JsonResponse({'document_section': document_section})
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def deleteDoc(request, doc_id):
    try:
        document = Doc.objects.get(doc_id=doc_id)
        if (not document):
            raise Exception("Document does not exist")
        document.delete()
        return HttpResponse('Document deleted')
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))


def deleteDocSection(request, doc_section_id):
    try:
        document_section = DocSection.objects.get(
            doc_section_id=doc_section_id)
        if (not document_section):
            raise Exception("Document Section does not exist")
        document_section.delete()
        return HttpResponse('Document Section deleted')
    except Exception as exception:
        print('An exception occurred')
        print(exception)
        return HttpResponse('An exception occurred and its: ' + str(exception))
