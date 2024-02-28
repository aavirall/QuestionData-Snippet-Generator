# Political leaning
from Question import *
a = Question()
a.set_sort_key("25")
a.set_partition_key("questions")

a.set_question_id("25")
at = TextItem()
at.set_text("What's your religious view?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Religious_view")
a.set_layout("v_list")
a.set_selection_type("1")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_next_button_text("Next")

options = []
o = Option()
o.set_option_id("1")
o.set_option_type("option_card")
ot = TextItem()
ot.set_text("Religious")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("2")
o.set_option_type("option_card")
ot = TextItem()
ot.set_text("Spiritual, but not Religious")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("3")
o.set_option_type("option_card")
ot = TextItem()
ot.set_text("Neither Religious nor Spiritual")
o.set_option_title(ot)
options.append(o)

#Add conditions

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()


