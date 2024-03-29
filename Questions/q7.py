from Question import *
a = Question()
a.set_sort_key("7")
a.set_partition_key("questions")

a.set_question_id("7")
at = TextItem()
at.set_text("Your top 5 interests?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Interests")
a.set_option_type("badges_grid_snippet")
a.set_selection_type("max5_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Going Out")
ot.set_left_icon("eb37")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Pets")
ot.set_left_icon("ec52")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("3")
ot = TextItem()
ot.set_text("Music")
ot.set_left_icon("ec08")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("4")
ot = TextItem()
ot.set_text("Cooking")
ot.set_left_icon("ea6a")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("5")
ot = TextItem()
ot.set_text("Reading")
ot.set_left_icon("e9c8")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("6")
ot = TextItem()
ot.set_text("Driving")
ot.set_left_icon("ed2d")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("7")
ot = TextItem()
ot.set_text("Parties")
ot.set_left_icon("edd9")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("8")
ot = TextItem()
ot.set_text("Travel")
ot.set_left_icon("ed3c")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("9")
ot = TextItem()
ot.set_text("Theatre")
ot.set_left_icon("ebe5")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("10")
ot = TextItem()
ot.set_text("Arts & Craft")
ot.set_left_icon("ec3d")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("11")
ot = TextItem()
ot.set_text("Shopping")
ot.set_left_icon("ecdd")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("12")
ot = TextItem()
ot.set_text("Dancing")
ot.set_left_icon("ec68")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("13")
ot = TextItem()
ot.set_text("Movies & TV Shows")
ot.set_left_icon("ec8d")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("14")
ot = TextItem()
ot.set_text("Fitness")
ot.set_left_icon("e993")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("15")
ot = TextItem()
ot.set_text("Video Games")
ot.set_left_icon("eb3d")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("16")
ot = TextItem()
ot.set_text("Board Games")
ot.set_left_icon("ea07")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("17")
ot = TextItem()
ot.set_text("Gardening")
ot.set_left_icon("ec8e")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("18")
ot = TextItem()
ot.set_text("Photography")
ot.set_left_icon("e91b")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("19")
ot = TextItem()
ot.set_text("Sports")
ot.set_left_icon("ed52")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("20")
ot = TextItem()
ot.set_text("Trekking")
ot.set_left_icon("ec04")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("21")
ot = TextItem()
ot.set_text("Yoga")
ot.set_left_icon("edde")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("22")
ot = TextItem()
ot.set_text("Meditation")
ot.set_left_icon("edde")
o.set_option_title(ot)
options.append(o)

o = Options()
o.set_option_id("23")
ot = TextItem()
ot.set_text("Current Affairs")
ot.set_left_icon("edde")
o.set_option_title(ot)
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()

# from Question import *
# a = Question()
# a.set_sort_key("11")
# a.set_partition_key("questions")

# a.set_question_id("11")
# at = TextItem()
# at.set_text("How tall are you?")
# a.set_title(at)
# a.set_subtitle("")
# a.set_subtitle_2("")
# a.set_warning("")
# a.set_warning_type("")
# a.set_question_type("Height")
# a.set_option_type("height_picker")
# a.set_selection_type("single_selection")
# a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
# a.set_conditions("")
# a.set_next_button_text("Next")

# options = []

# ops = options.__str__()
# a.set_options(ops)
# rep = a.__str__()