from Question import *
a = Question()
a.set_sort_key("130")
a.set_partition_key("questions")

a.set_question_id("130")
at = TextItem()
at.set_text("Do you smoke?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Smoke")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Never")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Sometimes")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("3")
ot = TextItem()
ot.set_text("Regularly")
o.set_option_title(ot)
options.append(o)

ops = options.__str__()
a.set_options(ops)

rep = a.__str__()