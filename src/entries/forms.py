
# -*- encoding: utf-8 -*-

#=====================================================
# @file  :
# @brief :
#=====================================================

#--------- import ---------
from django import newforms as forms

#------------------------------------------------
# @class : UserRegistrationForm
# @brief : ユーザー登録用フォーム
#------------------------------------------------
class UserRegistrationForm( forms.Form ):

    #
    username = forms.CharField(
        required = True,
        max_length = 30,
        label = 'UserName' )

    #
    password = forms.CharField(
        required = True,
        max_length = 128,
        widget = forms.PasswordInput )

    #
    email = forms.EmailField(
        required = True,
        label = 'email address' )

# End of File
