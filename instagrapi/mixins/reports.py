class ReportsMixin:
    """
    Helpers for the reports page
    """

    def get_frx_prompt(
        self,
        object_id: int,
        container_module: str = "feedPage",
        entry_point: int = 3,
        location: int = 1,
        object_type: int = 7,
        context: str = "",
        selected_tag_types: str = "",
        frx_prompt_request_type: int = 1,
    ):
        """
        Get the prompt for reporting a post
        """
        data = {
            'container_module': container_module,
            'entry_point': entry_point,
            'location': location,
            'object_id': object_id,
            'object_type': object_type,
            'context': context,
            'selected_tag_types': selected_tag_types,
            'frx_prompt_request_type': frx_prompt_request_type,
        }
        return self.private_request(
            "/v1/reports/get_frx_prompt/",
            data=data,
        )
