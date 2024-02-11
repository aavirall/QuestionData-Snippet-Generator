from Question import *
a = Question()
a.set_sort_key("22")
a.set_partition_key("questions")

a.set_question_id("22")
at = TextItem()
at.set_text("What's your religion?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("While your religious beliefs are personal, they can be a source of comfort, shared values, and traditions. Sharing it lets us find matches who respects your beliefs")
a.set_alert_type("info")
a.set_question_type("Religion")
a.set_layout("option_card_v_list")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Option()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Hindu")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Muslim")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("3")
ot = TextItem()
ot.set_text("Christian")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("4")
ot = TextItem()
ot.set_text("Jain")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("5")
ot = TextItem()
ot.set_text("Sikh")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("6")
ot = TextItem()
ot.set_text("Buddhist")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("7")
ot = TextItem()
ot.set_text("Jewish")
o.set_option_title(ot)
options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()