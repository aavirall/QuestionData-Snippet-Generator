from Question import *
a = Question()
a.set_sort_key("90")
a.set_partition_key("questions")

a.set_question_id("90")
at = TextItem()
at.set_text("What are your family plans?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Family_Plans_Yes")
a.set_layout("option_card_v_list")
a.set_selection_type("1")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Option()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Don't want more children")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Want more children")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("3")
ot = TextItem()
ot.set_text("Not sure yet")
o.set_option_title(ot)
options.append(o)

ops = options.__str__()
a.set_options(ops)

conditions = []
c = Conditions()
c.set_question_id("70")
c.set_option("2")
conditions.append(c)
conditions = conditions.__str__()
a.set_conditions(conditions)

rep = a.__str__()