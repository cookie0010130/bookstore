from django import forms
from order.models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='收件人')
    title = forms.ChoiceField(label='書　名',choices=[(0,'請選擇書名'),('傲慢與偏見 $284','傲慢與偏見'),('被討厭的勇氣  $237','被討厭的勇氣'),('福爾摩斯全集(套書) $980','福爾摩斯全集(套書)'),('HarryPotter $284','HarryPotter')])
    amount = forms.CharField(label='數　量')
    number = forms.CharField(label='連絡電話')
    
    
    class Meta:
        model = Product
        fields =  ['id','name','title','amount','number']