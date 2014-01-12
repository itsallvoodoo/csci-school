import java.io.Serializable;


public class Address implements Serializable{
	Address() { } 
	Address(String inStreet, String inCity, String inState, String inZip)
	{
		street = inStreet;
		city = inCity;
		state = inState;
		zip = inZip;
	}
private String street;
public String getStreet() {
	return street;
}
public void setStreet(String street) {
	this.street = street;
}
public String getCity() {
	return city;
}
public void setCity(String city) {
	this.city = city;
}
public String getState() {
	return state;
}
public void setState(String state) {
	this.state = state;
}
public String getZip() {
	return zip;
}
public void setZip(String zip) {
	this.zip = zip;
}
private String city;
private String state;
private String zip;
}
