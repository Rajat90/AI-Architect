error_log = ["TXN002: BusinessException", "TXN004: SystemException", 
             "TXN005: BusinessException", "TXN006: AuthError"]

print(error_log[0:2])    # first 2 items
print(error_log[-2:])    # last 2 items
print(error_log[::2])    # every other item (step=2)