local GUI = {

    is_open = false,

    init = function()
        global.players = {}
    end,

    setup_new_player = function(event)
        global.players[player.index] = {is_gui_open = false}
    end,

    toggle_gui = function(player)

        if global.players[player.index].is_gui_open then
            --close the gui
            
            global.players[player.index].is_gui_open = false

        else
            --open the gui

            global.players[player.index].is_gui_open = true

            local root = player.gui.screen
            local main_frame = root.add { type = "frame", name = "main_frame", caption = "gui_title" }
            local unnamed_0 = main_frame.add { type = "frame", name = "unnamed_0", direction = "vertical" }
            local row_flow = unnamed_0.add { type = "flow", name = "row_flow", direction = "horizontal" }
            local unnamed_1 = row_flow.add { type = "button", name = "unnamed_1", caption = "button_text" }
            local unnamed_2 = row_flow.add { type = "button", name = "unnamed_2", caption = "button_text" }
            local unnamed_3 = unnamed_0.add { type = "button", name = "unnamed_3", caption = "button_text" }
            local unnamed_4 = unnamed_0.add { type = "line", name = "unnamed_4" }
            local unnamed_5 = unnamed_0.add { type = "flow", name = "unnamed_5" }
            local unnamed_6 = unnamed_5.add { type = "button", name = "unnamed_6" }
        end


    end,

    on_event = function(event)
        --displatch the event to the custom functions
    end,

    --example
    skip_button_on_click = function ()

    end,
}
