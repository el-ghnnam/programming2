# ----------------------------------------------------------
# -- object oriented programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class Is The Blueprint Or the Constructor Of The Object.
# [02] Class Instantiate Means Create Instance of A Class.
# [03] Instance => Obeject Create From A Class And Have Their Methods and Attributes.
# [04] Class Definied With Keyword Class.
# [05] Class Name Written With Pascalcase [UpperCamelcase] Style.
# [06] Class May Contain Methods And Attributes.
# [07] When Creating Object Python Look For The Built In __init__ Methods.
# [08] __init__ Method Called Every Time You Create Object From Class.
# [09] __init__ Is The Initilization Data For The Class.
# [10] __init__ Have At Least One Argument Called [self].
# [11] __init__ print Not Return.
# [12] Any Methods With Two Underscroe In The Start and End Called Dunder or Magic Methods.
# [13] self Refer To The Current Instance Created From The Class And Must Be First Param.
# [14] In Python You Don't Need To Call new() KeyWord To Create Object.

class Member:
    def __init__(self):
        print(f'class Member Has Been Added.')


Member_1 = Member()
# __class__ ==> Tell You This Isntance Is Created From What Class.
print(Member_1.__class__)    # This Instance Is Created From Class Called Member.






