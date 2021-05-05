#***(1)Retorna todos los estudiantes de la tabla de estudiantes
estudiante = Estudiante.objects.all()
#(2)Retorna el primer estuantes en tabla
firstEstudiante = Estudiante.objects.first()
#(3)Retorna el ultimo estuantes en tabla
lastEstudiante = Estudiante.objects.last()
#(4)Returns single customer by name
estudianteByName = Estudiante.objects.get(name='Felipe Herrera')
#***(5)Returns single customer by name
estudianteById = Estudiante.objects.get(id=4)
#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstEstudiante.estado_set.all()
#(7)***Returns orders customer name: (Query parent model values)
estado = Estado.objects.first() 
parentName = estado.customer.name
#(8)***Returns products from products table with value of "Out Door" in category attribute
trabajo = Trabajo.objects.filter(category="Pendiente")
#(9)***Order/Sort Objects by id
leastToGreatest = Trabajo.objects.all().estado_by('id') 
greatestToLeast = Trabajo.objects.all().estado_by('-id') 
#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
trabajoFiltered = Trabajo.objects.filter(tags__name="Programming")
'''
(11)Bonus
Q: Si un estudiante tiene mas de 1 trabajo, como podrias tu reflejar esto en la base de datos?
A: Porque aqui hay diferentes trabajos y este valor carga constantement, tu podrias gustar menos ir a la tienda,
 el valor en la base de datos pero -- solo hace esto una funcion nosotros podemos correr en cada tiempo, nosotros 
 cargamos los perfiles de los estudiantes
'''
#Returns the total count for number of time a "Ball" was ordered by the first customer
pendiantePractica = firstEstudiante.estado_set.filter(trabajo__name="Practica").count()
#Returns total count for each product orderd
allEstado = {}
for estado in firstEstudiante.estado_set.all():
	if estado.trabajo.name in allEstado:
		allEstado[estado.trabajo.name] += 1
	else:
		allEstado[estado.trabajo.name] = 1
#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}
#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()