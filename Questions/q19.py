from Question import *
a = Question()
a.set_sort_key("19")
a.set_partition_key("questions")
a.set_question_id("19")
at = TextItem()
at.set_text("Tell me about your physique")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_alert("This will help me match you with a partner who respects your body type and avoids any first meeting surprises or awkwardness")
a.set_alert_type("info")
a.set_question_type("Employment")
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
c.set_option("5")
conditions.append(c)
conditions = conditions.__str__()
a.set_conditions(conditions)

rep = a.__str__()