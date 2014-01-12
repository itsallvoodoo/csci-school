import java.awt.Button;
import java.awt.Dialog;
import java.awt.Frame;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.MenuBar;
import java.awt.MenuItem;
import java.awt.TextArea;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Collections;


public class GuiMenu extends Frame implements WindowListener,ActionListener {
	private ArrayList<Person> people = new ArrayList<Person>();
	private int nextP = 0;
	private int currentP = -1;
	private TextArea console;
	private java.awt.Menu personMenu;

	class AddressDialog extends Dialog implements WindowListener,ActionListener
	{

		private TextField street;
		private TextField city;
		private TextField state;
		private TextField zip;

		public AddressDialog(Frame owner, String title) {
			super(owner, title, true);
			setSize(400,160);
			addWindowListener(this);
			setLayout(new GridLayout(5,2));
			add(new Label("Street:"));
			add(street = new TextField());
			add(new Label("City:"));
			add(city = new TextField());
			add(new Label("State:"));
			add(state = new TextField());
			add(new Label("Zip:"));
			add(zip = new TextField());
			Button saveButton = new Button("Save");
			add(saveButton);
			saveButton.addActionListener(this);
			
			setVisible(true);
		}

		@Override
		public void windowOpened(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowClosing(WindowEvent e) {
			this.hide();
			
		}

		@Override
		public void windowClosed(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowIconified(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeiconified(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowActivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeactivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			people.get(currentP).addHomeAddress(street.getText(), city.getText(), state.getText(), zip.getText(), "");
			this.hide();
		}
		
	}
	
	class PersonDialog extends Dialog implements WindowListener,ActionListener
	{

		private TextField firstName;
		private TextField lastName;
		private int el;

		public PersonDialog(Frame owner, String title, 
				String dFirstName, String dLastName, int element) {
			super(owner, title, true);
			setSize(400,160);
			addWindowListener(this);
			setLayout(new GridLayout(3,2));
			add(new Label("First Name:"));
			add(firstName = new TextField());
			add(new Label("Last Name:"));
			add(lastName = new TextField());
			Button saveButton = new Button("Save");
			add(saveButton);
			saveButton.addActionListener(this);
			el = element;
			if(!dFirstName.isEmpty())
				firstName.setText(dFirstName);
			if(!dLastName.isEmpty())
				lastName.setText(dLastName);
			
			setVisible(true);
		}

		@Override
		public void windowOpened(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowClosing(WindowEvent e) {
			this.hide();
			
		}

		@Override
		public void windowClosed(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowIconified(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeiconified(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowActivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeactivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			if(el >= 0)
			{
				people.set(el,new Person(firstName.getText(), lastName.getText()));
			}
			else
			{
				currentP = nextP++;  
				people.add(new Person(firstName.getText(), lastName.getText()));
			}
			this.hide();
		}
		
	}

	class SearchDialog extends Dialog implements WindowListener,ActionListener
	{

		TextField firstName;
		TextField lastName;
		public SearchDialog(Frame owner, String title) {
			super(owner, title, true);
			setSize(400,160);
			addWindowListener(this);
			setLayout(new GridLayout(3,2));
			add(new Label("First Name:"));
			add(firstName = new TextField());
			add(new Label("Last Name:"));
			add(lastName = new TextField());
			Button searchButton = new Button("Search");
			add(searchButton);
			searchButton.addActionListener(this);
			setVisible(true);
		}

		@Override
		public void windowOpened(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowClosing(WindowEvent e) {
			this.hide();
			
		}

		@Override
		public void windowClosed(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowIconified(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeiconified(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowActivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void windowDeactivated(WindowEvent e) {
			// TODO Auto-generated method stub
			
		}

		@Override
		public void actionPerformed(ActionEvent e) {
			currentP = -1;
			for(Person cPerson : people) {
				if (firstName.getText().equalsIgnoreCase(cPerson.getFirstName())
						&& lastName.getText().equalsIgnoreCase(cPerson.getLastName())) {
					currentP = people.indexOf(cPerson);
				}
			}
			if (currentP > -1)
				personMenu.enable();
		
			this.hide();
		}
		
	}

	private void showPeople() {
		console.setText("");
		Collections.sort(people);
		for(Person cPerson : people) {
			console.appendText(cPerson.getFirstName() + " " + 
					cPerson.getLastName() + "\n");
			for (int j = 0; j < cPerson.getAddressCount(); j++) {
				if (cPerson.getAddress(j) instanceof BusinessAddress) {
					BusinessAddress ba = (BusinessAddress) cPerson.getAddress(j);
					if (ba.isResidence() == true)
						console.appendText("   (Business) " + 
								ba.getStreet() + " " + ba.getCity() + " " + ba.getState()
								+ " " + ba.getZip() + "(Residence)\n");
					else
						console.appendText("   (Business) " + 
								ba.getStreet() + " " + ba.getCity() + " " + ba.getState()
								+ " " + ba.getZip() + "\n");

				} else {
					HomeAddress ha = (HomeAddress) cPerson.getAddress(j);
					console.appendText("   (Home) " + 
							ha.getStreet() + " " + ha.getCity() + " " + ha.getState()
							+ " " + ha.getZip() + "\n");

				}
			}
		}
	}
	

	
	
	GuiMenu() 
	{
		super("My Patron Database");
		setSize(640,480);
		addWindowListener(this);
		MenuBar mb = new MenuBar();
		setMenuBar(mb);
		java.awt.Menu myMenu = new java.awt.Menu("People");
		mb.add(myMenu);
		personMenu = new java.awt.Menu("Person");
		personMenu.disable();
		mb.add(personMenu);
		MenuItem mi = new MenuItem("Add Person");
		mi.addActionListener(this);
		myMenu.add(mi);
		mi = new MenuItem("Show People");
		mi.addActionListener(this);
		myMenu.add(mi);
		mi = new MenuItem("Search Person");
		mi.addActionListener(this);
		myMenu.add(mi);
		mi = new MenuItem("Edit Person");
		mi.addActionListener(this);
		personMenu.add(mi);
		mi = new MenuItem("Add Address");
		mi.addActionListener(this);
		personMenu.add(mi);
		console = new TextArea(10,60);
		console.setEditable(false);
		add(console);
		setVisible(true);
		FileInputStream fis;
		try {
			fis = new FileInputStream("mydata.dat");
			ObjectInputStream ois = new ObjectInputStream(fis);
			people = (ArrayList<Person>) ois.readObject();
			ois.close();
			fis.close();
		} catch (FileNotFoundException e) {
		} catch (IOException e) {
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
		
	}
	public static void main(String[] args) {
		new GuiMenu();
	}
	@Override
	public void windowOpened(WindowEvent e) {
	}
	@Override
	public void windowClosing(WindowEvent e) {
		try {
			FileOutputStream fis = new FileOutputStream("mydata.dat");
			ObjectOutputStream oos = new ObjectOutputStream(fis);
			oos.writeObject(people);
			oos.close();
			fis.close();
		} catch (FileNotFoundException e1) {
			e1.printStackTrace();
		} catch (IOException e2) {
			e2.printStackTrace();
		}
		
		System.exit(0);
	}
	@Override
	public void windowClosed(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowIconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowDeiconified(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowActivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void windowDeactivated(WindowEvent e) {
		// TODO Auto-generated method stub
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		MenuItem mi = (MenuItem)e.getSource();
		if(mi.getLabel().equalsIgnoreCase("Add Person")) {
			new PersonDialog(this,"Add Person","","",-1);
		}
		else if(mi.getLabel().equalsIgnoreCase("Edit Person")) {
			new PersonDialog(this,"Edit Person",
					people.get(currentP).getFirstName(),
					people.get(currentP).getLastName(),currentP);
		}
		else if(mi.getLabel().equalsIgnoreCase("Show People")) {
			showPeople();
		}
		else if(mi.getLabel().equalsIgnoreCase("Search Person")) {
			new SearchDialog(this,"Search Person");
		}
		else if(mi.getLabel().equalsIgnoreCase("Add Address")) {
			new AddressDialog(this,"Add Address");
		}
		
	}

}
