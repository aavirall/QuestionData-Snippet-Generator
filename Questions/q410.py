from Question import *
a = Question()
a.set_sort_key("5")
a.set_partition_key("questions")

a.set_question_id("5")
at = TextItem()
at.set_text("Do you have children?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("question_children")
a.set_layout("v_list")
a.set_selection_type("1")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")
a.set_next_button_id(f"qs_{a.question_id}_next")

options = []
o = Option()
o.set_option_id("1")
ot = TextItem()
ot.set_text("No")
o.set_option_title(ot)
o.set_option_type("option_card")
options.append(o)
o = Option()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Yes")
o.set_option_title(ot)
o.set_option_type("option_card")
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()