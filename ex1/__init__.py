def make_items_list(list_of_ids, roles):
    list_of_items = []
    for i in list_of_ids:
        list_of_items.append(
            {
                "id": i,
                "text": roles.get(i).get("name")
            }
        )
    return list_of_items

def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    roles = mapping.get('roles')
    categories = mapping.get('categories')

    category_list = []
    for category in mapping.get("categoryIdsSorted"):
        category_list.append(
            {
                "id": "category-" + categories.get(category).get("id"),
                "text": categories.get(category).get("name"),
                "items": make_items_list(categories.get(category).get("roleIds"), roles)
            }
        )
    return {"categories": category_list}


