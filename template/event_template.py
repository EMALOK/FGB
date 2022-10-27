event_template = r"""
script.on_event(defines.events.{%event_name%},function(event)
    {%event_body%}
end)
"""

event_element_template = r"""
if event.element.name == "{%element_name%}" then
    {%event_element_body%}
end
"""