from Question import *
a = Question()
a.set_sort_key("1")
a.set_partition_key("questions")

a.set_question_id("1")
at = TextItem()
at.set_text("What's your gender?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Gender")
a.set_option_type("image_card_view_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.04")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_image_url("Man")
o.set_option_text("Man")
ot = TextItem()
ot.set_text("Man")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_image_url("Woman")
o.set_option_text("Woman")
ot = TextItem()
ot.set_text("Woman")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("3")
o.set_option_image_url("OtherGender")
o.set_option_text("Other")
ot = TextItem()
ot.set_text("Other")
o.set_option_title(ot)
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()