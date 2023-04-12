from django import forms




class GastosFormulario(forms.Form):
    Tipo = forms.CharField(max_length=20)
    Articulo =  forms.CharField(max_length=20)
    Cantidad = forms.IntegerField()
    Precio = forms.DecimalField(max_digits=10, decimal_places=2)
  
    

    
class BuscarGastos(forms.Form):
    Tipo = forms.CharField(max_length=20, required=False)
    Articulo =  forms.CharField(max_length=20)
    Cantidad = forms.IntegerField()
    Precio = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
  
    
    
    