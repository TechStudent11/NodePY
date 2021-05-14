"""nodepy.errors: custom named errors"""


class ProjectFound(Exception):
    """Error for if a project is found."""
    pass

class ProjectNotFound(Exception):
    """Error for if a project is not found."""
    pass

class ScriptNotFound(Exception):
    """Error for if a script wasn't found."""
    pass