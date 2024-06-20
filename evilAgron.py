import os
import sys
from bidi.algorithm import get_display

# Clear screen command based on the operating system
clear_screen = "cls" if os.name == "nt" else "clear"

# ANSI escape code for red color
RED = "\033[91m"
RESET = "\033[0m"

logo = f"""
{RED}   , ,, ,
   | || |    ,/  _____  \.
   \_||_/    ||_/     \_||
     ||       \_| . . |_/
     ||         |  L  |
    ,||         |`==='|
    |>|      ___`>  -<'___
    |>|\    /             \,
    \>| \  /  ,    .    .  |
     ||  \/  /| .  |  . |  |
     ||\  ` / | ___|___ |  |     (
  (( || `--'  | _______ |  |     ))  (
(  )\|| (  )\ | - --- - | -| (  ( \  ))
(\/  || ))/ ( | -- - -- |  | )) )  \((
 ( ()||((( ())|         |  |( (( () )
{RESET}"""

# Clear the screen
os.system(clear_screen)

print(get_display(logo + '\n' + '\t' + '@האקרים בישראל בטלגרם\n'))

def load_data(file_path):
    """
    Load data from the specified file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

def save_results(results, query):
    """
    Save the search results to a file.
    """
    file_name = "_".join(query.values()) + '.txt'  # Create a file name based on the query details
    with open(file_name, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(format_result(result) + '\n\n')

def format_result(result):
    """
    Format the result.
    """
    result = result.strip().split('\t')
                       
    formatted_result = f"\nSTART\n" \
                       f"תעודת זהות: {result[0]}\n" \
                       f"שם פרטי: {result[1]}\n" \
                       f"שם משפחה: {result[2]}\n" \
                       f"שם קודם: {result[3]}\n" \
                       f"מין: {result[4]}\n" \
                       f"סטטוס: {result[5]}\n" \
                       f"מצב אישי: {result[6]}\n" \
                       f"רחוב: {result[7]}\n" \
                       f"בית: {result[8]}\n" \
                       f"כניסה: {result[9]}\n" \
                       f"דירה: {result[10]}\n" \
                       f"עיר: {result[11]}\n" \
                       f"מיקוד: {result[12]}\n" \
                       f"טלפון: {result[13]}\n" \
                       f"גיל: {result[14]}\n" \
                       f"תאריך לידה: {result[15]}\n" \
                       f"ארץ לידה: {result[16]}\n" \
                       f"תאריך עליה: {result[17]}\n" \
                       f"תאריך פטירה: {result[18]}\n" \
                       f"אב: {result[19]}\n" \
                       f"מספר זהות האב: {result[20]}\n" \
                       f"אם: {result[21]}\n" \
                       f"מספר זהות האם: {result[22]}\n" \
                       f"מספר זהות בן זוג: {result[23]}\n" \
                       f"מספר זהות משפחה: {result[24]}\n" \
                       f"ילדים: {result[25]}\n" \
                       f"מקור: {result[26]}\n" \
                       f"\nEND\n"
    return formatted_result

def search_data(data, query):
    """
    Search the data for the given query.
    """
    results = []
    for line in data:
        if all(sub_query in line for sub_query in query.values()):
            # Check if the name in the line exactly matches the query
            if query.get('שם', '') in line.split('\t') and \
               query.get('שם משפחה', '') in line.split('\t') and \
               query.get('עיר', '') in line.split('\t') and \
               query.get('מספר תעודת זהות', '') in line.split('\t') and \
               query.get('רחוב', '') in line.split('\t'):
                results.append(line)
    return results

def build_query():
    """
    Build the search query based on user input.
    """
    query = {}

    print("This tool is for searching our database.")
    print("You can search by: name, last name, city, ID number, or street.")
    input("\n\nPress ENTER to start...\n\n")
    print("Starting search...")

    while True:
        os.system(clear_screen)
        print(logo)
        print("1. Select Name")
        print("2. Select Last Name")
        print("3. Select City")
        print("4. Select ID Number")
        print("5. Select Street")
        print("\n6. Start Search\n")
        print_current_query(query)  # Print current search query
        choice = input("\nChoose an option:\n ")

        if choice == '1':
            os.system(clear_screen)
            print(logo)
            name = input("Enter name for search:\n ").strip()
            query['שם'] = name
        elif choice == '2':
            os.system(clear_screen)
            print(logo)
            last_name = input("Enter last name for search:\n ").strip()
            query['שם משפחה'] = last_name
        elif choice == '3':
            os.system(clear_screen)
            print(logo)
            city = input("Enter city for search:\n ").strip()
            query['עיר'] = city
        elif choice == '4':
            os.system(clear_screen)
            print(logo)
            id_number = input("Enter ID number for search:\n ").strip()
            query['מספר תעודת זהות'] = id_number
        elif choice == '5':
            os.system(clear_screen)
            print(logo)
            street = input("Enter street for search:\n ").strip()
            query['רחוב'] = street
        elif choice == '6':
            os.system(clear_screen)
            print(logo)
            if not query:
                print("\nPlease add at least one search condition\n")
                continue
            else:
                print("\nSearch details:\n")
                for key, value in query.items():
                    print(f"{key}: {value}")
                confirm = input("\nDo you want to start the search with these details? (1 - Yes, 2 - No): \n").strip()
                if confirm == '1':
                    break
                else:
                    continue
        else:
            print("Invalid option, please try again.")
            continue

    return query

def print_current_query(query):
    """
    Print the current search query.
    """
    if not query:
        print("No search details entered yet.")
    else:
        print("\nCurrent search conditions:\n")
        for key, value in query.items():
            print(f"{key}: {value}")
        print('\n')

def main():
    try:
        file_path = 'AGRON2006.csv'
        query = build_query()
        print_current_query(query)  # Print current search query before search
        os.system(clear_screen)
        print(logo)
        print("Searching...\n")
        print('\nPlease wait...\n')

        data = load_data(file_path)

        results = search_data(data, query)
        if results:
            print(f"\nFound {len(results)} matching results out of {len(data)} items:\n")
            for result in results:
                print(get_display(format_result(result)))
            save_choice = input("Do you want to save the results? (1- Yes, 2 - No): ").strip()
            if save_choice == '1':
                save_results(results, query)
                print("Results saved successfully.")
        else:
            print("No matching results found.")

    except KeyboardInterrupt:
        print("Goodbye!\nDon't forget to follow us on Telegram @האקרים בישראל !")
        close_choice = input("\nPress ENTER to close the program...\n\n")
        if close_choice == '':
            sys.exit(0)

if __name__ == "__main__":
    main()
