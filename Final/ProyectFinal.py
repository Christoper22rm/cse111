import csv
import random
from datetime import datetime
from fpdf import FPDF

# Create teams
def create_teams(team_names):
    return [{"name": name, "points": 0, "matches": []} for name in team_names]

# Generate schedule
def generate_schedule(teams):
    schedule = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            schedule.append((teams[i]["name"], teams[j]["name"]))
    random.shuffle(schedule)
    return schedule

# Record match result
def record_match_result(match, result, teams):
    team1, team2 = match
    for team in teams:
        if team["name"] == team1:
            team["points"] += result[0]
            team["matches"].append({"opponent": team2, "result": result[0]})
        elif team["name"] == team2:
            team["points"] += result[1]
            team["matches"].append({"opponent": team1, "result": result[1]})

# Calculate standings
def calculate_standings(teams):
    return sorted(teams, key=lambda x: x["points"], reverse=True)

# Generate elimination bracket
def generate_bracket(teams):
    standings = calculate_standings(teams)
    return [(standings[i]["name"], standings[len(standings) - 1 - i]["name"]) for i in range(len(standings) // 2)]

# Export results to CSV
def export_results_to_csv(results, file_name):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Team Name", "Points", "Matches"])
        for team in results:
            matches = " | ".join([f"vs {m['opponent']}: {m['result']}" for m in team['matches']])
            writer.writerow([team["name"], team["points"], matches])

# Export results to PDF
def export_results_to_pdf(results, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Tournament Standings", ln=True, align="C")
    pdf.ln(10)

    for team in results:
        pdf.cell(200, 10, txt=f"{team['name']} - Points: {team['points']}", ln=True)
    pdf.output(file_name)

# Load tournament history
def load_tournament_history(file_path):
    history = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            history.append(row)
    return history

# Apply custom rules
def apply_custom_rules(teams, rules):
    for rule in rules:
        for team in teams:
            if rule.get("condition", lambda x: False)(team):
                team["points"] += rule.get("points", 0)

# Display menu
def display_menu():
    print("Welcome to the Sports Tournament Simulator")
    print("1. Create Teams")
    print("2. Generate Schedule")
    print("3. Record Match Result")
    print("4. View Standings")
    print("5. Generate Bracket")
    print("6. Export Results to CSV")
    print("7. Export Results to PDF")
    print("8. Load Tournament History")
    print("9. Exit")

if __name__ == "__main__":
    teams = []
    schedule = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            team_names = input("Enter team names separated by commas: ").split(",")
            teams = create_teams([name.strip() for name in team_names])
        elif choice == "2":
            schedule = generate_schedule(teams)
            print("Schedule:")
            for match in schedule:
                print(f"{match[0]} vs {match[1]}")
        elif choice == "3":
            match = input("Enter match (Team1 vs Team2): ").split(" vs ")
            result = list(map(int, input("Enter results (Team1 score, Team2 score): ").split(",")))
            record_match_result(match, result, teams)
        elif choice == "4":
            standings = calculate_standings(teams)
            print("Standings:")
            for idx, team in enumerate(standings):
                print(f"{idx + 1}. {team['name']} - {team['points']} points")
        elif choice == "5":
            bracket = generate_bracket(teams)
            print("Bracket:")
            for match in bracket:
                print(f"{match[0]} vs {match[1]}")
        elif choice == "6":
            file_name = input("Enter CSV file name: ")
            export_results_to_csv(teams, file_name)
        elif choice == "7":
            file_name = input("Enter PDF file name: ")
            export_results_to_pdf(teams, file_name)
        elif choice == "8":
            file_path = input("Enter file path: ")
            history = load_tournament_history(file_path)
            print("Tournament History:")
            for record in history:
                print(record)
        elif choice == "9":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
