def combo_string(a, b):

    # your code here
    if len(a) < len(b):
         short,longer = a,b
    else:
        short,longer = b,a

    return short + longer + short