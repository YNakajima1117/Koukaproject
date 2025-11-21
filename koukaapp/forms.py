from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="名前")
    email = forms.EmailField(label="メールアドレス")
    phone = forms.CharField(label="電話番号")
    message = forms.CharField(label="メッセージ",widget=forms.Textarea)
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["name"].widget.attrs["placeholder"]="plz write your name here"
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["id"] = "name"
        self.fields["email"].widget.attrs["placeholder"]="plz write your email here"
        self.fields["email"].widget.attrs["class"] = "form-control"
        self.fields["email"].widget.attrs["id"] = "email"
        self.fields["phone"].widget.attrs["placeholder"]="plz write your phone number here"
        self.fields["phone"].widget.attrs["class"] = "form-control"
        self.fields["phone"].widget.attrs["id"] = "phone"
        self.fields["message"].widget.attrs["placeholder"]="plz write message here"
        self.fields["message"].widget.attrs["class"] = "form-control"
        self.fields["message"].widget.attrs["id"] = "message"
        self.fields["message"].widget.attrs["style"] = "height: 10rem"