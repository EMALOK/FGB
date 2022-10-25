gui_template = r"""
local GUI = {

    is_open = false,

    init = function()
        global.players = {}
    end,

    setup_new_player = function(player_index)
        global.players[player_index] = { is_gui_open = false }
    end,

    toggle_gui = function(player)

        if global.players[player.index].is_gui_open then
            --close the gui

            player.gui.screen["{%gui_name%}"].destroy()
            
            global.players[player.index].is_gui_open = false

        else
            --open the gui

            global.players[player.index].is_gui_open = true
            local root = player.gui.screen

            {%gui_build%}
        end


    end,

    on_event = function(event)
        --displatch the event to the custom functions

        {%gui_events_dispatch%}
    end

    {%gui_events%}
}

return GUI
"""