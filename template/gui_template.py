gui_template = r"""
local GUI = {

    init = function(self)
        global.players = {}

        script.on_event(defines.events.on_player_created,function(event)
            global.players[event.player_index] = { is_gui_open = false }
        end)

        {%bind_events%}
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

            {%extra_code%}
        end

    end
}

return GUI
"""