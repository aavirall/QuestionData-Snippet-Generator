from Question import *
a = Question()
a.set_sort_key("12")
a.set_partition_key("questions")

a.set_question_id("12")
a.set_title("What's your diet?")
a.set_subtitle("")
a.set_subtitle_2("")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Diet")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.54")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_text("Non vegetarian")
o.set_option_subtext("Everything (may exclude certain meats)")
o.set_option_text_left_icon("eb6e")
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_image_url("Carrot")
o.set_option_text("Vegetarian")
o.set_option_subtext("No mear, fish, seafood, eggs")
o.set_option_text_left_icon("ea04")
options.append(o)
o = Options()
o.set_option_id("3")
o.set_option_image_url("CrackedEgg")
o.set_option_text("Eggetarian")
o.set_option_subtext("No mear, fish, seafood")
o.set_option_text_left_icon("eabf")
options.append(o)
o = Options()
o.set_option_id("4")
o.set_option_image_url("Fish")
o.set_option_text("Pescetarian")
o.set_option_subtext("Fish and/or seafood, but no meat")
o.set_option_text_left_icon("eb11")
options.append(o)
o = Options()
o.set_option_id("5")
o.set_option_image_url("Leaf")
o.set_option_text("Jain")
o.set_option_subtext("No meat, fish, seafood, eggs, root vegetables")
o.set_option_text_left_icon("ebb8")
options.append(o)
o = Options()
o.set_option_id("6")
o.set_option_image_url("Herb")
o.set_option_text("Vegan")
o.set_option_subtext("No animal products including dairy")
o.set_option_text_left_icon("ec7d")
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()