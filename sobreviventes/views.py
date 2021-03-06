from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from sobreviventes.models import Sobreviventes, Inventario, Sobreviventesinventario
from sobreviventes.serializers import SobreviventesSerializer, inventarioSerializer, SobreviventesinventarioSerializer

#Sobreviventes

#Metodo para adicionar sobreviventes e inventario através da relação many to many 
def adicionarSobrevivente(request):
    sobrevivente_data = JSONParser().parse(request)
    sobreviventes_srl = SobreviventesSerializer(data = sobrevivente_data)

    #remoção dos itens dentro da requisição para a validação do novo sobrevivente
    itens = sobrevivente_data.pop('itens')

    #Adição da relação entre itens enviados e sobrevivente recem cadastrado 
    if sobreviventes_srl.is_valid():
        sobreviventes_srl.save()
        sobrevivente = Sobreviventes.objects.last()

        print(sobrevivente)
        for item in itens:
            itemBd = Inventario.objects.get(pk=item['inventario_id'])
            qtd = item['qtd']
            Sobreviventesinventario.objects.create(sobrevivente = sobrevivente, item = itemBd, qtd = qtd)

        return JsonResponse('Sobrevivente adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Sobrevivente', safe=False)

#Mostrar todos sobreviventes
def mostrarSobreviventes(request):
    sobreviventes = Sobreviventes.objects.all()
    sobreviventes_srl = SobreviventesSerializer(sobreviventes, many=True)
    return JsonResponse(sobreviventes_srl.data, safe=False)

#Mostrar sobrevivente filtrado por ID
def mostrarSobrevivente(request, rid):
	sobrevivente = Sobreviventes.objects.get(sobreviventes_id = rid)
	sobreviventes_srl = SobreviventesSerializer(sobrevivente, many=False)
	return JsonResponse(sobreviventes_srl.data, safe=False)

#Atualizar sobrevivente
def atualizarSobrevivente(request, rid):
    sobrevivente_data = JSONParser().parse(request)
    sobrevivente = Sobreviventes.objects.get(sobreviventes_id = rid)
    sobreviventes_srl = SobreviventesSerializer(sobrevivente, data = sobrevivente_data,  partial=True)
    if sobreviventes_srl.is_valid():
        sobreviventes_srl.save()
        return JsonResponse('Sobrevivente atualizado com sucesso!', safe=False)
    return JsonResponse('Falha ao atualizar Sobrevivente', safe=False)

#Deletar sobrevivente
def deletarSobrevivente(request, rid):
    sobrevivente = Sobreviventes.objects.get(sobreviventes_id = rid)
    sobrevivente.delete()
    return JsonResponse('Sobrevivente deletado com sucesso', safe=False)


#Itens
#Adicionar itens
def adicionarItens(request):
    item_data = JSONParser().parse(request)
    itens_srl = inventarioSerializer(data = item_data)
    if itens_srl.is_valid():
        itens_srl.save()
        return JsonResponse('item adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado item', safe=False)

#Mostrar itens todos
def mostrarItens(request):
    items = Inventario.objects.all()
    itens_srl = inventarioSerializer(items, many=True)
    return JsonResponse(itens_srl.data, safe=False)

#Mostrar item filtrado por ID
def mostrarItem(request, rid):
	item = Inventario.objects.get(inventario_id = rid)
	itens_srl = inventarioSerializer(item, many=False)
	return JsonResponse(itens_srl.data, safe=False)

#Atualizar item
def atualizarItens(request, rid):
    item_data = JSONParser().parse(request)
    item = Inventario.objects.get(items_id = rid)
    itens_srl = inventarioSerializer(item, data = item_data,  partial=True)
    if itens_srl.is_valid():
        itens_srl.save()
        return JsonResponse("item atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Adicionado item", safe=False)

#Deletar sobrevivente
def deletarItens(request, rid):
    item = Inventario.objects.get(inventario_id = rid)
    item.delete()
    return JsonResponse("item deletado com sucesso", safe=False)

#Items Sobreviventes
#Mostrar relações many to many intes e sobreviventes
def mostrarSobreviventesinventarios(request):
    sobreviventesItens_data = Sobreviventesinventario.objects.all()
    sobreviventesItens_srl = SobreviventesinventarioSerializer(sobreviventesItens_data, many=True)
    return JsonResponse(sobreviventesItens_srl.data, safe=False)

def mostrarSobreviventeinventario(request, rid):
	Sobreviventeinventario = Sobreviventesinventario.objects.filter(sobrevivente_id = rid)
	Sobreviventeinventario_srl = SobreviventesinventarioSerializer(Sobreviventeinventario, many=True)
	return JsonResponse(Sobreviventeinventario_srl.data, safe=False)

