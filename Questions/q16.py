from Question import *
a = Question()
a.set_sort_key("16")
a.set_partition_key("questions")

a.set_question_id("16")
at = TextItem()
at.set_text("Tell me about your education")
a.set_title(at)
at = TextItem()
at.set_text("Consider adding at least your high school and graduation details")
a.set_subtitle(at)
a.set_subtitle_2("")
a.set_alert("")
a.set_alert_type("")
a.set_question_type("Education")
a.set_layout("education_details_snippet")
a.set_selection_type("single_selection")
a.set_progress(f"{int(a.question_id)/TOTAL_QUESTIONS :.2f}")
a.set_conditions("")
a.set_next_button_text("Next")

options = []

ops = options.__str__()
a.set_options(ops)


rep = a.__str__()