import java.io.DataInputStream;
import java.io.IOException;

public class Menu {
	private Person people[] = new Person[10];
	int nextP = 0;
	int currentP = -1;

	private String getData(String prompt, String defaultv) {
		prompt = prompt + "(press enter to keep value of " + defaultv + ")";
		String data = getData(prompt);
		if (data.isEmpty())
			data = defaultv;
		return data;
	}

	private String getData(String prompt) {
		System.out.print(prompt);
		String data = "";
		DataInputStream mykb = new DataInputStream(System.in);
		try {
			data = mykb.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return data;
	}

	private void addAdress() {
		if (currentP > -1) {
			String type = getData("Enter type (H,B):");
			String street = getData("Enter street:");
			String city = getData("Enter city:");
			String state = getData("Enter state:");
			String zip = getData("Enter zip:");
			if (type.charAt(0) == 'H') {
				String aptNo = getData("Enter aptNo:");
				people[currentP]
						.addHomeAddress(street, city, state, zip, aptNo);

			} else {
				String isResidence = getData("Is this a residence:");
				if (isResidence.charAt(0) == 'Y')
					people[currentP].addBusinessAddress(street, city, state,
							zip, true);
				else
					people[currentP].addBusinessAddress(street, city, state,
							zip, false);
			}

		} else
			System.out.println("No current person");

	}

	private void editPerson() {
		if (currentP > -1) {
			String firstName = getData("Enter First Name:",
					people[currentP].getFirstName());
			String lastName = getData("Enter Last Name:",
					people[currentP].getLastName());
			people[currentP].setFirstName(firstName);
			people[currentP].setLastName(lastName);
		} else
			System.out.println("No current person");
	}

	private void searchPerson() {
		System.out.println("Search for person");
		String firstName = getData("Enter First Name:");
		String lastName = getData("Enter Last Name:");
		currentP = -1;
		for (int i = 0; i < nextP; i++) {
			if (firstName.equalsIgnoreCase(people[i].getFirstName())
					&& lastName.equalsIgnoreCase(people[i].getLastName())) {
				currentP = i;
			}
		}
		if (currentP > -1)
			System.out.println("Found them");
		else
			System.out.println("Could not find them");
	}

	private void addPerson() {
		String firstName = getData("Enter First Name:");
		String lastName = getData("Enter Last Name:");
		currentP = nextP;
		people[nextP++] = new Person(firstName, lastName);

	}

	private void showPeople() {
		for (int i = 0; i < nextP; i++) {
			System.out.format("%s %s\n", people[i].getFirstName(),
					people[i].getLastName());
			for (int j = 0; j < people[i].getAddressCount(); j++) {
				if (people[i].getAddress(j) instanceof BusinessAddress) {
					BusinessAddress ba = (BusinessAddress) people[i]
							.getAddress(j);
					if (ba.isResidence() == true)
						System.out.format("   (Business) %s %s %s %s (Residence)",
								ba.getStreet(), ba.getCity(), ba.getState(),
								ba.getZip());
					else
						System.out.format("   (Business) %s %s %s %s", ba.getStreet(),
								ba.getCity(), ba.getState(), ba.getZip());

				} else {
					HomeAddress ha = (HomeAddress) people[i].getAddress(j);
					System.out.format("   (Home) %s %s %s %s", ha.getStreet(),
							ha.getCity(), ha.getState(), ha.getZip());

				}
				System.out.println();
			}
		}
	}

	private String displayMenu() {
		System.out.println("[A]dd Person");
		System.out.println("[E]dit Person");
		System.out.println("a[D]d Address");
		System.out.println("Sea[R]ch Person");
		System.out.println("[S]how People");

		System.out.println("e[X]it");
		String data = "X";
		DataInputStream mykb = new DataInputStream(System.in);
		try {
			data = mykb.readLine();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return data;
	}

	public static void main(String[] args) {
		Menu mymenu = new Menu();
		String option = mymenu.displayMenu();
		while(!option.equalsIgnoreCase("X"))
		{
			switch(option.charAt(0))
			{
			case  'A':
			case  'a':
				mymenu.addPerson();
				break;
			case 'S':
			case 's':
				mymenu.showPeople();
				break;
			case 'R':
			case 'r':
				mymenu.searchPerson();
				break;
			case 'E':
			case 'e':
				mymenu.editPerson();
				break;
			case 'D':
			case 'd':
				mymenu.addAdress();		
				break;
			}
			option = mymenu.displayMenu();
		}
		
	}
}
