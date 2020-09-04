from django.db import models
from django.contrib.auth.models import User
import os
import random
# Create your models here.


def get_filename_ext(filepath):
    """
    TO get File Name anf File Extentation
    """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    """
    TO upload images in media folder for user profile
    """
    new_filename = str(instance.c_name) + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Company/{final_filename}".format(final_filename=final_filename)

def upload_ppt_path(instance, filename):
    """
    TO upload PPT file in Company/Product/PPT folder
    """
    new_filename = str(instance.p_name) + "_" + "ppt" + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Company/Product/PPT/{final_filename}".format(final_filename=final_filename)

def upload_pdf_path(instance, filename):
    """
    TO upload PDF file in Company/Product/PDF folder
    """
    new_filename = str(instance.p_name) + "_" + "pdf" + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Company/Product/PDF/{final_filename}".format(final_filename=final_filename)

def upload_product_img_path(instance, filename):
    """
    TO upload Image file in Company/Product/IMAGES folder
    """
    new_filename = str(instance.p_name) + "_" + "img" + "_" + str(random.randint(1,1000))
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "Company/Product/IMAGES/{final_filename}".format(final_filename=final_filename)



class Register(models.Model):
    c_name = models.CharField(max_length = 50, unique = True)
    c_email = models.EmailField()
    c_password = models.CharField(max_length = 16)
    c_r_password = models.CharField(max_length = 16)
    c_verification_flag = models.BooleanField()

    def __str__(self):
        return self.c_name


class Company_Profile(models.Model):
    c_email = models.EmailField(unique= True)
    c_name = models.CharField(max_length = 50)
    c_phone = models.CharField(max_length = 10)
    c_street = models.TextField()
    c_area = models.TextField()
    c_city = models.TextField()
    c_state = models.TextField()
    c_country = models.TextField()
    c_pincode = models.CharField(max_length = 6)
    c_logo = models.ImageField(upload_to = upload_image_path)
    c_website = models.URLField(max_length = 200)
    c_linkedin = models.URLField(max_length = 200)

    def __str__(self):
        return self.c_name




class Product_Catagory(models.Model):
    catagory_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.catagory_name



class Product_Hardware(models.Model):
    p_company_id = models.CharField(max_length = 20)
    p_name = models.CharField(max_length = 50)
    p_model_no = models.CharField(max_length = 20)
    p_bio = models.TextField()
    p_manufacturing_date = models.DateField()
    p_img_1 = models.ImageField(upload_to= upload_product_img_path)
    p_img_2 = models.ImageField(upload_to= upload_product_img_path)
    p_img_3 = models.ImageField(upload_to= upload_product_img_path, null=True, blank=True)
    p_img_4 = models.ImageField(upload_to= upload_product_img_path, null=True, blank=True)
    p_img_5 = models.ImageField(upload_to= upload_product_img_path, null=True, blank=True)
    p_img_6 = models.ImageField(upload_to= upload_product_img_path, null=True, blank=True)
    p_catagory = models.ForeignKey(Product_Catagory, on_delete = models.CASCADE)
    p_price = models.DecimalField(max_digits = 10, decimal_places = 2)
    P_warranty = models.DecimalField(max_digits = 4, decimal_places = 2)
    p_replace_time = models.CharField(max_length = 3)
    p_ppt = models.FileField( upload_to=upload_ppt_path, null= True, blank= True)
    p_pdf = models.FileField(upload_to = upload_pdf_path,null=True, blank=True)
    p_blog_link = models.URLField(null=True, blank=True)
    p_youtube_link = models.URLField(null=True, blank=True)
    p_software_link = models.URLField(max_length = 200, null=True, blank= True)
    p_feature_1 = models.CharField(max_length = 300)
    p_feature_2 = models.CharField(max_length=300)
    p_feature_3 = models.CharField(max_length=300, null=True, blank=True)
    p_feature_4 = models.CharField(max_length=300, null=True, blank=True)
    p_feature_5 = models.CharField(max_length=300, null=True, blank=True)
    p_feature_6 = models.CharField(max_length=300, null=True, blank=True)
    p_creation_date = models.DateTimeField(auto_now_add= True)
    p_updated_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.p_name



class Product_software(models.Model):
    software_name = models.CharField(max_length = 50)
    company_id = models.CharField(max_length = 20)
    hardware_product = models.ForeignKey(Product_Hardware, on_delete=models.CASCADE)
    software_link = models.URLField()
    youtube_link = models.URLField()
    p_feature_1 = models.CharField(max_length=300)
    p_feature_2 = models.CharField(max_length=300)
    p_feature_3 = models.CharField(max_length=300, null=True, blank=True)
    p_feature_4 = models.CharField(max_length=300, null=True, blank=True)
    p_feature_5 = models.CharField(max_length=300, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.software_name


class Product_Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    product = models.ForeignKey(Product_Hardware, on_delete = models.CASCADE)
    user_name = models.CharField(max_length = 20)
    user_email = models.EmailField()
    product_name = models.CharField(max_length = 20)
    message = models.TextField()
    submited_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user_name + " / " + self.product_name
