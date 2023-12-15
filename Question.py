import json

class Question:
    plan_name = "dynamodb_put"
    params = {}
    projections_string = '[\"title\", \"subtitle\", \"subtitle_2\", \"warning\", \"warning_type\", \"question_type\", \"option_type\",\"selection_type\",\"options\", \"question_id\",\"conditions\", \"next_button_text\", \"progress\"]'
    progress = "0.8"
    partition_key = "questions"
    sort_key = "sort_key"
    title = "title" 
    subtitle = "subtitle" 
    subtitle_2 = "subtitle_2" 
    warning = "warning"
    warning_type = "warning_type"
    question_type = "question_type"
    option_type = "option_type" 
    selection_type = "selection_type" 
    options = "options" 
    question_id = "question_id" 
    conditions = "conditions" 
    next_button_text = "next_button_text" 
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

    def set_warning(self, warning):
        self.warning = warning

    def set_warning_type(self, warning_type):
        self.warning_type = warning_type

    def set_question_type(self, question_type):
        self.question_type = question_type

    def set_option_type(self, option_type):
        self.option_type = option_type

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

    def set_projections(self, projections):
        self.projections = projections

    def __repr__(self):
        ret = {}
        params = {}
        params["partition_key"] = self.partition_key
        params["sort_key"] = self.sort_key
        params["progress"] = self.progress
        params["title"] = self.title
        params["subtitle"] = self.subtitle
        params["subtitle_2"] = self.subtitle_2
        params["warning"] = self.warning
        params["warning_type"] = self.warning_type
        params["question_type"] = self.question_type
        params["option_type"] = self.option_type
        params["selection_type"] = self.selection_type
        params["options"] = self.options
        params["question_id"] = self.question_id
        params["conditions"] = self.conditions
        params["next_button_text"] = self.next_button_text
        params["projections"] = self.projections

        ret["plan_name"] = self.plan_name
        ret["params"] = params
        return json.dumps(ret)
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Options:
    option_id = ""
    option_text = ""
    option_image_url = ""
    option_subtext = ""
    option_text_left_icon = ""
    option_subtext_left_icon = ""
    def __init__(self):
        pass

    def set_option_id(self, option_id):
        self.option_id = option_id

    def set_option_text(self, option_text):
        self.option_text = option_text

    def set_option_image_url(self, option_image_url):
        self.option_image_url = option_image_url
    
    def set_option_subtext(self, option_subtext):
        self.option_subtext = option_subtext

    def set_option_title(self, option_title):
        self.option_title = option_title

    def set_option_text_left_icon(self, option_text_left_icon):
        self.option_text_left_icon = option_text_left_icon

    def set_option_subtext_left_icon(self, option_subtext_left_icon):
        self.option_subtext_left_icon = option_subtext_left_icon

    def __repr__(self):
        return json.dumps(self.__dict__)
    
class OptionTitle:
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
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)