from Question import *
a = Question()
a.set_sort_key("17")
a.set_partition_key("questions")

a.set_question_id("17")
a.set_title("How much do you earn in a year?")
a.set_subtitle("Not shown on your profile, just between us so you can be honest")
a.set_subtitle_2("")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Income")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.77")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_text("₹ 5 Lakh or less")
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_text("₹ 5 to 10 lakhs")
options.append(o)
o = Options()
o.set_option_id("3")
o.set_option_text("₹ 10 to 20 lakhs")
options.append(o)
o = Options()
o.set_option_id("4")
o.set_option_text("₹  20 to 50 lakhs")
options.append(o)
o = Options()
o.set_option_id("5")
o.set_option_text("₹ 50 lakhs to 1 crore")
options.append(o)
o = Options()
o.set_option_id("6")
o.set_option_text("₹ 1 crore or more")
options.append(o)
o = Options()
o.set_option_id("7")
o.set_option_text("No income")
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()