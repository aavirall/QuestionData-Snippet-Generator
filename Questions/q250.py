from Question import *
a = Question()
a.set_sort_key("20")
a.set_partition_key("questions")

a.set_question_id("20")
at = TextItem()
at.set_text("What time were you born?")
a.set_title(at)
at = TextItem()
at.set_text("Not sure? Quickly call a family member to find out.")
a.set_subtitle(at)
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Birthtime")
a.set_layout("time_picker")
a.set_selection_type("1")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()