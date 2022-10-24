
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

            player.gui.screen["unnamed_0"].destroy()
            
            global.players[player.index].is_gui_open = false

        else
            --open the gui

            global.players[player.index].is_gui_open = true
            local root = player.gui.screen

            local unnamed_0 = root.add{type="frame",name="unnamed_0",direction="vertical"}
local unnamed_1 = unnamed_0.add{type="flow",name="unnamed_1"}
local unnamed_2 = unnamed_1.add{type="label",name="unnamed_2",style="frame_title",caption="titolo"}
local unnamed_3 = unnamed_1.add{type="empty-widget",name="unnamed_3"}
local unnamed_4 = unnamed_1.add{type="sprite-button",name="unnamed_4"}
local unnamed_5 = unnamed_0.add{type="frame",name="unnamed_5"}

        end


    end,

    on_event = function(event)
        --displatch the event to the custom functions

        
    end

    
}

return GUI
