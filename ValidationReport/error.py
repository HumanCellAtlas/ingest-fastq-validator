from enum import Enum


class ValidationError:

    def __init__(self, user_friendly_message):
        self.user_friendly_message = user_friendly_message

class RecordError(ValidationError):

    class Type(Enum):
        UNDEFINED = 'validation.fastq.error.undefined', 'unknown error'
        INVALID_SEQUENCE = 'validation.fastq.error.invalid_sequence', 'invalid sequence character(s)'

        def __new__(type, code, description):
            error_type = object.__new__(type)
            error_type.code = code
            error_type.description = description
            return  error_type

        def report_error(self, sequence_id:str):
            return RecordError(sequence_id, self)

    def __init__(self, sequence_id, type:Type=Type.UNDEFINED):
        self.sequence_id = sequence_id
        self.type = type
        self.user_friendly_message = "%s on record with sequence id %s" % (type.description, sequence_id)

