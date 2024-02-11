from Question import *
a = Question()
a.set_sort_key("21")
a.set_partition_key("questions")

a.set_question_id("21")
at = TextItem()
at.set_text("Where were you born?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Birthplace")
a.set_layout("option_card_text_field_snippet")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Option()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Search your city")
ot.set_left_icon("ebdd")
o.set_option_title(ot)
o.set_option_type("option_card")

bs = BottomSheet()
bs.set_selection_type("1")
ot = TextItem()
ot.set_text("Select your current city")
bs.set_title(ot)
bs.set_layout("bottom_sheet_search_field")
bsops = []
bso = Option()
bso.set_option_id("1")
bsotf = TextField()
bsotf.set_left_icon("ebdd")
bsotft = TextItem()
bsotft.set_text("Search your city")
bsotf.set_placeholder(bsotft)
bso.set_option_text_field(bsotf)
bsops.append(bso)
bs.set_options(bsops)

o.set_bottom_sheet(bs)


options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()

# from Question import *
# a = Question()
# a.set_sort_key("13")
# a.set_partition_key("questions")

# a.set_question_id("13")
# at = TextItem()
# at.set_text("XXX")
# a.set_title(at)
# a.set_subtitle("")
# a.set_subtitle_2("")
# a.set_warning("")
# a.set_warning_type("")
# a.set_question_type("Indulgement")
# a.set_option_type("option_card_v_list")
# a.set_selection_type("multi_selection")
# a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
# a.set_conditions("")
# a.set_next_button_text("Next")

# options = []
# o = Options()
# o.set_option_id("1")
# ot = TextItem()
# ot.set_text("Smoke")
# ot.set_left_icon("ea69")
# o.set_option_title(ot)
# options.append(o)
# o = Options()
# o.set_option_id("2")
# ot = TextItem()
# ot.set_text("Drink")
# ot.set_left_icon("edd9")
# o.set_option_title(ot)
# options.append(o)
# o = Options()
# o.set_option_id("3")
# ot = TextItem()
# ot.set_text("Marijuana")
# ot.set_left_icon("ebb8")
# o.set_option_title(ot)
# ot = TextItem()
# ot.set_text("Not Shown on your profile")
# ot.set_left_icon("ead3")
# o.set_option_subtitle(ot)
# options.append(o)
# o = Options()
# o.set_option_id("3")
# ot = TextItem()
# ot.set_text("Drugs")
# ot.set_left_icon("ec77")
# o.set_option_title(ot)
# ot = TextItem()
# ot.set_text("Not Shown on your profile")
# ot.set_left_icon("ead3")
# o.set_option_subtitle(ot)
# options.append(o)


# ops = options.__str__()
# a.set_options(ops)
# rep = a.__str__()