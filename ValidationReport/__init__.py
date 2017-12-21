from ValidationReport.error import ValidationError, RecordValidationError


class ValidationReport:

    def __init__(self, state="", error_reports=None):
        self.state = state
        self.errors = error_reports if error_reports is not None else list()  # list of ErrorReport

    def errors_to_dict(self):
        return [error.__dict__ for error in self.errors]

    def log_error(self, user_friendly_message):
        self.errors.append(ValidationError(user_friendly_message))

    def log_record_error(self, sequence_id):
        self.errors.append(RecordValidationError(sequence_id))

    def to_dict(self):
        return {
            "validation_state": self.state,
            "validation_errors": self.errors_to_dict()
        }

    @staticmethod
    def validation_report_ok():
        report = ValidationReport()
        report.state = "VALID"
        return report
