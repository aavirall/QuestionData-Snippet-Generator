# Political leaning
from Question import *
a = Question()
a.set_sort_key("26")
a.set_partition_key("questions")

a.set_question_id("26")
at = TextItem()
at.set_text("What's your political leaning?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Political_Leaning")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Socialist/Leftist")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Rightist")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("3")
ot = TextItem()
ot.set_text("Moderate/Centrist")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("4")
ot = TextItem()
ot.set_text("Apolitical")
o.set_option_title(ot)
options.append(o)

#Add conditions

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()






# from Question import *
# a = Question()
# a.set_sort_key("23")
# a.set_partition_key("questions")

# a.set_question_id("23")
# at = TextItem()
# at.set_text("Your professional background")
# a.set_title(at)
# a.set_subtitle("")
# a.set_subtitle_2("")
# a.set_warning("")
# a.set_warning_type("")
# a.set_question_type("Professional_Background")
# a.set_option_type("option_text_field_snippet")
# a.set_selection_type("single_selection")
# a.set_progress("1")
# a.set_conditions("")
# a.set_next_button_text("Next")

# options = []
# o = Options()
# o.set_option_id("1")
# of = TextField()
# of.set_isMultiLine(False)
# oft = TextItem()
# oft.set_text("Designation")
# of.set_title(oft)
# oft = TextItem()
# oft.set_text("Your current title")
# of.set_placeholder(oft)
# oft = TextItem()
# oft.set_text("Start typing...")
# of.placeholderOnEditing(oft)
# o.set_option_text_field(of)
# options.append(o)

# o = Options()
# o.set_option_id("2")
# of = TextField()
# of.set_isMultiLine(False)
# oft = TextItem()
# oft.set_text("Organisation")
# of.set_title(oft)
# oft = TextItem()
# oft.set_text("Enter current company")
# of.set_placeholder(oft)
# oft = TextItem()
# oft.set_text("Start typing...")
# of.placeholderOnEditing(oft)
# o.set_option_text_field(of)
# options.append(o)

# o = Options()
# o.set_option_id("3")
# of = TextField()
# of.set_isMultiLine(False)
# oft = TextItem()
# oft.set_text("Highest Degree")
# of.set_title(oft)
# oft = TextItem()
# oft.set_text("e.g., Masters in Computer Science")
# of.set_placeholder(oft)
# oft = TextItem()
# oft.set_text("Start typing...")
# of.placeholderOnEditing(oft)
# o.set_option_text_field(of)
# options.append(o)

# o = Options()
# o.set_option_id("4")
# of = TextField()
# of.set_isMultiLine(False)
# oft = TextItem()
# oft.set_text("Educational Institution")
# of.set_title(oft)
# oft = TextItem()
# oft.set_text("e.g., IIT Delhi")
# of.set_placeholder(oft)
# oft = TextItem()
# oft.set_text("Start typing...")
# of.placeholderOnEditing(oft)
# o.set_option_text_field(of)
# options.append(o)

# ops = options.__str__()
# a.set_options(ops)
# rep = a.__str__()