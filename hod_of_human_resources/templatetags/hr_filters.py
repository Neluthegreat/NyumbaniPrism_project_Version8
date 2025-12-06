from django import template
from django.template.defaultfilters import floatformat

register = template.Library()

@register.filter(name='calculate_percentage')
def calculate_percentage(value, total_dict):
    """
    Calculate the percentage of a value relative to the total.
    
    Usage: {{ count|calculate_percentage:department_headcount }}
    
    Args:
        value: The individual value (e.g., department count)
        total_dict: Dictionary containing all values to calculate total from
    
    Returns:
        Float percentage rounded to 2 decimal places
    """
    if not total_dict or not isinstance(total_dict, dict):
        return 0
    
    try:
        total = sum(total_dict.values())
        if total == 0:
            return 0
        
        percentage = (float(value) / float(total)) * 100
        return round(percentage, 2)
    except (ValueError, TypeError):
        return 0

@register.filter(name='percentage')
def percentage(value, total):
    """
    Simple percentage calculation filter.
    
    Usage: {{ value|percentage:total }}
    
    Args:
        value: The numerator
        total: The denominator
    
    Returns:
        Float percentage rounded to 2 decimal places
    """
    try:
        if float(total) == 0:
            return 0
        return round((float(value) / float(total)) * 100, 2)
    except (ValueError, TypeError):
        return 0
