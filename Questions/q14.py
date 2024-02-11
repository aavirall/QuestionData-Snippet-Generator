from Question import *
a = Question()
a.set_sort_key("14")
a.set_partition_key("questions")

a.set_question_id("14")
at = TextItem()
at.set_text("Where do/did you study?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Education")
a.set_layout("search_fields")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

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