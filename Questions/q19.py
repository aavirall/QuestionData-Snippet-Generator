from Question import *
a = Question()
a.set_sort_key("19")
a.set_partition_key("questions")

a.set_question_id("19")
a.set_title("Where were you born?")
a.set_subtitle("City, town or village")
a.set_subtitle_2("State")
a.set_warning("")
a.set_warning_type("")
a.set_question_type("Birthplace")
a.set_option_type("list_cell_snippet")
a.set_selection_type("single_selection")
a.set_progress("0.86")
a.set_conditions("")
a.set_next_button_text("Next")

options = []
o = Options()
o.set_option_id("1")
o.set_option_text("Andhra Pradesh")
options.append(o)

# Assam
o = Options()
o.set_option_id("2")
o.set_option_text("Assam")
options.append(o)

# Arunachal Pradesh
o = Options()
o.set_option_id("3")
o.set_option_text("Arunachal Pradesh")
options.append(o)

# Bihar
o = Options()
o.set_option_id("4")
o.set_option_text("Bihar")
options.append(o)

# Chhattisgarh
o = Options()
o.set_option_id("5")
o.set_option_text("Chhattisgarh")
options.append(o)

# Goa
o = Options()
o.set_option_id("6")
o.set_option_text("Goa")
options.append(o)

# Gujarat
o = Options()
o.set_option_id("7")
o.set_option_text("Gujarat")
options.append(o)

# Haryana
o = Options()
o.set_option_id("8")
o.set_option_text("Haryana")
options.append(o)

# Himachal Pradesh
o = Options()
o.set_option_id("9")
o.set_option_text("Himachal Pradesh")
options.append(o)

# Jharkhand
o = Options()
o.set_option_id("10")
o.set_option_text("Jharkhand")
options.append(o)

# Karnataka
o = Options()
o.set_option_id("11")
o.set_option_text("Karnataka")
options.append(o)

# Kerala
o = Options()
o.set_option_id("12")
o.set_option_text("Kerala")
options.append(o)

# Madhya Pradesh
o = Options()
o.set_option_id("13")
o.set_option_text("Madhya Pradesh")
options.append(o)

# Maharashtra
o = Options()
o.set_option_id("14")
o.set_option_text("Maharashtra")
options.append(o)

# Manipur
o = Options()
o.set_option_id("15")
o.set_option_text("Manipur")
options.append(o)

# Meghalaya
o = Options()
o.set_option_id("16")
o.set_option_text("Meghalaya")
options.append(o)

# Mizoram
o = Options()
o.set_option_id("17")
o.set_option_text("Mizoram")
options.append(o)

# Nagaland
o = Options()
o.set_option_id("18")
o.set_option_text("Nagaland")
options.append(o)

# Odisha
o = Options()
o.set_option_id("19")
o.set_option_text("Odisha")
options.append(o)

# Punjab
o = Options()
o.set_option_id("20")
o.set_option_text("Punjab")
options.append(o)

# Rajasthan
o = Options()
o.set_option_id("21")
o.set_option_text("Rajasthan")
options.append(o)

# Sikkim
o = Options()
o.set_option_id("22")
o.set_option_text("Sikkim")
options.append(o)

# Tamil Nadu
o = Options()
o.set_option_id("23")
o.set_option_text("Tamil Nadu")
options.append(o)

# Telangana
o = Options()
o.set_option_id("24")
o.set_option_text("Telangana")
options.append(o)

# Tripura
o = Options()
o.set_option_id("25")
o.set_option_text("Tripura")
options.append(o)

# Uttar Pradesh
o = Options()
o.set_option_id("26")
o.set_option_text("Uttar Pradesh")
options.append(o)

# Uttarakhand
o = Options()
o.set_option_id("27")
o.set_option_text("Uttarakhand")
options.append(o)

# West Bengal
o = Options()
o.set_option_id("28")
o.set_option_text("West Bengal")
options.append(o)

# Jammu and Kashmir
o = Options()
o.set_option_id("29")
o.set_option_text("Jammu and Kashmir")
options.append(o)

ops = options.__str__()
a.set_options(ops)
rep = a.__str__()