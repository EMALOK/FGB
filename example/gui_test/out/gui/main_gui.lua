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

            player.gui.screen["gui_main"].destroy()

            global.players[player.index].is_gui_open = false

        else
            --open the gui

            global.players[player.index].is_gui_open = true
            local root = player.gui.screen

            local gui_main = root.add { type = "frame", name = "gui_main", direction = "vertical" }
            local title_bar = gui_main.add { type = "flow", name = "title_bar" }
            local unnamed_0 = title_bar.add { type = "label", name = "unnamed_0", style = "frame_title", caption = "titolo" }
            local unnamed_1 = title_bar.add { type = "empty-widget", name = "unnamed_1", style = "draggable_space" }
            local unnamed_2 = title_bar.add { type = "sprite-button", name = "unnamed_2", style = "frame_action_button",
                sprite = "utility/close_white", hovered_sprite = "utility/close_black",
                clicked_sprite = "utility/close_black" }
            local content = gui_main.add { type = "frame", name = "content", style = "content_style",
                caption = "content caption" }

        end


    end,

    on_event = function(event)
        --displatch the event to the custom functions


    end


}

return GUI
