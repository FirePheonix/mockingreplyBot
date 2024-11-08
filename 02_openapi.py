from openai import OpenAI
client = OpenAI(
    api_key = "ENTER_YOUR_API_KEY_HERE"
)


command = '''[6:58 pm, 05/11/2024] IIIT Sonepat Ojas Dhenge: Lets Do That
[6:58 pm, 05/11/2024] shubham: yessss
[6:59 pm, 05/11/2024] IIIT Sonepat Ojas Dhenge: At What Time Are You Coming Tomorrow?
[6:59 pm, 05/11/2024] shubham: dupher ko aaunga vaise tow
[6:59 pm, 05/11/2024] IIIT Sonepat Ojas Dhenge: Ok
[6:59 pm, 05/11/2024] shubham: 1-2
[6:59 pm, 05/11/2024] shubham: types
[7:00 pm, 05/11/2024] shubham: okay, just do remind me again
[7:00 pm, 05/11/2024] IIIT Sonepat Ojas Dhenge: Ok
[7:00 pm, 05/11/2024] IIIT Sonepat Ojas Dhenge: Bye For Now
[8:01 pm, 05/11/2024] IIIT Sonepat Ojas Dhenge: Are You Able To Send It Now?


'''
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Shubham. You live in India and are fluent in enlish and hindi. You are a coder. Talk like shubham and reply to the chats"},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message)