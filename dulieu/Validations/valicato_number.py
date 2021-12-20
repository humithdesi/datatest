from django.core.exceptions import ValidationError
def LonHon8(value):
    if len(value) < 8:
        raise ValidationError("Mật Khảu Phải Có Ít Nhất 8 ký tự")
    else:
        return value