from Question import *
a = Question()
a.set_sort_key("3")
a.set_partition_key("questions")

a.set_question_id("3")
at = TextItem()
at.set_text("What are you here for?")
a.set_title(at)
at = TextItem()
at.set_text("Please be thoughtful as this selection will impact your and other Members' experience")
a.set_subtitle(at)
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Intent")
a.set_option_type("card_v_list")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("I am 100% sure!")

options = []
o = Options()
o.set_option_id("1")
ot = TextItem()
ot.set_text("Marry")
ot.set_left_icon("eba6")
o.set_option_title(ot)
ot = TextItem()
ot.set_text("Ready to get married, with family involved, from the first one-on-one meeting")
o.set_option_subtitle(ot)
options.append(o)
o = Options()
o.set_option_id("2")
ot = TextItem()
ot.set_text("Date to Marry")
ot.set_left_icon("ebb3")
o.set_option_title(ot)
ot = TextItem()
ot.set_text("Want to date with the serious intent to get married in max 2yrs")
o.set_option_subtitle(ot)
options.append(o)
o = Options()
o.set_option_id("3")
ot = TextItem()
ot.set_text("Exclusively Date")
ot.set_left_icon("eb8a")
o.set_option_title(ot)
ot = TextItem()
ot.set_text("Not sure if/when I want to get married, but want an exclusive relationship with emotional bonding")
o.set_option_subtitle(ot)
options.append(o)
o = Options()
o.set_option_id("4")
ot = TextItem()
ot.set_text("Casually Date")
ot.set_left_icon("ebbe")
o.set_option_title(ot)
ot = TextItem()
ot.set_text("Seek a partner without commitment, exclusivity or emotional attachment")
o.set_option_subtitle(ot)
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()