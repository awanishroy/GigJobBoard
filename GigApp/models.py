from django.db import models

class CbtFileData(models.Model):
    PR_FILE_ID = models.AutoField(primary_key=True)
    PR_FILE = models.FileField(upload_to='media/file-data/', null=True, blank=True)
    PR_META_TAG = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_file_data'

class CbtCountry(models.Model):
    PR_COUNTRY_ID = models.AutoField(primary_key=True)
    PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_country'

class CbtState(models.Model):
    PR_STATE_ID = models.AutoField(primary_key=True)
    PR_COUNTRY = models.ForeignKey(CbtCountry, on_delete=models.CASCADE)
    PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_state'

class CbtCity(models.Model):
    PR_CITY_ID = models.AutoField(primary_key=True)
    PR_STATE = models.ForeignKey(CbtState, on_delete=models.CASCADE, related_name='PR_CITY', null=True, blank=True)
    PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_city' 

class CbtDesignation(models.Model):
    PR_DESIGNATION_ID = models.BigAutoField(primary_key=True)
    PR_NAME = models.CharField(max_length=255, unique=True)
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DESCRIPTION = models.TextField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_designation'

class CbtDepartment(models.Model):
    PR_DEPARTMENT_ID = models.BigAutoField(primary_key=True)
    PR_NAME = models.CharField(max_length=255, unique=True)
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DESCRIPTION = models.TextField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_department'

class CbtDepartmentDesignation(models.Model):
    PR_ID = models.BigAutoField(primary_key=True)
    PR_DEPARTMENT = models.ForeignKey(CbtDepartment, on_delete=models.CASCADE, related_name='PR_DESIGNATIONS', null=True, blank=True)
    PR_DESIGNATION = models.ForeignKey(CbtDesignation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cbt_department_designation'

class CbtOrgType(models.Model):
    PR_ORG_TYPE_ID = models.AutoField(primary_key=True)
    PR_NAME = models.CharField(max_length=255, unique=True)
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=1)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateField(auto_now=True)

    class Meta:
        db_table = 'cbt_org_type'

class CbtOrgTypeDepartment(models.Model):
    PR_ID = models.BigAutoField(primary_key=True)
    PR_ORG_TYPE = models.ForeignKey(CbtOrgType, on_delete=models.CASCADE, related_name='PR_DEPARTMENTS', null=True, blank=True)
    PR_DEPARTMENT = models.ForeignKey(CbtDepartment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cbt_orgtype_department'

class CbtMenu(models.Model):
    PR_MENU_ID = models.BigAutoField(primary_key=True)
    PR_ORDER = models.IntegerField(null=True, blank=True, default=0)
    PR_NAME = models.CharField(max_length=255, unique=True)
    PR_CODE = models.CharField(max_length=255, unique=True)
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IS_VIEW = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FUNCTION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IS_HINDI = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=1)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateField(auto_now=True)

    class Meta:
        db_table = 'cbt_menu'

class CbtSubmenu(models.Model):
    PR_SUBMENU_ID = models.BigAutoField(primary_key=True)
    PR_MENU = models.ForeignKey(CbtMenu, on_delete=models.CASCADE, related_name='PR_SUBMENU')
    PR_ORDER = models.IntegerField(null=True, blank=True, default=0)
    PR_NAME = models.CharField(max_length=255)
    PR_CODE = models.CharField(max_length=255, unique=True)
    PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FUNCTION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IS_VIEW = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IS_HINDI = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_VIEW_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LIST_URL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FORM_URL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DELETE_URL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=1)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateField(auto_now=True)

    class Meta:
        db_table = 'cbt_submenu'

class CbtType(models.Model):
    PR_TYPE_ID = models.AutoField(primary_key=True)
    PR_NAME = models.CharField(max_length=255)
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_type'

class CbtDropdwonData(models.Model):
    PR_ID = models.AutoField(primary_key=True)
    PR_TYPE = models.ForeignKey(CbtType, on_delete=models.CASCADE)
    PR_NAME = models.CharField(max_length=255)
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_dropdown_data'

class CbtOrganization(models.Model):
    PR_ORGANIZATION_ID = models.BigAutoField(primary_key=True)
    PR_ORG_TYPE = models.ForeignKey(CbtOrgType, on_delete=models.CASCADE, null=True, blank=True)
    PR_DB_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DB_PASSWORD = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DB_USERNAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SALT_KEY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_TOKEN = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_UAN_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_NAME = models.CharField(max_length=255, unique=True, null=True, blank=True)
    PR_CODE = models.CharField(max_length=255, unique=True, null=True, blank=True)
    PR_OWNER_NAME = models.CharField(max_length=255, null=True, blank=True)
    PR_EMAIL = models.CharField(max_length=255, unique=True, null=True, blank=True)
    PR_PHONE = models.CharField(max_length=255, unique=True, null=True, blank=True)
    PR_STATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATE_CODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LICENCE_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CATEGORY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CNF_GROUP = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LEDGER_ACCOUNT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LOGIN_SEQUENCE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_NO_OF_ADMIN = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_USER_LIMIT = models.CharField(max_length=255, null=True, blank=True, default='') 
    PR_IMAGE_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LANGUAGE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_RELIGION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DOB = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_EMERGENCY_CONTACT_NO = models.CharField(max_length=255, null=True, blank=True, default='')

    # COMPANY INFORMATION
    PR_AADHAR_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AADHAR_FILE_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_GST_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CIN_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PAN_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PAN_FILE_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DL_NO1 = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DL_NO2 = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_TIN_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FSSAI_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FSSAI_DATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_MFG_LICENCE_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IMPORT_LICENCE_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_MEWS_FLASH = models.CharField(max_length=255, null=True, blank=True, default='')

    # BANK DETAILS
    PR_BANK_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BRANCH_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ACCOUNT_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IFSC_CODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ESI_APPLICABLE_IN_LAST = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ESI_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_MODIFIED_BY = models.CharField(max_length=255, null=True, blank=True, default='Super Admin')
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_organization'

class CbtOrganizationAddress(models.Model):
    PR_ID = models.AutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, related_name='PR_ORGANIZATION_ADDRESS', null=True, blank=True)
    PR_ADDRESS_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_COUNTRY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CITY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PINCODE = models.CharField(max_length=255, null=True, blank=True,  default='')
    PR_ADDRESS = models.TextField(null=True, blank=True,  default='')

    class Meta:
        db_table = 'cbt_organization_address'

class CbtOrganizationDirector(models.Model):
    PR_ID = models.AutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, related_name='PR_ORGANIZATION_DIRECTOR', null=True, blank=True)
    PR_DIRECTOR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DIN_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AUTH_SIGN1 = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DIRECTOR_PHOTO = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'cbt_organization_director'

class CbtAuthorizedSignature(models.Model):
    PR_ID = models.AutoField(primary_key=True)
    PR_COMPANY = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, related_name='PR_AUTHORIZED_SIGNATURE', null=True, blank=True)
    PR_ROLE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AUTH_SIGN2 = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STAMP_PHOTO = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'cbt_authorized_signature'

# MENU PERMISSION ORGANIZATION WISE
class CbtMenuPermissionOrganizationWise(models.Model):
    PR_ID = models.BigAutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE)
    PR_MENU = models.ForeignKey(CbtMenu, on_delete=models.CASCADE)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_ADD = models.IntegerField(null=True, blank=True, default=0)
    PR_VIEW = models.IntegerField(null=True, blank=True, default=0)
    PR_DELETE = models.IntegerField(null=True, blank=True, default=0)
    PR_EDIT = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_menu_permission_organization_wise'

# SUBMENU PERMISSION ORGANIZATION WISE
class CbtSubmenuPermissionOrganizationWise(models.Model):
    PR_ID = models.BigAutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE)
    PR_SUBMENU = models.ForeignKey(CbtSubmenu, on_delete=models.CASCADE)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_ADD = models.IntegerField(null=True, blank=True, default=0)
    PR_EDIT = models.IntegerField(null=True, blank=True, default=0)
    PR_VIEW = models.IntegerField(null=True, blank=True, default=0)
    PR_DELETE = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_submenu_permission_organization_wise'

# MENU PERMISSION DESIGNATION WISE
class CbtMenuPermissionDesignationWise(models.Model):
    PR_ID = models.BigAutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, null=True)
    PR_DEPARTMENT = models.ForeignKey(CbtDepartment, on_delete=models.CASCADE, null=True)
    PR_DESIGNATION = models.ForeignKey(CbtDesignation, on_delete=models.CASCADE)
    PR_MENU = models.ForeignKey(CbtMenu, on_delete=models.CASCADE)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_ADD = models.IntegerField(null=True, blank=True, default=0)
    PR_VIEW = models.IntegerField(null=True, blank=True, default=0)
    PR_DELETE = models.IntegerField(null=True, blank=True, default=0)
    PR_EDIT = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_menu_permission_designation_wise'

# SUBMENU PERMISSION DESIGNATION WISE
class CbtSubmenuPermissionDesignationWise(models.Model):
    PR_ID = models.BigAutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, null=True)
    PR_DEPARTMENT = models.ForeignKey(CbtDepartment, on_delete=models.CASCADE, null=True)
    PR_DESIGNATION = models.ForeignKey(CbtDesignation, on_delete=models.CASCADE)
    PR_SUBMENU = models.ForeignKey(CbtSubmenu, on_delete=models.CASCADE)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_ADD = models.IntegerField(null=True, blank=True, default=0)
    PR_EDIT = models.IntegerField(null=True, blank=True, default=0)
    PR_VIEW = models.IntegerField(null=True, blank=True, default=0)
    PR_DELETE = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_submenu_permission_designation_wise'

class CbtHeadquarter(models.Model):
    PR_HEADQUATER_ID = models.BigAutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, null=True, blank=True)
    PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DESCRIPTION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AREA = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ADDRESS = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PINCODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_headquarter'

class CbtUser(models.Model):
    PR_USER_ID = models.BigAutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, related_name='PR_USERS', null=True, blank=True)
    PR_HEADQUARTER = models.ForeignKey(CbtHeadquarter, on_delete=models.CASCADE, null=True, blank=True)
    PR_DEPARTMENT = models.ForeignKey(CbtDepartment, on_delete=models.CASCADE)
    PR_DESIGNATION = models.ForeignKey(CbtDesignation, on_delete=models.CASCADE)
    PR_REPORTING_MANAGER = models.IntegerField(null=True, blank=True, default=0)
    PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_REFERRAL_CODE = models.CharField(max_length=255, unique=True, null=True)
    PR_EMAIL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PHONE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PASSWORD = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PASSWORD_Hint = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ORG_EMAIL = models.CharField(max_length=255, null=True, blank=True, default='')

    PR_PIN = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IMEI = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PHONE_BRAND = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_OS = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_APP_VERSION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BATTERY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_TOKEN = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LOCATION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_QR_CODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_QR_CODE_TEXT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BARCODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BARCODE_TEXT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IS_LOGIN = models.BooleanField(default=False)
    PR_IS_ACTIVE = models.BooleanField(default=False)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cbt_user'

class CbtUserDetail(models.Model):
    PR_USER = models.OneToOneField(CbtUser, on_delete=models.CASCADE, related_name='PR_USER_DETAIL', null=True, blank=True)
    PR_FATHER_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_MOTHER_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SALT_KEY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BLOOD_GROUP = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_GENDER = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_HEIGHT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BODY_MARK = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_LANGUAGE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_EMPLOYEE_PHOTO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_RELIGION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CATEGORY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_QUALIFICATION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_MARIED_STATUS = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DOB = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_MARIAGE_DATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_EMERGENCY_CONTACT_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AADHAR_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AADHAR_FRONT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_AADHAR_BACK = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PAN_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PAN_FRONT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PAN_BACK = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DL_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DL_FRONT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DL_BACK = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PASSPORT_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PASSPORT_FRONT = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PASSPORT_BACK = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PF_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PF_APPLICABLE_IN_LAST = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BANK_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BRANCH_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_BANK_ACCOUNT_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_IFSC_CODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ACCOUNT_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ESI_NO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ESI_APPLICABLE_IN_LAST = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SALARY = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    PR_SALARY_STRUCTURE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DATE_OF_JOINING = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PROBATIONAL_DATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PROBATIONAL_NO_OF_DAYS = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SIGNATURE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SPECIALIZATION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_OFFER_LETTER = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_EXPERIENCE_LETTER = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SALARY_SLIP1 = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SALARY_SLIP2 = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SALARY_SLIP3 = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'cbt_user_detail'

class CbtUserAddress(models.Model):
    PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE, related_name='PR_USER_ADDRESS', null=True, blank=True)
    PR_ADDRESS_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_COUNTRY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_CITY = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PINCODE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ADDRESS = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'cbt_user_address'

class CbtUserActivity(models.Model):
    PR_ACTIVITY_ID = models.AutoField(primary_key=True)
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE)
    PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
    PR_LOCATION = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_IP_ADDRESS = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_LAT_LONG = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_BATTERY = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_OS = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_PHONE_BRAND = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_KM = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_ACTIVITY_TYPE = models.CharField(max_length=255, default='', null=True, blank=True)
    PR_STATUS = models.IntegerField(default=0, null=True, blank=True)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cbt_user_activity'

# ============ RECRUITMENT MODULES MODEL =============

class CbtCourse(models.Model):
  PR_COURSE_ID = models.BigAutoField(primary_key=True)
  PR_NAME = models.CharField(max_length=255)
  PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_course'

class CbtIndustry(models.Model):
  PR_INDUSTRY_ID = models.BigAutoField(primary_key=True)
  PR_NAME = models.CharField(max_length=255)
  PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_industry'

class CbtJobCategory(models.Model):
  PR_JOB_CATEGORY_ID = models.BigAutoField(primary_key=True)
  PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_job_category'

class CbtSkill(models.Model):
  PR_SKILL_ID = models.BigAutoField(primary_key=True)
  PR_JOB_CATEGORY = models.ForeignKey(CbtJobCategory, on_delete=models.CASCADE, related_name='PR_SKILLS')
  PR_NAME = models.CharField(max_length=255)
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_skill'

class CbtJobRole(models.Model):
  PR_ID = models.BigAutoField(primary_key=True)
  PR_NAME = models.CharField(max_length=255)
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_job_role'

class CbtJobPost(models.Model):
  PR_JOBPOST_ID = models.BigAutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE)
  PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
  PR_DEGREE = models.ForeignKey(CbtCourse, null=True, on_delete=models.CASCADE)
  PR_JOB_CATEGORY = models.ForeignKey(CbtJobCategory, null=True, on_delete=models.CASCADE)
  PR_JOB_ROLE = models.ForeignKey(CbtJobRole, null=True, on_delete=models.CASCADE)
  PR_JOB_TITLE = models.CharField(max_length=255)
  PR_JOB_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_JD_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_EMP_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_NO_OF_POSITION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_PRIORITY = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_SALARY_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_MIN_SALARY = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_MAX_SALARY = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_CURRENCY = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_MIN_EXP = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_MAX_EXP = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_SHIFT = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_TIME_OF_VALIDITY = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_ADDRESS = models.TextField(null=True, blank=True, default='')
  PR_STATE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_CITY = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_HIDE_SALARY = models.BooleanField(default=False)
  PR_HIDE_COMPANY_DETAIL = models.BooleanField(default=False)
  PR_WFH = models.BooleanField(default=False)
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_job_post'

# JOB SKILLS MODEL HERE
class CbtJobSkills(models.Model):
  PR_ID = models.BigAutoField(primary_key=True)
  PR_JOBPOST = models.ForeignKey(CbtJobPost, on_delete=models.CASCADE, related_name='PR_JOB_SKILLS', null=True, blank=True)
  PR_SKILL = models.ForeignKey(CbtSkill, on_delete=models.CASCADE)
  PR_STATUS = models.IntegerField(null=True, blank=True, default=1)

  class Meta:
    db_table = 'cbt_job_skills'

# JOB APPLY  MODEL HERE
class CbtJobApply(models.Model):
  PR_APPLY_ID = models.BigAutoField(primary_key=True)
  PR_JOBPOST = models.ForeignKey(CbtJobPost, on_delete=models.CASCADE)
  PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
  PR_APPLY_DATE = models.DateField(auto_now_add=True)
  PR_APPLY_TIME = models.TimeField(auto_now_add=True)
  PR_EXPERIENCE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_CURRENT_CTC = models.CharField(max_length=15, null=True, blank=True, default='')
  PR_EXPECTED_CTC = models.CharField(max_length=15, null=True, blank=True, default='')
  PR_RESUME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_job_apply'

# ================== MODELS FOR PORTFOLIO ==================
class CbtWebsiteData(models.Model):
  PR_WEBSITE_ID = models.AutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE)
  PR_NAME = models.CharField(max_length=255)
  PR_LOGO = models.CharField(max_length=255, null=True, blank=True, default='/media/default-img.png')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_website_data'

class CbtContactData(models.Model):
  PR_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_CONTACT_DATA')
  PR_ADDRESS = models.TextField(null=True, blank=True, default='')
  PR_EMAIL = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_PHONE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_contact_data'

class CbtSocialMedia(models.Model):
  PR_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_SOCIAL_MEDIA_DATA')
  PR_NAME = models.CharField(max_length=255)
  PR_URL = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_social_media'

class CbtBanner(models.Model):
  PR_BANNER_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_BANNERS')
  PR_TITLE = models.CharField(max_length=255)
  PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_IMAGE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_banner'
  
class CbtPage(models.Model):
  PR_PAGE_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_PAGES')
  PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_CONTENT = models.TextField(null=True, blank=True, default='')
  PR_THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_page'

class CbtServiceCategory(models.Model):
  PR_CATEGORY_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE)
  PR_NAME = models.CharField(max_length=255)
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_service_category'

class CbtService(models.Model):
  PR_SERVICE_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_SERVICES')
  PR_CATEGORY = models.ForeignKey(CbtServiceCategory, on_delete=models.CASCADE)
  PR_NAME = models.CharField(max_length=255)
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_CONTENT = models.TextField(null=True, blank=True, default='')
  PR_THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_service'

class CbtOurAchievement(models.Model):
    PR_ACHIEVEMENT_ID = models.AutoField(primary_key=True)
    PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_ACHIEVEMENTS')
    PR_TITLE = models.CharField(max_length=255)
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_URL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_our_achievement'

class CbtOurTeam(models.Model):
    PR_MEMBER_ID = models.AutoField(primary_key=True)
    PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_TEAM_MEMBERS')
    PR_NAME = models.CharField(max_length=255)
    PR_ROLE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PHOTO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_ABOUT = models.TextField(null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_our_team'

class CbtMarketingProject(models.Model):
  PR_PROJECT_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_MARKETING_PROJECTS')
  PR_NAME = models.CharField(max_length=255)
  PR_TITLE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_THUMBNAIL = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
      db_table = 'cbt_marketing_project'

class CbtMarketingProjectImages(models.Model):
    PR_IMAGE_ID = models.AutoField(primary_key=True)
    PR_MARKETING_PROJECT = models.ForeignKey(CbtMarketingProject, on_delete=models.CASCADE, null=True, blank=True, related_name='PR_IMAGES')
    PR_TITLE = models.CharField(max_length=255)
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_IMAGE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=1)
    
    class Meta:
        db_table = 'cbt_marketing_project_images'

class CbtClientReview(models.Model):
    PR_REVIEW_ID = models.AutoField(primary_key=True)
    PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_CLIENT_REVIEWS')
    PR_NAME = models.CharField(max_length=255)
    PR_EMAIL = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_PHOTO = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_RATING = models.IntegerField(null=True, blank=True, default=0)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_client_review'

class CbtOurClient(models.Model):
  PR_CLIENT_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_OUR_CLIENTS')
  PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_our_client'

class CbtOurProduct(models.Model):
  PR_PRODUCT_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_OUR_PRODUCTS')
  PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_our_product'

class CbtOurProject(models.Model):
  PR_PROJECT_ID = models.AutoField(primary_key=True)
  PR_WEBSITE = models.ForeignKey(CbtWebsiteData, on_delete=models.CASCADE, related_name='PR_OUR_PROJECTS')
  PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_ICON = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_our_project'

# SURVEY  MODEL HERE
class CbtSurvey(models.Model):
  PR_SURVEY_ID = models.BigAutoField(primary_key=True)
  PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
  PR_SHOP_NAME = models.CharField(max_length=255, null=True, blank=True)
  PR_OWNER_NAME = models.CharField(max_length=255, null=True, blank=True)
  PR_EMAIL = models.CharField(max_length=255,  null=True, blank=True)
  PR_PHONE = models.CharField(max_length=255,  null=True, blank=True)
  PR_LOCATION = models.CharField(max_length=255,  null=True, blank=True)
  PR_IMAGES = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_LATITUDE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_LONGITUDE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_survey'

# USER REVIEW  MODEL HERE
class CbtUserReview(models.Model):
    PR_REVIEW_ID = models.AutoField(primary_key=True)
    PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
    PR_JOBPOST = models.ForeignKey(CbtJobPost, on_delete=models.CASCADE)
    PR_RATING = models.FloatField(null=True, blank=True, default=0.0)
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cbt_user_review'
      
# TRAINING SESSION MODEL HERE
class CbtTrainingSession(models.Model):
    PR_ID = models.AutoField(primary_key=True)
    PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE,null=True, blank=True, default='')
    PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE,null=True, blank=True, default='')
    PR_TITLE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
    PR_LOCATION = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_SESSION_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_MAX_PARTICIPANTS = models.IntegerField(null=True, blank=True, default=0)
    PR_IMAGE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FILE_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_FILE = models.CharField(max_length=255, null=True, blank=True, default='')
    PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
    PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
    PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
    PR_MODIFIED_BY = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'cbt_training_session'
        
# QUESTION MODEL HERE
class CbtQuestion(models.Model):
  PR_QUESTION_ID = models.AutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_QUESTION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_FIRST_OPTION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_SECOND_OPTION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_THIRD_OPTION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_FORTH_OPTION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
      db_table = 'cbt_question'

# ASSESMENT MODEL HERE
class CbtAssesment(models.Model):
  PR_ASSESMENT_ID = models.AutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
  PR_JOBPOST = models.ForeignKey(CbtJobPost, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_TYPE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
      db_table = 'cbt_assesment'

#ASSESMENT QUESTION MODEL HERE
class CbtAssesmentsQuestion(models.Model):
  PR_ID = models.BigAutoField(primary_key=True)
  PR_ASSESMENT = models.ForeignKey(CbtAssesment, on_delete=models.CASCADE, related_name='PR_ASSESMENT', null=True, blank=True)
  PR_QUESTION = models.ForeignKey(CbtQuestion, on_delete=models.CASCADE)  
  PR_STATUS = models.IntegerField(null=True, blank=True, default=1)

  class Meta:
    db_table = 'cbt_assesment_question'

#ANSWERS MODEL HERE
class CbtAnswers(models.Model):
  PR_ANSWER_ID = models.BigAutoField(primary_key=True)
  PR_ASSESMENT = models.ForeignKey(CbtAssesment, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
  PR_QUESTION = models.ForeignKey(CbtQuestion, on_delete=models.CASCADE, null=True, blank=True)
  PR_ANSWER = models.CharField(max_length=255, null=True, blank=True, default='')  
  PR_REVIEW = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=1)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)
  
  class Meta:
    db_table = 'cbt_answer'
    
#==================== SUBSCRIPTIONS PLAN ==========================#
class CbtSubscriptionPlan(models.Model):
  PR_SUBSCRIPTION_ID = models.AutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_NAME = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_IMAGE_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DURATION = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_PRICE = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
  PR_OFFER_PRICE = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
  PR_DISCOUNT_PRICE = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_BG_COLOR = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_subscription_plan'
    

#========================= SUBSCRIPTION TERM AND CONDITION =====================#
class CbtTermAndCondition(models.Model):
  PR_ID = models.AutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE,null=True, blank=True, default='')
  PR_SUBSCRIPTION = models.ForeignKey(CbtSubscriptionPlan, on_delete=models.CASCADE, related_name='PR_TERM_AND_CONDITIONS')
  PR_TITLE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_DESCRIPTION = models.TextField(null=True, blank=True, default='')
  PR_IMAGE_PATH = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_term_and_condition'
    
#============================= SUBSCRIPTION PLAN ORDER =========================#
class CbtSubscriptionPlanOrder(models.Model):
  PR_ID = models.AutoField(primary_key=True)
  PR_ORGANIZATION = models.ForeignKey(CbtOrganization, on_delete=models.CASCADE, related_name='PR_SUBSCRIPTION_ORDERS')
  PR_SUBSCRIPTION = models.ForeignKey(CbtSubscriptionPlan, on_delete=models.CASCADE)
  PR_ORDER_ID = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_ORDER_VALUE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_EXPAIRE_DATE = models.CharField(max_length=255, null=True, blank=True, default='')
  PR_STATUS = models.IntegerField(null=True, blank=True, default=0)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_subscription_plan_order'
    
    
#POINTS MODEL HERE 
class CbtPoints(models.Model):
  PR_ID = models.AutoField(primary_key=True)
  PR_USER = models.ForeignKey(CbtUser, on_delete=models.CASCADE)
  PR_REFERRAL = models.ForeignKey(CbtUser, on_delete=models.CASCADE, related_name='PR_REFERRAL', null=True, blank=True)
  PR_POINTS = models.IntegerField(null=True, blank=True, default=100)
  PR_STATUS = models.IntegerField(null=True, blank=True, default=1)
  PR_CREATED_AT = models.DateTimeField(auto_now_add=True)
  PR_MODIFIED_AT = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'cbt_points'