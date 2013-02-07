from yampy.apis.utils import ArgumentDict


class UsersAPI(object):
    def __init__(self, client):
        """
        Initializes a new UsersAPI that will use the given client object
        to make HTTP requests.
        """
        self._client = client

    def all(self, page=None, letter=None, sort_by=None, reverse=None):
        """
        Returns all the users in the current user's network.

        Customize the response using the keyword arguments:
        page -- Enable pagination, and return the nth page of 50 users.
        letter -- Only return users whose username begins with this letter.
        sort_by -- Sort users by "messages" or "followers" (default order is
            alphabetical by username).
        reverse -- Reverse sort order.
        """
        return self._client.get("/users", **ArgumentDict(
            page=page,
            letter=letter,
            sort_by=sort_by,
            reverse=reverse,
        ))

    def find_current(self):
        """
        Returns the current user.
        """
        return self._client.get("/users/current")

    def find(self, user_id):
        """
        Returns the user identified by the given user_id.
        """
        return self._client.get("/users/%d" % user_id)

    def find_by_email(self, email_address):
        """
        Returns the user identified by the given email_address.
        """
        return self._client.get("/users/by_email", **ArgumentDict(
            email=email_address,
        ))