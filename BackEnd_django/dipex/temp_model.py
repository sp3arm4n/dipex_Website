# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class KdAdmMenu(models.Model):
    menu_sid = models.AutoField(db_column='MENU_SID', primary_key=True)  # Field name made lowercase.
    menu_nm = models.CharField(db_column='MENU_NM', max_length=50)  # Field name made lowercase.
    menu_uri = models.CharField(db_column='MENU_URI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    parent_menu = models.IntegerField(db_column='PARENT_MENU', blank=True, null=True)  # Field name made lowercase.
    is_del = models.CharField(db_column='IS_DEL', max_length=1)  # Field name made lowercase.
    code_sid = models.IntegerField(db_column='CODE_SID', blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.
    chg_dt = models.DateTimeField(db_column='CHG_DT')  # Field name made lowercase.
    chg_ip = models.CharField(db_column='CHG_IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    exp_ord = models.IntegerField(db_column='EXP_ORD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_adm_menu'


class KdAdmRight(models.Model):
    mem_sid = models.IntegerField(db_column='MEM_SID', primary_key=True)  # Field name made lowercase.
    menu_sid = models.IntegerField(db_column='MENU_SID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_adm_right'
        unique_together = (('mem_sid', 'menu_sid'),)


class KdBbs(models.Model):
    bbs_sid = models.AutoField(db_column='BBS_SID', primary_key=True)  # Field name made lowercase.
    bbs_cd = models.CharField(db_column='BBS_CD', max_length=30)  # Field name made lowercase.
    top_cd = models.IntegerField(db_column='TOP_CD', blank=True, null=True)  # Field name made lowercase.
    high_cd = models.IntegerField(db_column='HIGH_CD', blank=True, null=True)  # Field name made lowercase.
    low_cd = models.IntegerField(db_column='LOW_CD', blank=True, null=True)  # Field name made lowercase.
    exp_cd = models.IntegerField(db_column='EXP_CD', blank=True, null=True)  # Field name made lowercase.
    age_cd = models.IntegerField(db_column='AGE_CD', blank=True, null=True)  # Field name made lowercase.
    media_div = models.IntegerField(db_column='MEDIA_DIV', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=300)  # Field name made lowercase.
    contents = models.TextField(db_column='CONTENTS')  # Field name made lowercase.
    profile = models.TextField(db_column='PROFILE', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='SUBJECT', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    orgn = models.CharField(db_column='ORGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    interview_dt = models.CharField(db_column='INTERVIEW_DT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    interview_age = models.IntegerField(db_column='INTERVIEW_AGE', blank=True, null=True)  # Field name made lowercase.
    diag_age = models.IntegerField(db_column='DIAG_AGE', blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=300, blank=True, null=True)  # Field name made lowercase.
    is_main = models.CharField(db_column='IS_MAIN', max_length=1)  # Field name made lowercase.
    is_del = models.CharField(db_column='IS_DEL', max_length=1)  # Field name made lowercase.
    mem_sid = models.IntegerField(db_column='MEM_SID')  # Field name made lowercase.
    mem_nm = models.CharField(db_column='MEM_NM', max_length=10)  # Field name made lowercase.
    read_cnt = models.IntegerField(db_column='READ_CNT')  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.
    chg_dt = models.DateTimeField(db_column='CHG_DT')  # Field name made lowercase.
    chg_ip = models.CharField(db_column='CHG_IP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    personal_cd = models.CharField(db_column='PERSONAL_CD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    personal_sid = models.IntegerField(db_column='PERSONAL_SID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_bbs'


class KdBbsCmt(models.Model):
    bbs_sid = models.IntegerField(db_column='BBS_SID', primary_key=True)  # Field name made lowercase.
    cmt_sid = models.AutoField(db_column='CMT_SID')  # Field name made lowercase.
    contents = models.TextField(db_column='CONTENTS')  # Field name made lowercase.
    mem_sid = models.IntegerField(db_column='MEM_SID')  # Field name made lowercase.
    mem_nm = models.CharField(db_column='MEM_NM', max_length=10)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_bbs_cmt'
        unique_together = (('bbs_sid', 'cmt_sid'),)


class KdBbsFile(models.Model):
    bbs_sid = models.IntegerField(db_column='BBS_SID', primary_key=True)  # Field name made lowercase.
    file_sid = models.IntegerField(db_column='FILE_SID')  # Field name made lowercase.
    save_path = models.CharField(db_column='SAVE_PATH', max_length=100)  # Field name made lowercase.
    save_name = models.CharField(db_column='SAVE_NAME', max_length=50)  # Field name made lowercase.
    file_size = models.IntegerField(db_column='FILE_SIZE')  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=100)  # Field name made lowercase.
    file_div = models.IntegerField(db_column='FILE_DIV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_bbs_file'
        unique_together = (('bbs_sid', 'file_sid'),)


class KdCode(models.Model):
    code_sid = models.AutoField(db_column='CODE_SID', primary_key=True)  # Field name made lowercase.
    code_nm = models.CharField(db_column='CODE_NM', max_length=50)  # Field name made lowercase.
    code_grp = models.CharField(db_column='CODE_GRP', max_length=30)  # Field name made lowercase.
    parent_code = models.IntegerField(db_column='PARENT_CODE', blank=True, null=True)  # Field name made lowercase.
    exp_ord = models.IntegerField(db_column='EXP_ORD')  # Field name made lowercase.
    is_exp = models.CharField(db_column='IS_EXP', max_length=1)  # Field name made lowercase.
    is_del = models.CharField(db_column='IS_DEL', max_length=1)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.
    chg_dt = models.DateTimeField(db_column='CHG_DT')  # Field name made lowercase.
    chg_ip = models.CharField(db_column='CHG_IP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_code'


class KdInterview(models.Model):
    inv_sid = models.AutoField(db_column='INV_SID', primary_key=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='PHONE_NO', max_length=20)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='MOBILE_NO', max_length=20)  # Field name made lowercase.
    ill_div = models.IntegerField(db_column='ILL_DIV')  # Field name made lowercase.
    home_time = models.IntegerField(db_column='HOME_TIME')  # Field name made lowercase.
    contents = models.TextField(db_column='CONTENTS')  # Field name made lowercase.
    mem_sid = models.IntegerField(db_column='MEM_SID', blank=True, null=True)  # Field name made lowercase.
    is_del = models.CharField(db_column='IS_DEL', max_length=1)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.
    chg_dt = models.DateTimeField(db_column='CHG_DT')  # Field name made lowercase.
    chg_ip = models.CharField(db_column='CHG_IP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_interview'


class KdMember(models.Model):
    mem_sid = models.AutoField(db_column='MEM_SID', primary_key=True)  # Field name made lowercase.
    mem_div = models.IntegerField(db_column='MEM_DIV')  # Field name made lowercase.
    login_id = models.CharField(db_column='LOGIN_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    login_pwd = models.CharField(db_column='LOGIN_PWD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mem_nm = models.CharField(db_column='MEM_NM', max_length=10)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50)  # Field name made lowercase.
    phone_no = models.CharField(db_column='PHONE_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mobile_no = models.CharField(db_column='MOBILE_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resch_grd = models.IntegerField(db_column='RESCH_GRD', blank=True, null=True)  # Field name made lowercase.
    orgn_nm = models.CharField(db_column='ORGN_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    major_nm = models.CharField(db_column='MAJOR_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resch_div = models.CharField(db_column='RESCH_DIV', max_length=100, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(db_column='PHOTO', max_length=300, blank=True, null=True)  # Field name made lowercase.
    is_use = models.CharField(db_column='IS_USE', max_length=1)  # Field name made lowercase.
    is_del = models.CharField(db_column='IS_DEL', max_length=1)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.
    chg_dt = models.DateTimeField(db_column='CHG_DT')  # Field name made lowercase.
    chg_ip = models.CharField(db_column='CHG_IP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_member'


class KdOpinion(models.Model):
    opn_sid = models.AutoField(db_column='OPN_SID', primary_key=True)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=1)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    live_area = models.IntegerField(db_column='LIVE_AREA')  # Field name made lowercase.
    job = models.IntegerField(db_column='JOB')  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.
    reg_ip = models.CharField(db_column='REG_IP', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_opinion'


class KdOpinionState(models.Model):
    opn_sid = models.IntegerField(db_column='OPN_SID', primary_key=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='STATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kd_opinion_state'
        unique_together = (('opn_sid', 'state'),)
