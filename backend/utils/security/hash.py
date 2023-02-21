from passlib.context import CryptContext


class Hash:

    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
    )

    @classmethod
    def verify_password(
        cls,
        plain_password: str | bytes,
        hashed_password: str | bytes,
    ) -> bool:

        return cls.pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(
        cls,
        password: str | bytes,
    ) -> str:

        return cls.pwd_context.hash(password)
