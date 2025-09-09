from behave import *

@given('first number as {a} and Second Number as {b}')
def givenForAdditionOf2numbers(context,a,b):
    print(a , b)
    context.a = a
    context.b = b
    # print(dir.context)
    print("I am in Given")
    

@when('operation {Operation} is performed')
def givenForAdditionOf2numbers(context,Operation):
    
    print("I am in When")
    if Operation == 'Add':
        context.result= eval(context.a) + eval(context.b)
        return context.result
    if Operation == 'Sub':
        context.result = eval(context.a) - eval(context.b)
        return context.result
    if Operation == 'Mul':
        context.result = eval(context.a) * eval(context.b)
        return context.result
    if Operation == 'Div':
        context.result = eval(context.a) / eval(context.b)
        return context.result

@then('Result should match {Result}')
def givenForAdditionOf2numbers(context,Result):
    # context.Result=Result
    print("I am in Then")
    print("Actual:", context.result )
    print("Expected:",  Result)
    assert (context.result == Result, "Test Passed")
    



    

