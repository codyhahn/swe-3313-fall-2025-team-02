def ask_user(question):
    return input(question).strip().lower() == "y"


def get_rule(is_user, is_admin):
    if not is_user and not is_admin:
        return "R1"  # Guest
    elif is_user and not is_admin:
        return "R2"  # User
    elif is_user and is_admin:
        return "R3"  # Admin (inherits User)
    return "R4"      # Invalid scenario


def can_self_register(rule):
    return rule == "R1"


def can_login(rule):
    return rule in ("R2", "R3")


def can_view_inventory(rule):
    return rule in ("R2", "R3")


def can_search_inventory(rule):
    return rule in ("R2", "R3")


def can_purchase_items(rule):
    return rule in ("R2", "R3")


def can_export_sales(rule):
    return rule == "R3"


def can_run_reports(rule):
    return rule == "R3"


def can_manage_inventory(rule):
    return rule == "R3"


def main():
    is_user = ask_user("Is the person a User? (y/n): ")
    is_admin = ask_user("Is the person an Admin? (y/n): ")

    rule = get_rule(is_user, is_admin)

    print(f"\nApplying Rule: {rule}")
    print("================================")

    print(f"Self-Register:              {can_self_register(rule)}")
    print(f"Login:                      {can_login(rule)}")
    print(f"View Inventory:             {can_view_inventory(rule)}")
    print(f"Search Inventory:           {can_search_inventory(rule)}")
    print(f"Purchase Items:             {can_purchase_items(rule)}")
    print(f"Export Sales:               {can_export_sales(rule)}")
    print(f"Run Reports:                {can_run_reports(rule)}")
    print(f"Manage Inventory:           {can_manage_inventory(rule)}")


if __name__ == "__main__":
    main()
