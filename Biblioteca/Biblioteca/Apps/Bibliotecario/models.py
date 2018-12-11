from django.db import models

# Create your models here.
class Persona(models.Model):
	Nombres = models.CharField(max_length=20)
	ApellidoPaterno = models.CharField(max_length=35)
	ApellidoMaterno = models.CharField(max_length=35)
	DNI = models.CharField(max_length=10)
	Dedicación = models.CharField(max_length=25)  
	SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
	Sexo = models.CharField(max_length=1, choices=SEXOS, default= 'M')

	def NombreCompleto(self):
		cadena = "{0} {1}, {2}"
		return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

	def __str__(self):
		return self.NombreCompleto()

class Categorias(models.Model):
	Nombre = models.CharField(max_length = 20)
	Disponible  =models.BooleanField(default =True)

	def __str__(self):
		return"{0} ({1})".format(self.Nombre, self.Disponible)


class Libro(models.Model):
	NombreL = models.CharField(max_length=30)
	Editorial = models.CharField(max_length = 30)
	Autor = models.CharField(max_length = 20)
	NumeroPag = models.CharField(max_length = 10)


	def FichaBibliografica(self):
		cadenaf = "{0} {1}, {2} ({3})"
		return cadenaf.format(self.NombreL, self.Autor, self.Editorial, self.NumeroPag)

	def __str__(self):
		return self.FichaBibliografica()

class Prestamo(models.Model):
	Persona=models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
	Categorias=models.ForeignKey(Categorias, null=False, blank=False, on_delete=models.CASCADE)
	FechaMatricula=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		cadenaP = "{0} => {1}"
		return cadenaP.format(self.Persona, self.Categorias.Nombre)

class Registro(models.Model):
	Categorias=models.ForeignKey(Categorias, null=False, blank=False, on_delete=models.CASCADE)
	Libro=models.ForeignKey(Libro, null=False, blank=False, on_delete=models.CASCADE)
	FechaMatricula=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		cadenaR = "{0} => {1}"
		return cadenaR.format(self.Libro, self.Categorias.Nombre)