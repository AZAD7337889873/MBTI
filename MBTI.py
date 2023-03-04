# MBTI explanation took from https://www.truity.com/page/16-personality-types-myers-briggs
print("welcome to my personality test based on Myers-Briggs Type Indicator (MBTI)")
a=input(str("choose the first personality type(Introversion(I) or Extraversion(E))\n"))
b=input(str("choose the first personality type(Sensing(S) or Intuition(N))\n"))
c=input(str("choose the first personality type(Thinking(T) vs. Feeling(F))\n"))
d=input(str("choose the first personality type(Judging(J) vs. Perceiving(P))\n"))
arr = a+b+c+d
txt ="your personality type is {}"
print(txt.format(arr))

#types = {"INFP","INTJ","INFJ","INTP","ENFP","ENTJ","ENTP","ENFJ","ISFJ","ISFP","ISTJ","ISTP","ESFJ","ESFP","ESTJ","ESTP"}
types_dict = {"INFP":"The Healer","INTJ":"The Mastermind","INFJ":"The Counselor","INTP":"The Architect",
              "ENFP":"The Champion","ENTJ":"The Commander","ENTP":"The Visionary","ENFJ":"The Teacher",
              "ISFJ":"The Protector","ISFP":"The Composer","ISTJ":"The Inspector",
              "ISTP":"The Craftsperson","ESFJ":"The Provider","ESFP":"The Performer",
              "ESTJ":"The Supervisor","ESTP":"The Dynamo"}
print(types_dict.get(arr, 'invlid input'))


# if arr not in types_dict:
#     print("invalid input")
# else:
#     print(types_dict[arr])


# elif arr == "INFP":
#     print(types_dict['INFP'])
# elif arr == "INTJ":
#     print(types_dict['INTJ'])
# elif arr == "INFJ":
#     print(types_dict['INFJ'])
# elif arr == "INTP":
#     print(types_dict['INTP'])
# elif arr == "ENFP":
#     print(types_dict['ENFP'])
# elif arr == "ENTJ":
#     print(types_dict['ENTJ'])
# elif arr == "ENTP":
#     print(types_dict['ENTP'])
# elif arr == "ENFJ":
#     print(types_dict['ENFJ'])
# elif arr == "ISFJ":
#     print(types_dict['ISFJ'])
# elif arr == "ISFP":
#     print(types_dict['ISFP'])
# elif arr == "ISTJ":
#     print(types_dict['ISTJ'])
# elif arr == "ISTP":
#     print(types_dict['ISTP'])
# elif arr == "ESFJ":
#     print(types_dict['ESFJ'])
# elif arr == "ESFP":
#     print(types_dict['ESFP'])
# elif arr == "ESTJ":
#     print(types_dict['ESTJ'])
# elif arr == "ESTP":
#     print(arr['ESTP'])
# else:
#     print("hello try again")
