from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

user_input = input('Enter Travel request : \n')
response = run_travel_agent(
    user_input=user_input,
    thread_id="test_user"
)

print("\nFinal Response : \n")
print(response["answer"])

# For flight test
# res = search_flights("Plan a 7 days Japan trip from India")
# print(res)


# For Tavily Test
# res = tavily_search("Best hotels in Sikkim")
# print(res)