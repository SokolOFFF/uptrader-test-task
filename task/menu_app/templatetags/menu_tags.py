from menu_app.models import Item
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    menu_items = Item.objects.filter(menu__name=name)
    if menu_items:
        menu = menu_items[0].menu
        local_context = {'menu' : menu}
        needed_item_url = context['request'].path
        if needed_item_url == '/':
            local_context['active_children'] = menu_items.filter(parent__uri=None)
        else:
            local_context['active_children'] = menu_items.filter(parent__uri=needed_item_url)
        try:
            active_item = menu_items.get(uri=needed_item_url)
        except ObjectDoesNotExist:
            pass
        else:
            unwrapped_menu_item_ids = active_item.get_parent_ids() + [active_item.id]
            unwrapped_menu_items = []
            for id in unwrapped_menu_item_ids:
                unwrapped_menu_items.append(menu_items.get(id=id))
            local_context['unwrapped_menu_items'] = unwrapped_menu_items
        return local_context
    else:
        raise template.TemplateSyntaxError('Did not find menu items')
