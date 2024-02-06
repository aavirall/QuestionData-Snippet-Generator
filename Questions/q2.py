from Question import *
a = Question()
a.set_sort_key("2")
a.set_partition_key("questions")

a.set_question_id("2")
at = TextItem()
at.set_text("Who are you interested in meeting?")
a.set_title(at)
at = TextItem()
at.set_text("Select as many as you want")
a.set_subtitle(at)
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Gender_Preference")
a.set_layout("grid")
a.set_selection_type("20")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Option()
o.set_option_id("1")
o.set_option_image_url("Man")
ot = TextItem()
ot.set_text("Man")
o.set_option_title(ot)
o.set_option_type("image_card")
o.set_option_shape("square")
options.append(o)
o = Option()
o.set_option_id("2")
o.set_option_image_url("Woman")
ot = TextItem()
ot.set_text("Woman")
o.set_option_title(ot)
o.set_option_type("image_card")
o.set_option_shape("square")
options.append(o)
o = Option()
o.set_option_id("3")
o.set_option_image_url("OtherGender")
ot = TextItem()
ot.set_text("Other")
o.set_option_title(ot)
o.set_option_type("image_card")
o.set_option_shape("rectangle")
options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()