from Question import *
a = Question()
a.set_sort_key("16")
a.set_partition_key("questions")

a.set_question_id("16")
at = TextItem()
at.set_text("What did you do for work?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Employment_Past")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []

ops = options.__str__()
a.set_options(ops)

conditions = []
c = Conditions()
c.set_question_id("14")
c.set_option("5,7,8,9")
conditions.append(c)
conditions = conditions.__str__()
a.set_conditions(conditions)

rep = a.__str__()