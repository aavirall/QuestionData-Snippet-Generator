from Question import *
a = Question()
a.set_sort_key("9")
a.set_partition_key("questions")

a.set_question_id("9")
a.set_title("DUMMY SCREEN")
a.set_subtitle("This will help me match you to the right supportive partner")
a.set_subtitle_2("")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Chronic_Illness")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.40")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_text("No")
# o.set_option_text_left_icon("eddb")
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_text("Yes")
# o.set_option_text_left_icon("ea30")
options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()