#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai_news.crew import AiNews

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
warnings.filterwarnings("ignore", category=DeprecationWarning)

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'openai',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S'),
        'current_year': str(datetime.now().year)
    }
    
    # inputs_array = [
    #     {
    #         'topic': 'ai agents',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     }, 
    #     {
    #         'topic': 'openai',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     },
    #     {
    #         'topic': 'hugging face',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     }
    # ]
    
    try:
        AiNews().crew().kickoff(inputs=inputs)
        # AiNews().crew().kickoff_for_each(inputs=inputs_array)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()

# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         AiNews().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         AiNews().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
    
#     try:
#         AiNews().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

