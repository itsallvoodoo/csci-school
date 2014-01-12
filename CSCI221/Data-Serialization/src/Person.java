import java.io.Serializable;
import java.util.ArrayList;


public class Person implements Comparable,Serializable {
private String firstName;
private String lastName;
private ArrayList<Address> addresses = new ArrayList<Address>();
Person(String inFirstName, String inLastName) {
	firstName = inFirstName;
	lastName = inLastName;
}

public void addAddress(String street, String city, String state, String zip)
{
	addresses.add(new Address(street, city, state, zip));
}
public void addHomeAddress(String street, String city, String state, String zip, String aptNo)
{
	addresses.add(new HomeAddress(street, city, state, zip, aptNo));
}
public void addBusinessAddress(String street, String city, String state, String zip, boolean isResidence)
{
	addresses.add(new BusinessAddress(street, city, state, zip, isResidence));
}

public int getAddressCount()
{
	return addresses.size(); 
}

public Address getAddress(int num)
{
	return addresses.get(num);
}

public String getFirstName() {
	return firstName;
}
public void setFirstName(String firstName) {
	this.firstName = firstName;
}
public String getLastName() {
	return lastName;
}
public void setLastName(String lastName) {
	this.lastName = lastName;
}

@Override
public int compareTo(Object o) {
	Person otherPerson = (Person)o;
	if(lastName.equalsIgnoreCase(otherPerson.getLastName()))
		return firstName.compareToIgnoreCase(otherPerson.getFirstName());
	else
		return lastName.compareToIgnoreCase(otherPerson.getLastName());
}

}
