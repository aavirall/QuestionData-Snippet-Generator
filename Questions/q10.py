from Question import *
a = Question()
a.set_sort_key("10")
a.set_partition_key("questions")

a.set_question_id("10")
a.set_title("DUMMY SCREEN")
a.set_subtitle("")
a.set_subtitle_2("")
a.set_warning("These things may not matter to you, but I want to be inclusive and respectful of individual choice, since these may matter to some members or their famalies.")
a.set_warning_type("")
a.set_question_type("Religion")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.45")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_text("Hindu")
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_text("Muslim")
options.append(o)
o = Options()
o.set_option_id("3")
o.set_option_text("Christian")
options.append(o)
o = Options()
o.set_option_id("4")
o.set_option_text("Jain")
options.append(o)
o = Options()
o.set_option_id("5")
o.set_option_text("Sikh")
options.append(o)
o = Options()
o.set_option_id("6")
o.set_option_text("Buddhist")
options.append(o)
o = Options()
o.set_option_id("7")
o.set_option_text("Jewish")
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()