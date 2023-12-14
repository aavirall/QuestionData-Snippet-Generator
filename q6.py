from Question import *
a = Question()
a.set_sort_key("6")
a.set_partition_key("questions")

a.set_question_id("6")
a.set_title("How long do you wish to date before getting married?")
a.set_subtitle("")
a.set_subtitle_2("")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Date_To_Marry_Intent")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.4")
a.set_conditions("[{\"question_id\": \"5\", \"option\": \"2\"}]")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_image_url("")
o.set_option_text("3 months")
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_image_url("")
o.set_option_text("6 months")
options.append(o)
o = Options()
o.set_option_id("3")
o.set_option_image_url("")
o.set_option_text("1 year")
options.append(o)
o = Options()
o.set_option_id("4")
o.set_option_image_url("")
o.set_option_text("2 years")
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()