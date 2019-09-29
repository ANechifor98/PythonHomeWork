#def reverseInParentheses(inputString):
#    s = " ".join(" ".join(inputString.split("(")).split(")"))
#   return s

def reverseInParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseInParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

if __name__ == "__main__":
    inputString = "foo(bar)baz"
    print(reverseInParentheses(inputString))
