from Question import *
a = Question()
a.set_sort_key("21")
a.set_partition_key("questions")

a.set_question_id("21")
at = TextItem()
at.set_text("Is your birthdate the same as your govt. ID?")
a.set_title(at)
at = TextItem()
at.set_text("It's cool to share, that's the case with many of us, we can blame it on the parents :)")
a.set_subtitle(at)
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Birthdate_Matches_Id")
a.set_layout("option_card_v_list")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Option()
o.set_option_id("1")
ot = TextItem()
ot.set_text("No")
ot.set_left_icon("eddb")
o.set_option_title(ot)
options.append(o)
o = Option()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Yes")
ot.set_left_icon("ea30")
o.set_option_title(ot)
of = TextField()
of.set_isMultiLine(True)
oft = TextItem()
oft.set_text("Please share a bit more...")
of.set_placeholder(oft)
o.set_option_text_field(of)
options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()