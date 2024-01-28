from Question import *
a = Question()
a.set_sort_key("7")
a.set_partition_key("questions")

a.set_question_id("7")
at = TextItem()
at.set_text("Which city do you live in?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Location_City")
a.set_option_type("option_text_field_snippet")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
ot = TextItem()
ot.set_text("No")
o.set_option_title(ot)
of = TextField()
of.set_icon("ebdd")
of.set_isMultiLine(False)
oft = TextItem()
oft.set_text("Search your city")
of.set_placeholder(oft)
oft = TextItem()
oft.set_text("Start typing...")
of.placeholderOnEditing(oft)
o.set_option_text_field(of)
options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()