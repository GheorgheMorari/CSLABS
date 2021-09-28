import winreg


# TODO create file menu DONE
# TODO export json data to a function in this file DONE
# TODO get every custom item in the exported json DONE
# TODO make a custom evaluation for each check type:
# REGISTRY_SETTING
# USER_RIGHTS_POLICY
# LOCKOUT_POLICY
# AUDIT_POLICY_SUBCATEGORY
# REG_CHECK
# PASSWORD_POLICY
# WMI_POLICY

# TODO evaluate each type of check
# TODO take account which custom items failed
# TODO create new frame which displays what check passed and failed, make the failed checks be first


def check_custom_item(custom_item_dict) -> bool:
    return switch_dict[custom_item_dict['type']](custom_item_dict)


def check_registry_setting(custom_item_dict) -> bool:
    if 'check_type' in custom_item_dict:
        if custom_item_dict['check_type'] == 'CHECK_REGEX':
            access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            access_key = winreg.OpenKey(access_registry, custom_item_dict['reg_key'].strip('"').replace("HKLM",""))

    return False


def check_user_right_policy(custom_item_dict):
    pass


def check_lookout_policy(custom_item_dict):
    pass


def check_audit_subcategory(custom_item_dict):
    pass


def check_reg_check(custom_item_dict):
    pass


def check_password_policy(custom_item_dict):
    pass


def check_wmi_policy(custom_item_dict):
    pass


switch_dict = {
    'REGISTRY_SETTING': check_registry_setting,
    'USER_RIGHTS_POLICY': check_user_right_policy,
    'LOCKOUT_POLICY': check_lookout_policy,
    'AUDIT_POLICY_SUBCATEGORY': check_audit_subcategory,
    'REG_CHECK': check_reg_check,
    'PASSWORD_POLICY': check_password_policy,
    'WMI_POLICY': check_wmi_policy
}
