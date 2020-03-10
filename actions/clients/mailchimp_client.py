from mailchimp3 import MailChimp
from mailchimp3.mailchimpclient import MailChimpError
from typing import Text


class MailChimpClient:
  """Sends emails through MailChimp"""

  def __init__(self, api_key: Text, user: Text) -> None:
    self.client = MailChimp(mc_api=api_key, mc_user=user)

  def subscribe(self, newsletter_id: Text, email: Text) -> bool:
    # Subscribe the user to the newsletter if they're not already
    # User subscribed with the status pending
    try:
      self.client.lists.members.create(
          newsletter_id, data={"email_address": email, "status": "pending"}
      )
      return True
    except MailChimpError as e:
      # TODO this can be any error log it!
      print(e)
      # The user is already subscribed
      return False