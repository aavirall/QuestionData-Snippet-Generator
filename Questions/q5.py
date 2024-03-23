from Question import *
a = Question()
a.set_sort_key("5")
a.set_partition_key("questions")

a.set_question_id("5")
at = TextItem()
at.set_text("Which city do you live in?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("Several Members currently reside in Mumbai and Delhi NCR. You can meet them over video while we build a large community around the world")
a.set_alert_type("warning")
a.set_question_type("question_location_city")
a.set_layout("search_fields")
a.set_selection_type("20")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")
a.set_next_button_id(f"qs_{a.question_id}_next")

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

# bstf = TextField()
# bstf.set_left_icon("ebdd")
# bstft = TextItem()
# bstft.set_text("Search your city")
# bstf.set_placeholder(bstft)
# bs.set_text_field(bstf)

bs.set_screen_type("city_selector_screen")
# bsops = []
# bso = Option()
# bso.set_option_id("1")
# bso.set_option_type("list_item_2")
# bsops.append(bso)
# bs.set_options(bsops)
o.set_bottom_sheet(bs)
options.append(o)
# o = Options()
# o.set_option_id("1")
# of = TextField()
# of.set_left_icon("ebdd")
# oft = TextItem()
# oft.set_text("Search your city")
# of.set_placeholder(oft)
# o.set_option_text_field(of)
# o.set_option_type("option_card")
# options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()