from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, *args, timestamp):
        return six.text_type(args.id)+six.text_type(timestamp)+six.text_type(args.Verified)
