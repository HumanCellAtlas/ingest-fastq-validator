class ValidationError:

    def __init__(self, user_friendly_message):
        self.user_friendly_message = user_friendly_message


class RecordValidationError(ValidationError):

    def __init__(self, sequence_id):
        self.sequence_id = sequence_id
        self.user_friendly_message = "Invalid sequence characters found in sequence with id %s." % (sequence_id)
