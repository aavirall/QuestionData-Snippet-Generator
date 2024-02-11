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
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Gender")
a.set_layout("grid")
a.set_selection_type("1")
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

bs = BottomSheet()
bs.set_selection_type("1")
ot = TextItem()
ot.set_text("Which gender do you identify as?")
bs.set_title(ot)
bs.set_layout("v_list")

bsops = []
bso = Option()
bso.set_option_id("1")
bsot = TextItem()
bsot.set_text("Trans-man")
bso.set_option_title(bsot)
bso.set_option_type("list_item_2")
bsops.append(bso)
bso = Option()
bso.set_option_id("2")
bsot = TextItem()
bsot.set_text("Trans-woman")
bso.set_option_title(bsot)
bso.set_option_type("list_item_2")
bsops.append(bso)
bs.set_options(bsops)

o.set_bottom_sheet(bs)

options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()