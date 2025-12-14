class ToolInputError(Exception):
    """Raised when a tool receives invalid or unsupported input."""
    pass


class ToolExecutionError(Exception):
    """Raised when a tool fails during execution (API errors, math errors, etc.)."""
    pass
