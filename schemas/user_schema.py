from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    id: int = Field(..., description="Identificador único do usuário")
    username: str = Field(..., min_length=3, description="Nome de usuário")
    email: EmailStr
    status: str = Field(..., description="Status da conta do usuário")