import sys, os
import openai



OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def get_response(name, objective, max_date, commitment, current_date):

    part_1 = "Put together a plan called:" + ' ' + name + ' '
    part_2 = "for the following objective:" + ' ' + objective + ' '
    part_3 = "Deadline:" + ' ' + max_date + ". " + "The plan should start at:" + current_date + ". "
    part_4 = "Estimated weekly commitment hours:" + ' ' + commitment + ". "
    part_5 = '''Generate the plan with a list of tasks in JSON format, following the model bellow:
    The term "XXX" is a placeholder.
    Consider "task.group" field as an agregator of similar tasks, so that the plan has a maximum of 5 groups.
    {
    "tasks": [    
        {
        "group": "xxx",
        "title": "xxx",
        "description": "xxx",
        "date": "YYYY-MM-DD",
        "estimated_hours": xxx,
        },
        ...
    ]
    }
    Answer whith the JSON only.
    '''
    PROMPT = part_1 + part_2 + part_3 + part_4 + part_5
    

    prompt_to_send = PROMPT
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= [
          {"role": "system", "content": "You are a planning expert"},
          {"role": "user", "content": prompt_to_send},
        ]
    )

    answer = response['choices'][0]['message']['content']
    return answer.strip()
    


