from django.db import models

import hashlib
import time
import jwt

# Create your models here.

class HashedAutoField(models.AutoField):
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is None:
            return value
        return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

# to define common fields or functionality that will be shared by all the models that inherit from it.   
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
          
class ReportEngine(BaseModel, models.Model):
    # id = HashedAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    type = models.CharField(
        choices=(("metabase", "Metabase"),), default="metabase", max_length=50)
    base_url = models.URLField()
    integration_api_key = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    
class EmbeddedReport(BaseModel, models.Model):
    # id = HashedAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    engine = models.ForeignKey(ReportEngine, on_delete=models.PROTECT)
    reference_id = models.CharField(
        help_text="Report ID on the engine, like question id, dashboard id on Metabase",
        max_length=50,
    )
    reference_type = models.CharField(
        choices=(
            ("single_report", "Question/Single Report"),
            ("dashboard", "Dashboard"),
        ),
        max_length=50,
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_report_url_for_business(self, business):
        map_resource = {
            "dashboard": {
                "params": {"dashboard": int(self.reference_id)},
                "url_path": "dashboard",
            },
            "single_report": {
                "params": {"question": int(self.reference_id)},
                "url_path": "question",
            },
        }

        resource = map_resource[self.reference_type]

        payload = {
            "resource": resource["params"],
            "params": {"organization_id": business.organization_id},
            "exp": round(time.time()) + (60 * 10),  # 10 minute expiration
        }

        token = jwt.encode(
            payload, self.engine.integration_api_key, algorithm="HS256"
        ).decode("utf8")

        return "{}/embed/{}/{}#bordered=false&titled=false".format(
            self.engine.base_url, resource["url_path"], token
        )
    
    
'''
The HashedAutoField is a custom field type that is defined in your code. 
It is a subclass of the built-in models.AutoField field and adds the necessary 
logic to generate a hash of the field value before storing it in the database.

In the HashedAutoField class, the get_prep_value method is overridden to generate 
the hash using the hashlib module. The get_prep_value method is called by Django when the
model instance is saved to the database, and it is used to convert the field value to a 
format that can be stored in the database.

In the example you provided, the HashedAutoField is used as the id field for the 
ReportEngine and EmbeddedReport models. The id field is a primary key field, 
which means that it is used to uniquely identify each record in the database table. 
By using the HashedAutoField as the id field, the primary key values will be hashed 
before they are stored in the database, 
rather than being auto-incremented integer values as is the case with the built-in models.AutoField.
'''