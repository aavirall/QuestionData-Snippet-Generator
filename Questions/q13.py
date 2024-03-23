from Question import *
a = Question()
a.set_sort_key("13")
a.set_partition_key("questions")

a.set_question_id("13")
at = TextItem()
at.set_text("Tell me about your education")
a.set_title(at)
at = TextItem()
at.set_text("Consider adding at least your high school and graduation details")
a.set_subtitle(at)
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("question_education")
a.set_layout("add_education_details")
a.set_selection_type("1")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")
a.set_next_button_id(f"qs_{a.question_id}_next")

options = []

ops = options.__str__()
a.set_options(ops)

# conditions = []
# c = Conditions()
# c.set_question_id("14")
# c.set_option("1,2,3,4,6")
# conditions.append(c)
# conditions = conditions.__str__()
# a.set_conditions(conditions)

rep = a.__str__()