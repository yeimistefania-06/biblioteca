from django.shortcuts import render, redirect, get_object_or_404
from .models import autor, libro


def crear_autor(request):
    if request.method == 'GET':
        return render(request,'crear_autor.html')
    else:
        autorObj = autor(
            nombre = request.POST.get('nombre'),
            lugar_nacimiento = request.POST.get('lugar'),
            fecha_nacimiento = request.POST.get('fecha')
        )
        autorObj.save()
        return redirect('crear_autor')

def editar_autor(request, autor_id):
    if request.method =='GET':
        autorObj = get_object_or_404(autor, pk=autor_id)   
        return render(request,'editar_autor.html', {'autor':autorObj})
    else:
        autorObj = get_object_or_404(autor, pk=autor_id)
        autorObj.nombre = request.POST.get('nombre')
        autorObj.lugar_nacimiento = request.POST.get('lugar')
        autorObj.fecha_nacimiento = request.POST.get('fecha')

        autorObj.save()
        return redirect('crear_autor')

def eliminar_autor(request, autor_id):
    autorObj = get_object_or_404(autor, pk=autor_id)
    autorObj.delete()
    return redirect('crear_autor')

def crear_libro(request):
    if request.method == 'GET':
        autores = autor.objects.all()
        return render(request, 'crear_libro.html',{'autores':autores})
    else:
        autorObj = autor.objects.get(pk=request.POST.get('autor'))
        libroObj = libro(
            titulo = request.POST.get('titulo'),
            descripcion = request.POST.get('descripcion'),
            autor_id = autorObj
        )
        libroObj.save()
        return redirect('crear_libro')

def listar_libros(request):
    libros = libro.objects.all()
    return render(request, 'listar_libros.html', {'libros':libros})

def editar_libro(request, libro_id):
    if request.method =="GET":
        libroObj = get_object_or_404(libro,pk = libro_id)
        autores = autor.objects.all()
        return render (request, 'editar_libro.html',{
            'libro':libroObj,
            'autores':autores})
    else:
        libroObj = get_object_or_404(libro, pk= libro_id)
        autorObj= get_object_or_404(autor, pk =request.POST.get('autor'))
        libroObj.titulo = request.POST.get('titulo')
        libroObj.descripcion = request.POST.get('descripcion')
        libroObj.autor = autorObj
        libroObj.save()
        return redirect('listar_libros')

def eliminar_libro(request,libro_id):
    libroObj = get_object_or_404(libro, pk =libro_id)
    libroObj.delete()
    return redirect('listar_libros')

def listar_autores(request):
    autores = autor.objects.all()
    return render(request, 'listar_autores.html', {'autores':autores})