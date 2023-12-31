from Question import *
a = Question()
a.set_sort_key("2")
a.set_partition_key("questions")

a.set_question_id("2")
at = TextItem()
at.set_text("Which gender do you identify as?")
a.set_title(at)
a.set_subtitle("")
a.set_subtitle_2("")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Gender_Others")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.09")
a.set_conditions("[{\"question_id\": \"1\", \"option\": \"3\"}]")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_image_url("")
o.set_option_text("Trans-man")
ot = TextItem()
ot.set_text("Trans-man")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("2")
o.set_option_image_url("")
o.set_option_text("Trans-woman")
options.append(o)
ot = TextItem()
ot.set_text("Trans-woman")
o.set_option_title(ot)
o = Options()
o.set_option_id("3")
o.set_option_image_url("")
o.set_option_text("Genderqueer")
ot = TextItem()
ot.set_text("Genderqueer")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("4")
o.set_option_image_url("")
o.set_option_text("Agender")
ot = TextItem()
ot.set_text("Agender")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("5")
o.set_option_image_url("")
o.set_option_text("Genderless")
ot = TextItem()
ot.set_text("Genderless")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("6")
o.set_option_image_url("")
o.set_option_text("Non-binary")
ot = TextItem()
ot.set_text("Non-binary")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("7")
o.set_option_image_url("")
o.set_option_text("Third gender")
ot = TextItem()
ot.set_text("Third gender")
o.set_option_title(ot)
options.append(o)
o = Options()
o.set_option_id("8")
o.set_option_image_url("")
o.set_option_text("Two-spirit")
ot = TextItem()
ot.set_text("Two-spirit")
o.set_option_title(ot)
options.append(o)


ops = options.__str__()
a.set_options(ops)
rep = a.__str__()