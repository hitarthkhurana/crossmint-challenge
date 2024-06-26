import requests
import time

def fetch_goal_map(candidate_id):
    url = f"https://challenge.crossmint.io/api/map/{candidate_id}/goal"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch the goal map")


candidate_id = "f9fec5bf-71a8-41ab-b74c-98a4feb400a5"
goal_map = fetch_goal_map(candidate_id)
print(goal_map)


def create_polyanet(candidate_id, row, column):
    url = f"https://challenge.crossmint.io/api/polyanets"
    data = {
        "row": row,
        "column": column,
        "candidateId": candidate_id
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Polyanet created successfully at position:", row, column)
    else:
        print("Failed to create Polyanet at position:", row, column)

def create_soloon(candidate_id, row, column, color):
    url = f"https://challenge.crossmint.io/api/soloons"
    data = {"row": row, "column": column, "color": color, "candidateId": candidate_id}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Soloon created successfully at position:", row, column)
    else:
        print("Failed to create Soloon at position:", row, column)

def create_cometh(candidate_id, row, column, direction):
    url = f"https://challenge.crossmint.io/api/comeths"
    data = {"row": row, "column": column, "direction": direction, "candidateId": candidate_id}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Cometh created successfully at position:", row, column)
    else:
        print("Failed to create Cometh at position:", row, column)

goal_map = goal_map['goal']
def setup_megaverse(candidate_id, goal_map):
    for row_index, row in enumerate(goal_map):
        for col_index, cell in enumerate(row):
            if cell == "POLYANET":
                create_polyanet(candidate_id, row_index, col_index)
            elif "SOLOON" in cell:
                color = cell.split('_')[0].lower() 
                create_soloon(candidate_id, row_index, col_index, color)
            elif "COMETH" in cell:
                direction = cell.split('_')[0].lower()
                create_cometh(candidate_id, row_index, col_index, direction)
            time.sleep(1)  


setup_megaverse(candidate_id, goal_map)
