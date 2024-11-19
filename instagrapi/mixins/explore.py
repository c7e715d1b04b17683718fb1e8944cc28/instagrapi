import random


class ExploreMixin:
    """
    Helpers for the explore page
    """

    def explore_page(self):
        """
        Get explore page

        Returns
        -------
        dict
        """
        return self.private_request("discover/topical_explore/")

    def report_explore_media(self, media_pk: int):
        """
        Report media in explore page. This is equivalent to the "not interested" button

        Parameters
        ----------
        media_pk: int
            Media PK
        Returns
        -------
        bool
            True if success
        """
        params = {
            "m_pk": media_pk,
        }
        result = self.private_request("discover/explore_report/", params=params)
        return result["explore_report_status"] == "OK"

    def explore_page_media_info(self, media_pk: int):
        """
        Returns media information for a media item on the explore page

        This is the API call that happens when you're on the explore page
        and you click into a media item. It returns information about that media item
        like comments, likes, etc.
        """
        return self.private_request(
            "/v1/discover/media_metadata/", params={"media_id": media_pk}
        )["media_or_ad"]

    def explore_chaining_experience_contextual_ads(
        self,
        seed_ad_id: int,
        inventory_source: str,
        multi_ad_individual_chain_ad_tracking_token: str,
        multi_ad_individual_chain_ad_ad_id: int,
        seed_ad_token: str,
        trigger_type: str,
        position: int,
        log_exposure_on_server: bool,
        container_module: str = "feed_timeline",
    ):
        data = {
            "seed_ad_id": seed_ad_id,
            "inventory_source": inventory_source,
            "phone_id": self.phone_id,
            "battery_level": random.randint(25, 100),
            "multi_ad_individual_chain_ad_tracking_token": multi_ad_individual_chain_ad_tracking_token,
            "_uid": self.user_id,
            "multi_ad_individual_chain_ad_ad_id": multi_ad_individual_chain_ad_ad_id,
            "_uuid": self.uuid,
            "seed_ad_token": seed_ad_token,
            "trigger_type": trigger_type,
            "is_charging": random.randint(0, 1),
            "position": position,
            "is_dark_mode": random.randint(0, 1),
            "will_sound_on": random.randint(0, 1),
            "log_exposure_on_server": log_exposure_on_server,
            "container_module": container_module,
        }

        return self.private_request(
            "/v1/discover/chaining_experience_contextual_ads/",
            data=data,
            with_signature=True,
        )
