import json

TOTAL_QUESTIONS = 40
class Question:
    plan_name = "dynamodb_put"
    params = {}
    projections_string = '[\"title\", \"subtitle\", \"subtitle_2\", \"alert\", \"alert_type\", \"question_type\", \"layout\",\"selection_type\",\"options\", \"question_id\",\"conditions\", \"next_button_text\", \"progress\", \"consent_text\", \"subtitle_3\"]'
    progress = ""
    partition_key = "questions"
    sort_key = "sort_key"
    title = "" 
    subtitle = "" 
    subtitle_2 = "" 
    subtitle_3 = "" 
    consent_text = ""
    alert = ""
    alert_type = ""
    question_type = ""
    layout = "" 
    selection_type = "" 
    options = "" 
    question_id = "" 
    conditions = "" 
    next_button_text = "" 
    skip_button_text = ""
    projections = projections_string
    def __init__(self):
        pass
    
    def set_sort_key(self, sort_key):
        self.sort_key = sort_key

    def set_progress(self, progress):
        self.progress = progress

    def set_partition_key(self, partition_key):
        self.partition_key = partition_key

    def set_title(self, title):
        self.title = title

    def set_subtitle(self, subtitle):
        self.subtitle = subtitle

    def set_subtitle_2(self, subtitle_2):
        self.subtitle_2 = subtitle_2

    def set_subtitle_3(self, subtitle_3):
        self.subtitle_3 = subtitle_3

    def set_alert(self, alert):
        self.alert = alert

    def set_alert_type(self, alert_type):
        self.alert_type = alert_type

    def set_consent_text(self, consent_text):
        self.consent_text = consent_text

    def set_question_type(self, question_type):
        self.question_type = question_type

    def set_layout(self, layout):
        self.layout = layout

    def set_selection_type(self, selection_type):
        self.selection_type = selection_type

    def set_options(self, options):
        self.options = options

    def set_question_id(self, question_id):
        self.question_id = question_id

    def set_conditions(self, conditions):
        self.conditions = conditions

    def set_next_button_text(self, next_button_text):
        self.next_button_text = next_button_text
    
    def set_skip_button_text(self, skip_button_text):
        self.skip_button_text = skip_button_text

    def set_projections(self, projections):
        self.projections = projections

    def __repr__(self):
        ret = {}
        params = {}
        params["partition_key"] = str(self.partition_key)
        params["sort_key"] = str(self.sort_key)
        params["progress"] = str(self.progress)
        params["title"] = str(self.title)
        params["subtitle"] = str(self.subtitle)
        params["subtitle_2"] = str(self.subtitle_2)
        params["subtitle_3"] = str(self.subtitle_3)
        params["consent_text"] = str(self.consent_text)
        params["alert"] = str(self.alert)
        params["alert_type"] = str(self.alert_type)
        params["question_type"] = str(self.question_type)
        params["layout"] = str(self.layout)
        params["selection_type"] = str(self.selection_type)
        params["options"] = str(self.options)
        params["question_id"] = str(self.question_id)
        params["conditions"] = str(self.conditions)
        params["next_button_text"] = str(self.next_button_text)
        params["skip_button_text"] = str(self.skip_button_text)
        params["projections"] = str(self.projections)

        ret["plan_name"] = self.plan_name
        ret["params"] = params
        return json.dumps(ret)

class Option:
    option_id = ""
    option_title = ""
    option_subtitle = ""
    option_text_field = ""
    option_type = ""
    option_shape = ""
    bottom_sheet = ""
    option_image_url = ""
    def __init__(self):
        pass

    def set_option_id(self, option_id):
        self.option_id = option_id

    def set_option_title(self, option_title):
        self.option_title = option_title

    def set_option_subtitle(self, option_subtitle):
        self.option_subtitle = option_subtitle

    def set_option_image_url(self, option_image_url):
        self.option_image_url = option_image_url

    def set_option_text_field(self, option_text_field):
        self.option_text_field = option_text_field
    
    def set_option_type(self, option_type):
        self.option_type = option_type
    
    def set_option_shape(self, shape):
        self.option_shape = shape
    
    def set_bottom_sheet(self, bottom_sheet):
        self.bottom_sheet = bottom_sheet

    def __repr__(self):
        ret = {}
        ret["option_id"] = self.option_id
        ret["option_image_url"] = self.option_image_url
        ret["option_type"] = self.option_type
        ret["option_shape"] = self.option_shape
        if self.option_title != "":
            ret["option_title"] = self.option_title.__dict__
        if self.option_subtitle != "":
            ret["option_subtitle"] = self.option_subtitle.__dict__
        if self.option_text_field != "":
            ret["option_text_field"] = self.option_text_field.__dict__
        if self.bottom_sheet != "":
            ret["bottom_sheet"] = self.bottom_sheet.__dict__
        return json.dumps(ret)
    
class TextItem:
    text = ""
    left_icon = ""
    right_icon = ""

    def __init__(self):
        pass

    def set_text(self, text):
        self.text = text

    def set_left_icon(self,left_icon):
        self.left_icon = left_icon

    def set_right_icon(self,right_icon):
        self.right_icon = right_icon
    
    def __repr__(self):
        return json.dumps(self.__dict__)
    
class TextField:
    is_multi_line         = ""
    left_icon                = ""
    right_icon                = ""
    placeholder         = ""
    text                = ""
    placeholder_on_editing = ""
    title = ""
    error_label = ""

    def __init__(self):
        pass

    def set_isMultiLine(self, is_multi_line):
        self.is_multi_line = is_multi_line
    
    def set_left_icon(self, icon):
        self.left_icon = icon
    
    def set_right_icon(self, icon):
        self.right_icon = icon
    
    def set_title(self, title):
        self.title = title.__dict__

    def set_error_label(self, label):
        self.error_label = label.__dict__

    def set_placeholder(self, placeholder):
        self.placeholder = placeholder.__dict__
    
    def placeholderOnEditing(self, placeholderOnEditing):
        self.placeholder_on_editing = placeholderOnEditing.__dict__
    
    def set_text(self, text):
        self.text = text.__dict__
    
    def __repr__(self):
        return json.dumps(self.__dict__)
    
class BottomSheet:
    selection_type = ""
    options = ""
    title = ""
    subtitle = ""
    layout = ""
    bottom_button_text = ""
    bottom_button_icon = ""

    def __init__(self):
        pass

    def set_selection_type(self, selection_type):
        self.selection_type = selection_type
    
    def set_options(self, options):
        self.options = [make_json(ele.__dict__) for ele in options]
    
    def set_title(self, title):
        self.title = title.__dict__
    
    def set_subtitle(self, subtitle):
        self.subtitle = subtitle.__dict__
    
    def set_bottom_button_text(self, bottom_button_text):
        self.bottom_button_text = bottom_button_text
    
    def set_bottom_button_icon(self, bottom_button_icon):
        self.bottom_button_icon = bottom_button_icon
    
    def set_layout(self, layout):
        self.layout = layout
    

def make_json(ele):
    ret = {}
    for k,v in ele.items():
        if type(v) != str:
            ret[k] = v.__dict__
        else:
            ret[k] = v
    return ret


class Conditions:
    question_id = ""
    option  = ""

    def set_question_id(self, question_id):
        self.question_id = question_id

    def set_option(self, option):
        self.option = option

    def __repr__(self):
        return json.dumps(self.__dict__)
    
class ButtonModel:
    title = ""
    left_icon = ""
    right_icon = ""
    def __init__(self):
        pass

    def set_title(self, title):
        self.title = title
    
    def set_left_icon(self, left_icon):
        self.left_icon = left_icon
    
    def set_right_icon(self, right_icon):
        self.right_icon = right_icon
    