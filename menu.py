import helpers
import database as db


def iniciar():
    while True:
        helpers.clean_screen()

        print("======================")
        print("  Welcome to manager  ")
        print("======================")
        print("[1] List clients      ")
        print("[2] Search client     ")
        print("[3] Add client        ")
        print("[4] Modify client     ")
        print("[5] Delete client     ")
        print("[6] Close Manager     ")
        print("======================")

        option = input("> ")
        helpers.clean_screen()

        match option:
            case "1":
                print("Listing clients...")
                for client in db.Clients.list:
                    print(client)

            case "2":
                print("Searching client...")
                dni = helpers.read_text(3, 3, "DNI (2 int and 1 char)").upper()
                client = db.Clients.search(dni)
                print(client) if client else print("Client not found")

            case "3":
                print("Adding client...")

                dni = None
                while True:
                    dni = helpers.read_text(3, 3, "DNI (2 int and 1 char)").upper()
                    if helpers.validate_dni(dni,db.Clients.list):
                        break
                name = helpers.read_text(2, 30, "Name (2 int and 30 char)").capitalize()
                last_name = helpers.read_text(
                    2, 30, "Last Name (2 int and 30 char)"
                ).capitalize()
                db.Clients.create(dni, name, last_name)
                print("Client added successfully")

            case "4":
                print("Modifying client...")
                dni = helpers.read_text(3, 3, "DNI (2 int and 1 char)").upper()
                client = db.Clients.search(dni)
                if client:
                    name = helpers.read_text(
                        2, 30, f"Name (2 int and 30 char) [{client.name}]"
                    ).capitalize()
                    last_name = helpers.read_text(
                        2, 30, f"Last Name (2 int and 30 char) [{client.last_name}]"
                    ).capitalize()
                    db.Clients.modify(dni, name, last_name)
                    print("Client modified successfully")
                else:
                    print("Client not found")

            case "5":
                print("Deleting client...")
                dni = helpers.read_text(3, 3, "DNI (2 int and 1 char)").upper()
                print("client deleted successfully") if db.Clients.delete(
                    dni
                ) else print("Client not found")

            case "6":
                print("Coming out...")
                break

        input("\n Press RETURN to continue")
